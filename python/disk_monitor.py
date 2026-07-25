import shutil
import csv
from datetime import datetime
try:
    total, used, free = shutil.disk_usage("/")
    total_gb = round(total / (1024 ** 3), 2)
    used_gb = round(used / (1024 ** 3), 2)
    free_gb = round(free / (1024 ** 3), 2)
    usage_percent = round((used / total) * 100, 2)
    print("===== Disk Usage Report =====")
    print(f"Total Space : {total_gb} GB")
    print(f"Used Space  : {used_gb} GB")
    print(f"Free Space  : {free_gb} GB")
    print(f"Usage       : {usage_percent}%")
    if usage_percent > 80:
        print("\nALERT: Disk usage exceeded 80%!")
    else:
        print("\nDisk usage is under control.")
    with open("reports/disk_report.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "Date",
            "Total(GB)",
            "Used(GB)",
            "Free(GB)",
            "Usage(%)"
        ])
        writer.writerow([
            datetime.now(),
            total_gb,
            used_gb,
            free_gb,
            usage_percent
        ])
    print("\nCSV report generated successfully!")
except Exception as e:
    print("Error:", e)