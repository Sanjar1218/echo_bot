#import library for telegram bot
import requests

TOKEN = '5446020024:AAHcDq0gInuUnVWolbamoUNoqbFA490U4N8'
url = "https://api.telegram.org/bot"

def sendMessage(chat_id, text):
    url = f'{url}{TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, params=payload)
    return r.json()