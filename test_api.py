import os
import httpx

USER_TOKEN = os.getenv("USER_TOKEN")  

BASE_URL = "https://api.alteg.io/v1/employees"  

def main():
    headers = {
        "X-User-Token": 4d8b1b277cad78fd47f057fcf1de2686,
        "Accept": "application/json"
    }
    try:
        r = httpx.get(BASE_URL, headers=headers, timeout=20.0)
        print("Status:", r.status_code)
        print("Response:", r.json())
    except Exception as e:
        print("Ошибка запроса:", e)

if __name__ == "__main__":
    main()
