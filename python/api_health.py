import requests
# Input file with URLs
with open("urls.txt", "r") as f:
    urls = [line.strip() for line in f if line.strip()]
failed_urls = []
print("===== API Health Check =====")
for url in urls:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[OK] {url} -> {response.status_code}")
        else:
            print(f"[FAILED] {url} -> {response.status_code}")
            failed_urls.append(f"{url} -> {response.status_code}")
    except Exception as e:
        print(f"[ERROR] {url} -> {e}")
        failed_urls.append(f"{url} -> {e}")
# Save failed endpoints into a report
if failed_urls:
    with open("reports/api_report.txt", "w") as report:
        report.write("Failed Endpoints:\n")
        for entry in failed_urls:
            report.write(entry + "\n")
    print("\nReport generated: reports/api_report.txt")
else:
    print("\nAll endpoints are healthy!")
