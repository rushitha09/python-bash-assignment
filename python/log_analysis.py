from collections import Counter
log_file = "logs/server.log"
info_count = 0
warning_count = 0
error_count = 0
error_messages = []
try:
    with open(log_file, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("INFO"):
                info_count += 1
            elif line.startswith("WARNING"):
                warning_count += 1
            elif line.startswith("ERROR"):
                error_count += 1
                message = line.split("ERROR", 1)[1].strip()
                error_messages.append(message)
    print("=" * 10, "LOG ANALYSIS REPORT", "=" * 10)
    print(f"Total INFO Messages    : {info_count}")
    print(f"Total WARNING Messages : {warning_count}")
    print(f"Total ERROR Messages   : {error_count}")
    print("\nTop 5 Most Frequent Error Messages")
    if error_messages:
        frequency = Counter(error_messages)
        for message, count in frequency.most_common(5):
            print(f"{message} : {count} times")
    else:
        print("No error messages found.")
except FileNotFoundError:
    print("Error: Log file not found.")

except Exception as e:
    print("Error:", e)