import requests

API_KEY = input('Введите ключ API_KEY к сервису Yandex-translate: ')

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(key, in_text_file, out_text_file, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & in_text_file = <файл с переводимым текстом>
     & out_text_file =  <файл с переводом>
     & from_lang=<напр es (испанский), de(немецкий), fr(французский)
     & to_lang = <на какой переводить, по умолчанию русский>
    :return: <возвращаю текст перевода>
    """
    with open(in_text_file, 'r', encoding="utf-8") as f:
        text = f.read()
    params = {
        'key': key,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }


    response = requests.get(URL, params=params)
    try:
        json_ = response.json()
    except ConnectionError as ce:
        print(ce)
    with open(out_text_file,'w', encoding = 'utf-8') as f:
        f.write(''.join(json_['text']))
    return ''.join(json_['text'])

print(translate_it(API_KEY, 'ES.txt','ES-RU.txt','es','ru'))
print(translate_it(API_KEY, 'DE.txt','DE-RU.txt','de','ru'))
print(translate_it(API_KEY, 'DE.txt','DE-EN.txt','de','en'))
print(translate_it(API_KEY, 'FR.txt','FR-RU.txt','fr'))

