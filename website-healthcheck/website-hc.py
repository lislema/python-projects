import requests
import csv
from datetime import datetime

input_file = "websites.txt"

def check_website(url):
    """Check the health of a website"""
    try:
        response = requests.get(url, timeout=5)
        status = "Online" if response.status_code == 200 else "Offline"
        return response.status_code, response.elapsed.total_seconds() * 1000, status
    except requests.exceptions.RequestException:
        return None, None, "Offline"

def log_results(data):
    """Log results to a CSV file"""
    with open("log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

with open(input_file, mode="r") as file:
    websites = [line.strip() for line in file if line.strip()]

# Initialize log file with headers

with open("log.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "URL", "Response Time (ms)", "Status Code", "Status"])

print(f"Checking {len(websites)} websites...")
for website in websites:
    status_code, response_time, status = check_website(website)
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{website} - {status} - {status_code if status_code else 'N/A'}")
    log_results([time_stamp, website, response_time or "N/A", status_code or "N/A",status])



