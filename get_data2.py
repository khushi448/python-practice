#------1----
import pandas as  pd
import requests
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
today=datetime.now()
week_ago=today-timedelta(days=7)

start=week_ago.strftime("%Y-%m-%d")
end=today.strftime("%Y-%m-%d")
url=f"https://archive-api.open-meteo.com/v1/archive?latitude=22.572645&longitude=88.363892&start_date={start}&end_date={end}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Asia/Kolkata"
response=requests.get(url)
data=response.json()
print(data)
#------------2----------
daily_data=data["daily"]
df=pd.DataFrame({
'date':daily_data["time"],
'max_temp':daily_data["temperature_2m_max"],
'min_temp':daily_data["temperature_2m_min"]
})
df['date']=pd.to_datetime(df['date'])
print(df)
#--------3-------
plt.figure(figsize=(10,5))
plt.plot(df['date'],df['max_temp'],marker='o',label='Max_Temp')
plt.plot(df['date'],df['min_temp'],marker='o',label='Min_Temp')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('kolkata weather forecast in last 7 days')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('weather_chart.png')
plt.show()
import os
if not os.path.exists('data'):
  os.makedirs('data')
  df.to_csv('data/kolkata_weather.csv',index=False)
print("Data saved to data/kolkata_weather.csv")
# date,max_temp,min_temp
# 2026-02-12,29.3,16.7
# 2026-02-13,28.8,16.9
# 2026-02-14,29.2,16.5
# 2026-02-15,29.7,17.4
# 2026-02-16,29.5,16.6
# 2026-02-17,30.2,16.8
# 2026-02-18,31.1,18.0
# 2026-02-19,31.8,18.4