"""
python으로 telegram message 보내기

"""

import requests

# 1. getUpdates를 통해 chat_id를 가져옴
id_url = 'https://api.telegram.org/bot<token>/getUpdates'
response = requests.get(id_url)
res_dict = response.json()
chat_id = str(res_dict['result'][0]['message']['chat']['id'])
print(chat_id)
# 2. 
base_url = 'https://api.telegram.org'
token = MY_TOKEN
method = 'sendMessage'
msg = '이밥오'
url = f'{base_url}/bot{token}/{method}?chat_id={chat_id}&text={msg}'
requests.get(url)