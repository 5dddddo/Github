from flask import Flask
import random
import requests
app = Flask(__name__)
@app.route('/')
def home():
    return 'hello'

# 1. 주문서를 만들고 -> @app.route('/name') 부분
# / : root
# 2. 해당 주문이 들어왔을 때 무엇을 할지 정의

@app.route('/name')
def name():
    return '오은애'

# Variable routing : <>
# 사용자가 입력한 값을 name 변수에 대입
@app.route('/hello/<name>')
def hello(name):
    return f'hello {name}'

@app.route('/square/<int:num>')
def square(num):
    # number를 제곱하여 반환
    return f'{str(num ** 2)}'

@app.route('/menu')
def menu():
    foods = ['대우식당','고갯마루','진가와','바스버거']

    res = random.choice(foods)
    return f'{res}'

@app.route('/lotto')
def lotto():
    # .sort : 원본까지 정렬
    # sorted() : 복사본만 정렬
        
    # 1. requests 통해 요청 보내기
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
    response = requests.get(url)
    # print(response.text)

    # .json() : dictionary로 결과값 return
    res_dict = response.json()
    # print(res_dict)

    # 1등 번호 6개 담긴 result list 출력
    result = []
    # result.append (res_dict['drwtNo1'])
    # result.append (res_dict['drwtNo2'])
    # result.append (res_dict['drwtNo3'])
    # result.append (res_dict['drwtNo4'])
    # result.append (res_dict['drwtNo5'])
    # result.append (res_dict['drwtNo6'])

    for i in range(6):
        result.append (res_dict[f'drwtNo{i+1}'])
    #  print(result)
    user = sorted(random.sample(range(1,46),6))

    # 만약 6개의 숫자가 모두 일치하면 1등
    # 만약 5개의 숫자가 일치하면 3등
    # 만약 4개의 숫자가 일치하면 4등
    # 만약 3개의 숫자가 일치하면 5등

    # set : 집합 자료구조
    # & : 교집합
    cnt = set(result) & set(user)
    # for i in re:
    #     if i in user :
    #         cnt += 1
    res = '꽝'
    if len(cnt) == 6 :
        res ='1등'
    elif len(cnt) == 5 :
        res = '3등'
    elif len(cnt) == 4 :
        res = '4등'
    elif len(cnt) == 3:
        res = '5등'
    return str(user) + res