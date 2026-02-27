import requests
import time

URL1 = "https://www.liptovskaosada.com/index.php/samosprava/uznesenia-a-zapisnice-oz"
URL2 = "https://www.liptovskaosada.com/index.php/samosprava/uznesenia-a-zapisnice-oz/678-uznesenia-a-zapisnice-rok-2026"
H = {"User-Agent": "Mozilla/5.0"}

for i in range(20):
    try:
        requests.get(URL1, headers=H, timeout=10)
        time.sleep(1)
        r = requests.get(URL2, headers=H, timeout=10)
        print(f"OK {i+1}/20 status={r.status_code}")
        time.sleep(10)
    except Exception as e:
        print(f"Chyba: {e}")
        time.sleep(5)
print("Hotovo!")
