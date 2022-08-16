#import library for telegram bot
import requests

TOKEN = '5446020024:AAHcDq0gInuUnVWolbamoUNoqbFA490U4N8'
url = "https://api.telegram.org/bot"
URL = url+TOKEN

def sendMessage(chat_id: int, text: str) -> dict:
    """
    args:
        chat_id: int
        text: str
    return:
        json object
    """
    url = f'{URL}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, params=payload)
    return r.json()
    
def sendPhoto(chat_id: int, photo: str) -> dict:
    """
    args:
        chat_id: int
        photo: str
    return:
        json object
    """
    url = f'{URL}/sendPhoto'
    payload = {'chat_id': chat_id, 'photo': photo}
    r = requests.post(url, params=payload)
    return r.json()

def getLastUpdates() -> tuple:
    """get last updates then returns update_id and message object"""
    url = f'{URL}/getUpdates'
    r = requests.get(url).json()['result'][-1]
    return r['update_id'], r['message']


last_id = -1
while True:
    # getting update_id and message object
    current_id, message = getLastUpdates()
    if current_id!=last_id:
        #storing last update_id
        last_id = current_id
        #chat id
        chat_id = message['chat']['id']
        # checks that photo object exist or not
        if 'photo' in message.keys():
            #photo_id
            photo_id = message['photo'][0]['file_id']
            #sending_photo
            sendPhoto(chat_id, photo_id)
            continue
        #text that send to bot
        text = message['text']
        #sending back the text
        sendMessage(chat_id, text)