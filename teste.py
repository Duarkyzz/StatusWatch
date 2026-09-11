import requests

url = input("Enter the URL to check: ")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Online")
    else:
        print(f"Offline")

except requests.RequestException as e:
    print(f"An error occurred while checking the URL: {e}")
