import requests
import json
import win32com.client as wincom
import os

city = input('Enter the name of the City :\n')

url=f'https://api.weatherapi.com/v1/current.json?key=5e89b728f74d495c895122120232211&q={city}'

r= requests.get(url)
# print(r.text)
# print(type(r.text))
wdic= json.loads(r.text)
# text = wdic
w=(wdic["current"]["temp_c"])
# text1 = "You Selected City name is ",city
# text = ("The Current Weather is",wdic["current"]["temp_c"],"Centigrades")

speak = wincom.Dispatch("SAPI.SpVoice")

# text = "Python text-to-speech test. using win32com.client"
# speak.Speak(text1)
# speak.Speak(text)

os.system(speak.Speak(f'The Current Weather in {city} is {w} degrees '))
