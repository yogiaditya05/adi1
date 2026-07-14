import requests
import json

# Your Postman Mock API URL (Fixed and Public)
url = "https://485ab272-b860-4c62-80f4-fa6a80a8c9d1.mock.pstmn.io/students"

try:
    # Sending a GET request to the API
    # Headers are optional now as the mock is public
    response = requests.get(url)
    
    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()
        print("Successfully fetched data from API:\n")
        print(json.dumps(data, indent=4))
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        print(f"Response: {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
