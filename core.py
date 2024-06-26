from random import randint
import requests
import pandas
import config

#function to read csv and get random task of any passed type
def outputter(task_type):
    
    if task_type == 'text':
        file_path = config.filespath + '/task_text.csv'
    else:
        file_path = config.filespath + '/task_media.csv'
    df = pandas.read_csv(
        f'{file_path}',
        index_col=False,
        delimiter='№'
    )
    return str(list(df.sample(n=1)['body'])[0])

FIN = [
    ".",
    " =)",
    " :)",
    " ;)",
    "...",
    "!",
    "!!!",
    "))0",
    "!!11!1",
    " ^_^",
    ", немедленно!",
    ", так-то!"
]

def send_support():
    return config.support_msg

def compose_dbl(user_id, user_name):
    if user_id in config.USER_LIB:
        user = config.USER_LIB[user_id]
    else:
        user = user_name
    roll_text = f'{user}, напиши ' + outputter('text')
    roll_media = ('Пришли ' + outputter('media'))
    message = roll_text + ',\n\nИ/или,\n\n' + roll_media
    return message

def askhole_compose(user_id, user_name):
    if user_id in config.USER_LIB:
        user = config.USER_LIB[user_id]
    else:
        user = user_name
    ending = '__взято с askhole.io__'
    df = pandas.read_csv(
        (f'{config.askhole_path} + /askhole.csv'),
        index_col=False,
        delimiter='№'
    )
    question = str(list(df.sample(n=1)['body'])[0])
    message = f'{user}, {question}' + '\n\n' + ending
    return message


def xkcd_comp():
    #Randomizing link, and concatenating into a url, then requesting from api
    latest = requests.get('https://xkcd.com/info.0.json', timeout=10).json()['num']
    random = randint(1, latest)
    photo = requests.get(f'https://xkcd.com/{random}/info.0.json', timeout=10).json()['img']
    caption = f'Here goes an xkcd.com/{str(random)}'
    return [photo, caption]

def cat_f():
    req = requests.get(
        f'https://api.thecatapi.com/v1/images/search?mime_types=gif,jpg,png?api_key={config.cat_api}',
        timeout=10,
        ).json()
    photo = req[0]['url']
    caption = 'Random cat from api.thecatapi.com'
    return [photo, caption]
