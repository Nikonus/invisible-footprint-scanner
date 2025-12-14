# scan.py
from email_scan import scan_email
from phone_scan import scan_phone

def main():
    print("\nInvisible Internet Footprint Scanner\n")
    print("1. Scan Email")
    print("2. Scan Phone Number")

    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == "1":
        email = input("Enter email address: ").strip()
        scan_email(email)

    elif choice == "2":
        phone = input("Enter phone number (with country code): ").strip()
        scan_phone(phone)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
