import requests
import time

TOKEN = "MASUKKAN_TOKEN_MU_DI_SINI"
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