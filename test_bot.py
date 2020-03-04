import requests as requests

url = "https://api.telegram.org/bot930822082:AAFe0l8hv4VXgu_PcQ5Tsxwk-tM1MvA424s"

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]


def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response


def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            send_message(get_chat_id(update), get_message_text(update))
            update_id += 1
