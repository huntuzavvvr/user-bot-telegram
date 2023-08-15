import json
import sys
from pyrogram import Client, filters
from pyrogram.types import InputPhoneContact
from configs import configure_send
from constants import API_ID, API_HASH


# Определение адресата
def get_username(app, recipient, data):
    if recipient[0] != "@" and recipient[0] != "+":
        try:
            a = str(app.get_users(recipient))
            content_type = "id"
        except Exception as error:
            data["status"] = "error"
            data["error_type"] = "user_id error"
            # Завершение программы, вывод ошибки
            sys.exit(json.dumps(data, ensure_ascii=False))
    elif recipient[0] == "+":
        try:
            a = str(app.import_contacts([InputPhoneContact(recipient, "addressee")]).users[0])
            content_type = "num"
        except Exception as error:
            data["status"] = "error"
            data["error_type"] = "phone number error"
            # Завершение программы, вывод ошибки
            sys.exit(json.dumps(data, ensure_ascii=False))
    else:
        try:
            a = str(app.get_users(recipient))
            content_type = "name"
        except Exception as error:
            data["status"] = "error"
            data["error_type"] = "username error"
            # Завершение программы, вывод ошибки
            sys.exit(json.dumps(data, ensure_ascii=False))
    username = "@" + json.loads(a).get("username")
    return username, content_type


# Отправка сообщения
def send_message(app, username, content, data):
    try:
        if content["text"] != "":
            app.send_message(username, content["text"])
        if content["photo"] != "":
            app.send_photo(username, content["photo"])
    except Exception as error:
        data["status"] = "error"
        data["error_type"] = "error while sending a message"
    else:
        data["status"] = "succeed"
    return json.dumps(data, ensure_ascii=False)


def main(params):
    with open('some.txt', 'w') as f:
        f.write('выаыфафыафаф')
    args = json.loads(params)
    data = {}
    app = Client('session', API_ID, API_HASH)
    app.start()
    content = args["content"]
    recipient = args["addressee"]
    username, content_type = get_username(app, recipient, data)
    result = send_message(app, username, content, data)
    app.stop()
    print(result)


if __name__ == '__main__':
    main(configure_send())

