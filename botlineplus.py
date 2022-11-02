# https://www.youtube.com/watch?v=kJxkx_FNfGI&lc=Ugz0rJ4rB05PBmtS55R4AaABAg.9htpCvboDP79huv8IPvwO-&ab_channel=MaoLoop
import requests
from datetime import datetime as d
import time

def main(message):
  url = "https://notify-api.line.me/api/notify"
  token = "DaCpa4i9O8w9TegSZnDzHroTRMexN56Vc5IsVZZMgc3"
  header = {"content-type": "application/x-www-form-urlencoded", 
            "Authorization": "Bearer " + token}
  return requests.post(url, headers=header, data=message)


url = "https://api.bitkub.com"
price = 0
mycoin = ["THB_BTC", "THB_DOGE", "THB_ZIL", "THB_GALA"]

date = d.now()
day = date.strftime("%Y-%m-%d %H:%M")

while True:
      req = requests.get(url + "/api/market/ticker")
      data = req.json()

      for i in mycoin:
          coin = data[i]
          last = coin["last"]
          high = coin["high24hr"]
          low = coin["low24hr"]
          
          if price != last:
            msg = f"{day} \n" \
                f"ตอนนี {mycoin} \n" \
                f"ตอนนี {i} \n" \
                f"ราคาล่าสุดอยู่ที่ : {last} THB \n" \
                f"---------------- \n" \
                f"24 H สูงสุด : {high} THB \n" \
                f"24 H ต่ำสุด : {low} THB \n" \
                f"-------------- \n"
            price = last
            main({"message": msg})  
            time.sleep(3600)