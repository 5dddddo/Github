'''
requests를 통해 동행 복권 API예 요청을 뽀냬어
1등 번호를 가져와 python list로 만듦
'''

import requests

# 1. requests 통해 요청 보내기
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
response = requests.get(url)
# print(response.text)

# .json() : dictionary로 결과값 return
res_dict = response.json()
# print(res_dict)

list = []
list.append (res_dict['drwtNo1'])
list.append (res_dict['drwtNo2'])
list.append (res_dict['drwtNo3'])
list.append (res_dict['drwtNo4'])
list.append (res_dict['drwtNo5'])
list.append (res_dict['drwtNo6'])

print(list)