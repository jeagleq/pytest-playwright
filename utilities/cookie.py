import os
import json

def load_cookies_from_file(file_name="state.json"):
    # path to cookie file
    login_file = os.path.join(os.path.dirname(__file__),"..", file_name)

    # existing check and reading of the cookies
    if os.path.exists(login_file):
        with open(login_file, "r", encoding="utf-8") as file:
            cookies = json.load(file)
        return cookies
    else:
        print(f"The file {login_file} does not exist.")
        return []
cookies = load_cookies_from_file()
print("Returned cookies:", cookies)