# install requests, win10toast
import requests
from win10toast import ToastNotifier
import json
import time

def getUpdate():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    # print(data)
    text = f'Confirmed cases: {data["cases"]} \nDeaths: {data["deaths"]} \n Recovered: {data["recovered"]}'

    while True:
        toast = ToastNotifier
        toast.show_toast("Covid-19 Update", text, duration=5)
        time.sleep(3600)

getUpdate()