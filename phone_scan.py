# phone_scan.py

def scan_phone(phone):
    print(f"\n[+] Scanning phone number: {phone}\n")

    if phone.startswith("+91"):
        print("Country   : India")
    elif phone.startswith("+1"):
        print("Country   : USA")
    else:
        print("Country   : Unknown")

    digits = phone.replace("+", "").replace(" ", "")

    if digits.isdigit() and len(digits) >= 10:
        print("Validity  : Looks valid")
    else:
        print("Validity  : Invalid format")

    print("\n⚠️ Phone OSINT is limited to public info only.")
