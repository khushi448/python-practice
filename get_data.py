
# for i in range(0,5,2):
#   print("khushi")


#list[]
# age=12
# has_ans=True
# lis=[age,has_ans,10,"hi"]
# lis[0]="akash"
# print(lis)

#dictionary {}
# person={
#   "name":"Khushi",
#   "age":25
# }
# person["age"]=16
# print(person["age"])

# del person["age"]
# print (person)

#tuples ()--->immutable
# emp=()
# point=(3,5)
# colors=("red","green","blue")

#sets
# number={1,2,3,4,5,6}

# scores=[85,90,85,92,90]

# uniq=set(scores)
 
# score={1,2,3,4,4,4,5}
# print(score)

#funtion
# def greet():
#   print("hello")

# greet()
# greet()
# greet()

# def check(temp):
#   if(temp>30):
#     print("hot")
#   else:
#     print("cold")

# check(31)
# check(17)

# def greet(name,title):
#   print(f"my name is {name} {title}")
 

# greet("khushi","gupta")
# greet("ayush","saraf")

# def calculator(a,b):
#   s=a+b
#   m=a*b
#   d=a/b
#   print(f"sum: {s}")
#   print(f"multiply: {m}")
#   print(f"divide {d}")

# calculator(9,3)

# def calculator(a,b,op):
#   if(op=='+'):
#     return a+b
#   elif(op=='-'):
#     return a-b
#   else:
#     return "invalid"
  
# k=calculator(8,7,'+')
# print(k)
 
#return multiple value
# def func():
#   arr=[1,2,3,4,5,6]
#   first=arr[0]
#   second=arr[-1]
#   return first,second

# f,l=func()
# print(f)
# print(l)
# print(func())

#external tools
#packages
# import math 
# print(math.sqrt(16) )

# import random 
# rand=random.randint(1,10)
# print(rand)
# choi=random.choice(["apple","banana",'grapes'])
# print(choi)
# ch=random.choice([1,2,3,4,4,5,6,7])
# print(ch)

# import pandas as pd

# API
# import requests
# latitude=48.85
# longitude=2.35
# url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
# response=requests.get(url)
# data=response.json()
# type(data)
# print(data["current_weather"]["temperature"])


# import requests
# def weath(latitude,longitude):
#   url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
#   response=requests.get(url)
#   data=response.json()
#   return data["current_weather"]["temperature"]

# london=weath(48.85,2.35)
# tokyo=weath(35.68,139.79)
# print(f"london:{london}")
# print(f"tokyo: {tokyo}")

# import requests
# from datetime import datetime,timedelta
# today =datetime.now()
# week_ago=today-timedelta(days=7)
# start_date=week_ago.strftime("%Y-%m-%d")
# end_date=today.strftime("%Y-%m-%d")
# url=f"https://archive-api.open-meteo.com/v1/archive?latitude=48.8566&longitude=2.3522&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe/Paris"

# response=requests.get(url)
# data=response.json()
# print(data)

# # pandas
# import pandas as pd
# import requests
# from datetime import datetime,timedelta
# today =datetime.now()
# week_ago=today-timedelta(days=7)
# start_date=week_ago.strftime("%Y-%m-%d")
# end_date=today.strftime("%Y-%m-%d")
# url=f"https://archive-api.open-meteo.com/v1/archive?latitude=48.8566&longitude=2.3522&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe/Paris"

# response=requests.get(url)
# data=response.json()
# print(data)


# #-----------------------------
# daily_data=data['daily']
# df=pd.DataFrame({
#   'date':daily_data['time'],
#   'max_temp':daily_data['temperature_2m_max'],
#   'min_temp':daily_data['temperature_2m_min']
# })
# df['date']=pd.to_datetime(df['date'])
# # print(df)

# #--------------------------
#  #matplot lib
# import matplotlib.pyplot as plt

# #create plot
# plt.figure(figsize=(10,6))
# plt.plot(df['date'],df['max_temp'],marker='o',label='Max_Temp')
# plt.plot(df['date'],df['min_temp'],marker='o',label='Min_Temp')

# #add labels and title
# plt.xlabel
# ('Date')
# plt.ylabel('Temperature')
# plt.title('Paris Weather-Past 7 Days')
# plt.legend()

# #rotate x axis labels for redability
# plt.xticks(rotation=45)
# plt.tight_layout()

# #save plot
# plt.savefig('weather_chart1.png')
# plt.show()
  

# #create folder
# import os
# if not os.path.exists('data'):
#   os.makedirs('data')

# #save to csv
# df.to_csv('data/paris_weather.csv',index=False)
# print("Data saved to data/paris_weather.csbv")



#connected to a real apicc
#worked with dates and time
#processed data using pandas
#created a visualization
#handled files and folders
#saved your results

#practical python  

#ERROR HANDLING

# try:
#    result=10/0
# except:
#   print("error")
# print(" khushi")



#OOPS
 #without classes data and function seperate 
# name="OpenAi"
# model="gpt4"
# def generate_response(prompt):
#   #--process prompt
#   return response

# #with class
# class OpenAiclient:
#   def __init__(self,name,model):
#     self.name=name
#     self.model=mpdel
  
#   def generate_response(self,prompt):
#     #process prompt
#     return response

# class Dog:
#   def __init__(self,name,breed):
#     self.name=name
#     self.breed=breed

# class Cat:
#   def __init__(self,name,color):
#     self.name=name
#     self.color=color

# dog1=Dog("buddy","golden retreiver")
# cat2=Cat("tommy","Blue")
  
# print(dog1.name)
# print(cat2.color)

# class APIconfig:
#   def __init__(self,api_key,model="gpt-3.5",max_token=100):
#     self.api_key=api_key
#     self.model=model
#     self.max_token=max_token
#     self.base_url="https://api.openai.com/v1"

# dev_config=APIconfig("sk-dev-key",max_token=50)
# prod_config=APIconfig("sk-product-key","gpt-4",1000)
   
# print(dev_config.model)
# print(prod_config.model)
# print(prod_config.api_key)
# print(prod_config.max_token)


#data validator-methods
# class DataValidator:
#   def __init__(self):#attribute
#     self.errors=[]

#   def validate_email(self,email):#method
#     if '@' not in email:
#       self.errors.append(f"invalid email {email}")
#       return False
#     return True

#   def valiate_age(self,age):
#     if age<0 or age>150:
#       self.errors.append(f"invalid age {age}")
#       return False
#     return True
  
#   def get_errors(self):
#     return self.errors
  
# validator=DataValidator()

# validator.validate_email(email="1234")
# validator.valiate_age(200)

# print(validator.get_errors())


# class Dog:
#   def __init__(self,name):
#     self.name=name

#   def bark(self):
#     print("bark")
  
# tom=Dog(name="Tom")
# print(tom.name)
# tom.bark()

#inheritance



#git/github
#to install git u see video
#to clone repo-> git clone url
#to intialize git in your project
#git init
# git add .
#git commit -m "Initial commit"
#git branch _M main
#git remote add origin https://github.com/khushi448/python-practice.git
#git push -u origin main

