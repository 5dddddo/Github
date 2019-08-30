"""
python���� telegram message ������

"""

import requests

# 1. getUpdates�� ���� chat_id�� ������
id_url = 'https://api.telegram.org/bot<token>/getUpdates'
response = requests.get(id_url)
res_dict = response.json()
chat_id = str(res_dict['result'][0]['message']['chat']['id'])
print(chat_id)
# 2. 
base_url = 'https://api.telegram.org'
token = MY_TOKEN
method = 'sendMessage'
msg = '�̹��'
url = f'{base_url}/bot{token}/{method}?chat_id={chat_id}&text={msg}'
requests.get(url)