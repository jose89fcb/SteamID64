import requests
import json
import os


SteamID64 = input("Url de steam: ")

url = requests.get(f"https://jose89fcb.webcindario.com/a/steamID64.php?url={SteamID64}")
SteamID64 = json.loads(url.text)


Steam = url.json()['SteamID64']


print(f'Steam ID 64: {Steam}')
os.system("pause")

