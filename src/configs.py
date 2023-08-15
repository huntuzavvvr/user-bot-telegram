import json


def configure_send():
    d = {"content": {"text": "", "photo": "", "video": ""}}
    addressee = input("Кому отправить (@username/номер телефона с +7/tg_id): ")
    flag = True
    while flag:
        content = input("Что отправить (введите текст/фото): ")
        if 'текст' in content:
            d["content"]["text"] = input("Введите текст: ")
            flag = False
        if 'фото' in content:
            d["content"]["photo"] = input("Введите ссылку на фото: ")
            flag = False
    d["addressee"] = addressee
    a = json.dumps(d, ensure_ascii=False)
    return a

