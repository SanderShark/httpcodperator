import argparse
import requests
import time

def check_status_codes(base_url, filename):
    success_codes = []

    with open(filename, 'r') as file:
        for line in file:
            code = line.strip()
            url = f"{base_url}/{code}"
            response = requests.get(url)
            print(f"Checking status code {code}... Response code: {response.status_code}")
            if response.status_code == 200:
                success_codes.append(code)
            time.sleep(0.2)  # Limiting to 5 requests per second

    with open('success_codes.txt', 'w') as success_file:
        success_file.write('\n'.join(success_codes))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check status codes against a base URL')
    parser.add_argument('base_url', type=str, help='Base URL to check status codes against')
    parser.add_argument('filename', type=str, help='File containing status codes, one per line')
    args = parser.parse_args()

    check_status_codes(args.base_url, args.filename)
