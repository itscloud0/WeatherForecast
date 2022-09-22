import ssl
import smtplib
import os
import const as keys
import certifi
from os import system
import requests
from pprint import pprint
from email.message import EmailMessage

def forecastStr(city):

    API_KEY = '211f6c862df69b5b11bef20fdbbe2ede'

    system('clear')
    base_url = "http://api.openweathermap.org/data/2.5/weather?units=metric&appid=" + API_KEY +"&q="+city

    weather_data = requests.get(base_url).json()

    #pprint(weather_data)

    location = weather_data['name'] +  ", " + weather_data['sys']['country']

    temp = round(weather_data['main']['temp'],1)

    feels = round(weather_data['main']['feels_like'],1)

    desc = (weather_data['weather'][0]['description']).capitalize()

    humid = weather_data['main']['humidity']

    deg = " C°"

    return("Weather in "  + location + '\n' + '\n' + "Description: " 
    + desc + '\n' + '\n' + "Current temperature: " + str(temp)  + deg + '\n'
    + '\n' + "Feels like: " +  str(feels) + deg + '\n' + '\n' + "Humidity: " + str(humid) + "%" + '\n')

email_sender = 'wthfrcst@gmail.com'
email_password = keys.CODE

cityStr = input("Enter a city: ")
email_receiver = input("Enter an email: ")

subject = 'Weather Forecast'
body = forecastStr(cityStr)

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context = context) as smtp: 
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())




