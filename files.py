from datetime import datetime
from config import filespath

def now():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

false_starts = [
    '/suggest@coachrollerbot ',
    '/suggest@coachrollerbot',
    '/suggest ',
    '/suggest'
    ]

def err_log(error):
    with open(f'{filespath}logs.txt', 'a+', encoding='UTF-8') as logs:
        logs.write(f'\n\n{error}, {now()}')
    return "Произошла ошибка, свяжитесь с @Nevokapr"

def add_sugg(user_fullname, user_id, text):
    if text in false_starts:
        return 'Вы ничего не предложили.\nНапишите команду /suggest руками, и напишите текст после неё. **В одном сообщении.**'
    try:
        with open(f"{filespath}suggestions.csv", "a+", encoding="utf-8") as file:
            file.write(f'\n\n{user_id}, {user_fullname}, {text}')
    except Exception as e:
        return err_log(e)
    return f"Спасибо, {user_fullname}, предложение успешно сохранено, Nevokapr вас не забудет!"

def grab(user_fullname, user_name, user_id, func, text=''):
    try:
        with open(f"{filespath}users.csv", "a+", encoding="utf-8") as file:
            file.write(f'\n\n{user_fullname}, {user_name}, {user_id}, {func}, {text}, {now()}')
    except Exception as e:
        return err_log(e)
