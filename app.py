from Configuration import Configuration
import time
import requests
import json
import traceback
from database import db
print (time.time())
while '1' == '1':
  try:
    url = "https://computo.oep.org.bo/api/v1/resultado/presidente"
    payload = ""
    headers = {
      'authority': 'computo.oep.org.bo',
      'accept': 'application/json, text/plain, */*',
      'captcha': 'nocaptcha',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43',
      'content-type': 'application/json',
      'origin': 'https://computo.oep.org.bo',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://computo.oep.org.bo/',
      'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
      'Cookie': '__cfduid=db06081b80a4f14f67af930bf25f630941603139715'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    text = response.text.encode('utf8').decode()
    txtJson = json.loads(text)
    txtJson["registerDate"] = int(round(time.time() * 1000))
    txtJson["type"] = "mundial"
    db.presidente.insert_one(txtJson)
  except:
    traceback.print_exc()
  finally:
    time.sleep(Configuration.SECONDS) #60 seconds.