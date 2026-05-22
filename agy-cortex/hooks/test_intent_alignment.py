import os
import json
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock

# Add hooks directory to path to import intent_alignment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import intent_alignment

class TestIntentAlignment(unittest.TestCase):
    def setUp(self):
        # Create a temporary transcript file
        self.temp_transcript = tempfile.NamedTemporaryFile(delete=False, suffix=".jsonl", mode="w", encoding="utf-8")
        
        # Write mock transcript entries
        self.temp_transcript.write(json.dumps({
            "step_index": 0,
            "source": "USER_EXPLICIT",
            "type": "USER_INPUT",
            "content": "Implement a post-execution tool for L4/L5"
        }) + "\n")
        
        self.temp_transcript.write(json.dumps({
            "step_index": 1,
            "source": "MODEL",
            "type": "PLANNER_RESPONSE",
            "content": ">>> [L4 | SENIOR | Gemini 3.1 Pro] Delegating task..."
        }) + "\n")
        
        self.temp_transcript.close()

    def tearDown(self):
        # Clean up temporary transcript
        os.unlink(self.temp_transcript.name)

    def test_extract_session_info(self):
        original_prompt, is_l4_l5 = intent_alignment.extract_session_info(self.temp_transcript.name)
        self.assertEqual(original_prompt, "Implement a post-execution tool for L4/L5")
        self.assertTrue(is_l4_l5)

    def test_check_env_for_agent(self):
        with patch.dict(os.environ, {"ANTIGRAVITY_AGENT_NAME": "senior"}):
            self.assertTrue(intent_alignment.check_env_for_agent())

        with patch.dict(os.environ, {"ANTIGRAVITY_AGENT_NAME": "junior"}):
            self.assertFalse(intent_alignment.check_env_for_agent())

    @patch("requests.post")
    @patch.dict(os.environ, {"GEMINI_API_KEY": "fake-key"})
    def test_analyze_intent_alignment_success(self, mock_post):
        # Mock successful response from Gemini
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "candidates": [{
                "content": {
                    "parts": [{
                        "text": '{"aligned": true, "feedback": "All changes look good."}'
                    }]
                }
            }]
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        aligned, feedback = intent_alignment.analyze_intent_alignment("Prompt", "Diff")
        self.assertTrue(aligned)
        self.assertEqual(feedback, "All changes look good.")

    @patch("requests.post")
    @patch.dict(os.environ, {"GEMINI_API_KEY": "fake-key"})
    def test_analyze_intent_alignment_failure(self, mock_post):
        # Mock alignment failure response from Gemini
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "candidates": [{
                "content": {
                    "parts": [{
                        "text": '{"aligned": false, "feedback": "Missing test case."}'
                    }]
                }
            }]
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        aligned, feedback = intent_alignment.analyze_intent_alignment("Prompt", "Diff")
        self.assertFalse(aligned)
        self.assertEqual(feedback, "Missing test case.")

if __name__ == "__main__":
    unittest.main()
