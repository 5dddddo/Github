import requests

# 1. requests 통해 요청 보내기
url = 'https://api.bithumb.com/public/ticker/'
response = requests.get(url)
# print(response.text)

# .json() : dictionary로 결과값 return
res_dict = response.json()
print(res_dict)

# data 안의 opening_price 변수 추출
result = res_dict['data']['opening_price']
print(result)