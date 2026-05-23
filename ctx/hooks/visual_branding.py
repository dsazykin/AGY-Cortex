import sys
import json
import os

def main():
    try:
        # Read stdin
        input_data = sys.stdin.read()
        
        # Write to debug log
        with open(r"C:\Users\yikes\Code\AGY Cortex\hook_debug.log", "w", encoding="utf-8") as f:
            f.write(f"CWD: {os.getcwd()}\n")
            f.write(f"ENV: {dict(os.environ)}\n")
            f.write(f"STDIN:\n{input_data}\n")
            
        # Return valid JSON on stdout
        print(json.dumps({}))
    except Exception as e:
        with open(r"C:\Users\yikes\Code\AGY Cortex\hook_debug.log", "a", encoding="utf-8") as f:
            f.write(f"ERROR: {str(e)}\n")
        print(json.dumps({}))

if __name__ == "__main__":
    main()
