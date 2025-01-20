import requests # type: ignore
import pytest # type: ignore
from utilities.readConfig import ReadConfig
from utilities.cookie import load_cookies_from_file  


class TestPytestDemo:
    @pytest.mark.api
    def test_get_items(self):
        my_cookie = load_cookies_from_file()
        cookie_value = None
        for cookie in my_cookie["cookies"]:
            if cookie["name"] == "tokenp_":
                cookie_value = cookie["value"]
                break
        if my_cookie:
            # SEND REQUEST
            requests_data = {
                "cookie": cookie_value,
                "flag": True
            }
            headers= {
                "Content-Type": "application/json",
            }
            response = requests.post(f"{ReadConfig.getApplicationAPIURL()}viewcart", headers=headers, json = requests_data)
            # ASSERT
            if response.status_code == 200:
                print("Request was successful.")
            else:
                print(f"Request failed with status {response.status_code}")
        else:
            print("No cookies found to send with the request.")