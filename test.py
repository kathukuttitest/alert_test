from email import message
import ccxt
import pandas_ta as ta
import pandas as pd
import requests
url = "https://api.telegram.org/bot5308554635:AAHXPltt3MUI3XRfLME-rQDYoRILrsmuqKs/sendMessage?chat_id=-1001595590550&parse_mode=HTML&"
exchange = ccxt.binance()

bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='15m', limit=50)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])

rsi = df.ta.rsi()

last_row = rsi.iloc[-1]



if last_row >= 70:
    alert = f"ETH is <b>overbought</b> - RSI value is {last_row}" 
   
    file = {
        "text" : str(alert)
    } 
    requests.get(url, params=file)
if last_row <= 30:
    alert = f"ETH is <b>oversold</b> - RSI value is {last_row}"  
   
    file = {
        "text" : str(alert)
    }

    requests.get(url, params=file)
        


