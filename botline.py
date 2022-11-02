import requests
def main(message):
  url = "https://notify-api.line.me/api/notify"
  token = "DaCpa4i9O8w9TegSZnDzHroTRMexN56Vc5IsVZZMgc3"
  header = {"content-type": "application/x-www-form-urlencoded", 
            "Authorization": "Bearer " + token}
  return requests.post(url, headers=header, data=message)
url = "https://api.bitkub.com"
price = 0
while True:
      req = requests.get(url + "/api/market/ticker")
      data = req.json()
      last = data["THB_BTC"]["last"]
      high = data["THB_BTC"]["high24hr"]
      low = data["THB_BTC"]["low24hr"]
      if price != last:
            msg = f"ตอนนี้ Bitcoin \n" \
              f"ราคาล่าสุดอยู่ที่ : {last} \n" \
              f"-----------------" \
              f"24 H สูงสุด : {high}" \
              f"24 H ต่ำสุด : {low}" \
              f"--------------"
      main({"message": msg})
      price = last