import ccxt
# import pandas_ta as ta
import pandas as pd
import requests






exchange = ccxt.binance()


data = exchange.fetch_ohlcv('BTCUSDT',"15m", limit=5)
df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
df['Date']= pd.to_datetime(df['Date'], unit="ms")

last_row = df.iloc[-2]
 
if last_row.Volume >= 2500:
  img_url = "https://api.chart-img.com/v1/tradingview/advanced-chart?width=800&height=600&interval=15m&theme=light&key=5da40c6a-9cfb-4be4-8555-ca057139bdf4"
  bot_url = "https://api.telegram.org/bot5308554635:AAHXPltt3MUI3XRfLME-rQDYoRILrsmuqKs/sendPhoto?chat_id=-1001595590550&parse_mode=HTML&"
  file = {
      'photo' : img_url,
      'caption' : f"<b>BTC/USDT - Hight Volume Alert (15m)</b> \n\n Volume - {last_row.Volume} \n\n @cryptoguruakacg"
  }
  requests.post(bot_url,json=file)
