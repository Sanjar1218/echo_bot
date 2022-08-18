#import library for telegram bot
import requests

TOKEN = '5446020024:AAHcDq0gInuUnVWolbamoUNoqbFA490U4N8'
url = "https://api.telegram.org/bot"
URL = url+TOKEN



def sendMessage(chat_id: int, text: str) -> dict:
    url = f'{URL}/sendMessage'

    button = {
            'text':'button',
        }
    inlinekeyboard = [
        [button, button, button]
    ]
    reply = {
        'keyboard': inlinekeyboard,
    }

    payload = {
        'chat_id': chat_id,
        'text': text,
        
     }

    r = requests.post(url, params=payload, json={'reply_markup':reply})
    return r.json()

print(sendMessage(555351863, 'text'))