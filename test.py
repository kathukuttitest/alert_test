import ccxt
# import pandas_ta as ta
import pandas as pd
import requests
import time

exchange = ccxt.binance()


while(True):
  data = exchange.fetch_ohlcv('BTCUSDT',"15m", limit=5)
  df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
  df['Date']= pd.to_datetime(df['Date'], unit="ms")

  last_row = df.iloc[-2]
  
  if last_row.Volume >= 2500:
   
    file = {
        'photo' : img_url,
        'caption' : f"<b>BTC/USDT - Hight Volume Alert (15m)</b> \n\n Volume - {last_row.Volume} \n\n @cryptoguruakacg"
    }
    requests.post(bot_url,json=file)
  else:
    bot_url = "https://api.telegram.org/bot5308554635:AAHXPltt3MUI3XRfLME-rQDYoRILrsmuqKs/sendMessage?chat_id=-1001595590550&parse_mode=HTML&"
    file = {
      'text' : f'not much volume in btc {last_row.Volume}'
    }
    requests.post(bot_url,json=file)
    time.sleep(300)
