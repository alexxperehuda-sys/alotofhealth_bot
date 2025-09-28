import httpx

USER_TOKEN = "4d8b1b277cad78fd47f057fcf1de2686"

url = "https://api.alteg.io/api/v1/companies"


headers = {
    "X-User-Token": USER_TOKEN
}

try:
    response = httpx.get(url, headers=headers, timeout=10)
    print("Status:", response.status_code)
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.text)
except Exception as e:
    print("Request failed:", str(e))

