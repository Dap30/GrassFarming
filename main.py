import requests
import time

TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJseGtPeW9QaWIwMlNzUlpGeHBaN2JlSzJOSEJBMSJ9.eyJ1c2VySWQiOiIybzNGWGdIYk9Xcm1hcDBDSjBBS2pkR0luN2ciLCJzZXNzaW9uSWQiOiIyd0ZmSXBvRHMybDRlYVlDckNJZTcxQmZuR2siLCJpYXQiOjE3NDU2NDIxNjUsIm5iZiI6MTc0NTY0MjE2NSwiZXhwIjoxNzQ4MjM0MTY1LCJhdWQiOiJ3eW5kLXVzZXJzIiwiaXNzIjoiaHR0cHM6Ly93eW5kLnMzLmFtYXpvbmF3cy5jb20vcHVibGljIn0.VVQ7eax72N2Br6hQskFOsUsrAXN4DHUHXMjSniIfy1_BxNBJATWTiri4M4k7Bxh7AtLPB_3DZcynoPWdBySorlyiP-PXaFfFZKTiPj7SIg6NG_sV6B05pWDyJTYMRWVMFetExHofH8-ybuqz0y4j9sZV0GMbpCcLpHJ5RBpYSr1F05pcrAnSStZYv89_BaDkb3ZfzYbIqNvnRJXBxpoqD61bk4kP094gjzxqM04uRj5aCi4FX8juYm8WdjS36JAp-ZjSC3kABuiaLRv1g-S8GT4GyW_crF8AEPPHfqXaW3Nu7GnoiUp7sKx4GxoNLJBtNBKiHMEZ8l-1EDs2MpB9Vw"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def farm_loop():
    while True:
        try:
            response = requests.get("https://app.grass.io/api/user", headers=HEADERS)
            if response.status_code == 200:
                print("[✅] Farming successful.")
            else:
                print(f"[❌] Failed: {response.text}")
        except Exception as e:
            print(f"[⚠️] Error: {str(e)}")
        time.sleep(60)  # ulangi tiap 1 menit

if __name__ == "__main__":
    farm_loop()
