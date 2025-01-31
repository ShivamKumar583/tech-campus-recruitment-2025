import sys
import os
import re
from datetime import datetime

def format_log_line(line):
    pattern = r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})\.\d+ - (\w+) - (.+)"
    match = re.match(pattern, line)

    if match:
        date, time, log_level, message = match.groups()
        return f"{date} {time} {log_level} {message}"  # No extra dot at the end
    
    return None  # Return None for lines that don't match the format

def extract_logs(log_file, date):
    """
    Extracts and reformats logs from the given log file for the specified date.
    Saves the reformatted logs in an 'output' directory.
    """
    try:
        output_dir = "output"
        output_file = f"{output_dir}/output_{date}.txt"

        print(f"🔍 Searching logs for date: {date}")
        print(f"📂 Log File Path: {log_file}")

        os.makedirs(output_dir, exist_ok=True)

        found_logs = 0  

        with open(log_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
            for line in f_in:
                formatted_line = format_log_line(line.strip())

                if formatted_line and formatted_line.startswith(date):
                    f_out.write(formatted_line + "\n")  # Ensure correct line breaks, no extra dots
                    found_logs += 1

        if found_logs > 0:
            print(f"✅ Extracted {found_logs} log(s) for {date}. Check: {output_file}")
        else:
            print(f"⚠️ No logs found for {date}.")
    
    except FileNotFoundError:
        print(f"❌ Error: Log file not found - {log_file}")
        sys.exit(1)
    except PermissionError:
        print(f"❌ Error: Permission denied - {output_file}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Usage: python src/extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date = sys.argv[1]

    log_file = os.path.join(os.path.dirname(__file__), "test_logs.log")

    if not os.path.exists(log_file):
        print(f"❌ Log file not found: {log_file}")
        sys.exit(1)

    extract_logs(log_file, date)
