# platforms.py
import requests

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Dev.to": "https://dev.to/{}",
    "Medium": "https://medium.com/@{}"
}

def check_platforms(username):
    results = {}

    for name, url in PLATFORMS.items():
        profile_url = url.format(username)

        try:
            response = requests.get(profile_url, timeout=5)

            if response.status_code == 200:
                print(f"{name:<10}: FOUND")
                results[name] = 1
            else:
                print(f"{name:<10}: NOT FOUND")
                results[name] = 0

        except:
            print(f"{name:<10}: ERROR")
            results[name] = 0

    return results
