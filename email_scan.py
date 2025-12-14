# email_scan.py
import hashlib
import requests

def scan_email(email):
    print(f"\n[+] Scanning email: {email}\n")

    # ---- Gravatar Check ----
    email_hash = hashlib.md5(email.lower().encode()).hexdigest()
    gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?d=404"

    response = requests.get(gravatar_url)

    if response.status_code == 200:
        print("Gravatar  : FOUND (Used by GitHub / WordPress)")
    else:
        print("Gravatar  : NOT FOUND")

    # ---- Domain Intelligence ----
    domain = email.split("@")[-1]

    print(f"Domain     : {domain}")

    if domain in ["gmail.com", "yahoo.com", "outlook.com"]:
        print("Provider   : Common email provider")
    else:
        print("Provider   : Custom / company domain")

    print("\nNote: Only public indicators checked.")
