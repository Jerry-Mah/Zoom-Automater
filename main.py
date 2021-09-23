import webbrowser
from datetime import datetime
import time
import pandas as pd


df = pd.read_csv("C:\\Users\\91986\\Desktop\\timings.csv")

def meeting_start(link):
    webbrowser.open(link) 



while True:
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):
        row = df.loc[df['timings']==now]
        link = str(row.iloc[0,1])
        meeting_start(link)
        print("Meeting has started")
        break
    else:
        print("Meeting will start soon")
        time.sleep(20)



