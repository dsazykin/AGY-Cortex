import sys
import os
import json
import subprocess

def log_message(msg):
    sys.stderr.write(f"[IntentAlignment] {msg}\n")

def get_git_diff():
    try:
        # Get all changes compared to HEAD (both staged and unstaged)
        res = subprocess.run(["git", "diff", "HEAD"], capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except Exception as e:
        log_message(f"Error getting git diff: {e}")
        return ""

def extract_session_info(transcript_path):
    original_prompt = ""
    is_l4_l5 = False
    
    if not transcript_path or not os.path.exists(transcript_path):
        log_message(f"Transcript path not found: {transcript_path}")
        return original_prompt, is_l4_l5

    try:
        with open(transcript_path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    entry = json.loads(line)
                    # Check for original user prompt (USER_INPUT type or USER_EXPLICIT source)
                    if not original_prompt:
                        if entry.get("type") == "USER_INPUT" or entry.get("source") == "USER_EXPLICIT":
                            original_prompt = entry.get("content", "").strip()
                    
                    # Detect if L4 (Senior) or L5 (Architect) is involved
                    # 1. Search in the content of planner responses, tool calls, or other fields
                    content_str = str(entry).lower()
                    if "senior" in content_str or "architect" in content_str or "gemini-3.1-pro" in content_str or "gemini-3.5-pro" in content_str:
                        is_l4_l5 = True
                    if ">>> [l4" in content_str or ">>> [l5" in content_str:
                        is_l4_l5 = True
                except Exception:
                    pass
    except Exception as e:
        log_message(f"Error parsing transcript.jsonl: {e}")
        
    return original_prompt, is_l4_l5

def check_env_for_agent():
    # Check environment variables for agent names or IDs
    for k, v in os.environ.items():
        k_upper = k.upper()
        v_lower = str(v).lower()
        if "AGENT" in k_upper or "ROLE" in k_upper or "MODEL" in k_upper:
            if "senior" in v_lower or "architect" in v_lower or "l4" in v_lower or "l5" in v_lower:
                return True
    return False

def analyze_intent_alignment(original_prompt, git_diff):
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        log_message("Warning: No GEMINI_API_KEY or GOOGLE_API_KEY found in environment. Skipping automated diff review.")
        return True, "No API key found in environment to run alignment checks."

    import requests
    
    prompt_to_gemini = f"""You are an expert AI software architect and quality assurance agent.
Your task is to analyze the following Git Diff against the User's Original Prompt to verify if the implementation aligns with the user's intent.

=== ORIGINAL PROMPT ===
{original_prompt}

=== GIT DIFF ===
{git_diff}

=== INSTRUCTIONS ===
1. Verify if the changes in the Git Diff satisfy all the requirements and constraints in the Original Prompt.
2. Check for any mismatches, deviations, unintended side effects, or missing implementation details.
3. Determine if the alignment is successful (true) or if there are issues that require correction (false).
4. Provide constructive, precise feedback. If there are issues, list them clearly so the agent can fix them.

You MUST respond with a valid JSON object matching this schema:
{{
  "aligned": true or false,
  "feedback": "A detailed explanation of the alignment. If aligned is false, list the specific issues that need to be corrected. If true, summarize the verified changes."
}}
Do NOT include any markdown formatting (like ```json) in your response. Return ONLY the JSON object.
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt_to_gemini
            }]
        }],
        "generationConfig": {
            "responseMimeType": "application/json"
        }
    }

    try:
        log_message("Requesting Gemini to verify intent alignment...")
        res = requests.post(url, json=payload, headers=headers, timeout=30)
        res.raise_for_status()
        
        res_json = res.json()
        text_response = res_json["candidates"][0]["content"]["parts"][0]["text"].strip()
        
        # Strip markdown tags if the model ignored generationConfig instructions
        if text_response.startswith("```"):
            text_response = text_response.strip("`").strip()
            if text_response.startswith("json"):
                text_response = text_response[4:].strip()
                
        data = json.loads(text_response)
        aligned = data.get("aligned", True)
        feedback = data.get("feedback", "No feedback provided by the verification model.")
        return aligned, feedback
    except Exception as e:
        log_message(f"Error calling Gemini API for alignment check: {e}")
        return True, f"Failed to check intent alignment due to API error: {e}"

def main():
    try:
        # Parse stdin payload
        stdin_data = sys.stdin.read().strip()
        payload = {}
        if stdin_data:
            try:
                payload = json.loads(stdin_data)
            except Exception as e:
                log_message(f"Failed to parse stdin payload: {e}")

        # Extract transcript path from context
        context = payload.get("context", {})
        transcript_path = context.get("transcriptPath", "")

        # Extract session info
        original_prompt, is_l4_l5 = extract_session_info(transcript_path)
        
        # Double check environment variables
        if not is_l4_l5:
            is_l4_l5 = check_env_for_agent()

        log_message(f"Stop hook invoked. Active Agent L4/L5: {is_l4_l5}")

        # If it is L4/L5 agent, run the diff review
        if is_l4_l5:
            git_diff = get_git_diff()
            if not git_diff:
                log_message("No uncommitted changes detected. Skipping diff review.")
                print(json.dumps({}))
                return

            if not original_prompt:
                log_message("Original prompt not found in transcript. Skipping diff review.")
                print(json.dumps({}))
                return

            # Perform the intent alignment check
            aligned, feedback = analyze_intent_alignment(original_prompt, git_diff)
            
            if not aligned:
                log_message("⚠️ INTENT ALIGNMENT MISMATCH DETECTED!")
                log_message(feedback)
                # Return continue decision to block Stop and force re-entry to the execution loop
                print(json.dumps({
                    "decision": "continue",
                    "message": f"\n[Intent Alignment Checker] Intent alignment mismatch detected!\nFeedback:\n{feedback}\nPlease adjust the implementation to align with the original prompt."
                }))
                return
            else:
                log_message("✅ Intent alignment verified successfully.")
                log_message(feedback)

        # Proceed with normal stopping
        print(json.dumps({}))
    except Exception as e:
        log_message(f"Unexpected error in hook: {e}")
        print(json.dumps({}))

if __name__ == "__main__":
    main()
