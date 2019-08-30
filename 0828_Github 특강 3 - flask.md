# 0828_Github 특강 3 - Flask

### MSA ( Micro Service Architecture )

- Application을 낮은 결합도를 가진 서비스의 모임으로 구조화하는 서비스 지향 아키텍처 (SOA) 스타일의 SW 개발 기법
- 모듈성을 개선시키고 병렬성을 향상 시킴

- <-> **Monolithic** : UI와 로직 코드가 하나로 묶여있는 구조



### Python Flask를 이용한 Github 예제

- Setting

![1566988201309](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566988201309.png)

1. python 설치

   -  Add Python 3.7 to PATH :  체크
   - Install Now 

   ![1567143756311](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1567143756311.png)

   - warning 해결

     `$ python -m pip install --upgrade pip`

2. flask 설치

   - 초경량 WSGI(웹 서버와 웹 앱의 인터페이스를 위한 프레임워크) web application Framework

   `$ pip install flask`

3. chatbot dir를 생성하고    `$ mkdir chatbot`

   chatbot dir로 이동한 후   `$ cd chatbot`

   code Editor 실행               ` $ code .`

<br>

- #### app.py

1. hello 함수 : hello를 찍어보자!

   - @app.route() Decorator :  URL을 함수와 연결해줌

   ``` python
   from flask import Flask
   app = Flask(__name__)
   
   # localhost:5000/
   @app.route('/')
   def home():
       return 'hello'
   ```

   - flask 서버 시작 

     `$ flask run`

   ![1566957197863](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566957197863.png)

   - URL 주소에 localhost:5000/ 입력 시 hello 출력 확인

2. hello 함수 : 사용자가 url에 입력한 단어를 출력해보자!

   - Variable route : url에서 문자를 가져와 변수로 사용

     - localhost:5000/hello/이 위치에 입력한 문자를 가져오려면

       ​									 \< ... \>으로 표시

     - 함수의 인자로 \< \> 에 입력한 변수 이름을 넘겨줌

     ``` python
     @app.route('/hello/<name>')
     def hello(name):
         return f'hello {name}' # f-string
     	return 'hello {}'.format(name) # string formatting
     	return 'hello ' + name # string concatenation
     ```

   - flask 서버 시작 

     `$ flask run`

   - 실행 결과

     ![1567151600498](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1567151600498.png)

3. square 함수 : 숫자를 입력 받아 제곱해보자!

   - \< \> 안에 변수의 type을 지정해서 입력 받을 수 있음

   - **flask의 return 값은 무조건 string이어야 함**

     - int -> string으로 casting 해야 함

     ``` python
     @app.route('/square/<int:num>')
     def square(num):
         # number를 제곱하여 반환
         return f'{str(num ** 2)}'
     ```

   - flask 서버 시작

   - 실행 결과

     ![1567156156724](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1567156156724.png)

4. lotto 함수

   ``` python
   @app.route('/lotto')
   def lotto():
       # List.sort : 원본까지 정렬하고 return X
       # sorted() : 정렬된 새로운 리스트를 return
       
       winner = [3,5,12,13,33,39]
       # random.sample(Collection, 샘플 수)
       # 1~45 사이의 난수 6개를 정렬
      	user = sorted(random.sample(range(1,46),6))
       
       # 6개 일치 -> 1등
       # 5개 일치 -> 3등
       # 4개 일치 -> 4등
       # 3개 일치 -> 5등
       
       # set : 집합 자류구조
       # & : 교집합
       # set & set : 같은 원소를 가진 set 생성
       cnt = set(winner) & set(result)
       for i in winner:
           # user list가 i를 원소로 가지고 있으면
           if i in user :
               cnt += 1
       res = "꽝"
       if cnt == 6:
           res = '1등'
       elif cnt == 5:
           res = '3등'
       elif cnt == 4:
           res = '4등'
       elif cnt == 3:
           res = '5등'
       return res + cnt
   ```

   - 실행 결과

     ![1567156047363](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1567156047363.png)

   

- #### lotto.py

  - 동행 복권 API를 이용해 당첨 번호를 받아오자!

  - json 형식으로 drwtNo1~6이 당첨 번호

  ![1566970302365](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566970302365.png)

  - **Requests** library를 이용

    - HTTP 요청을 보다 간편하게 이용할 수 있음

    - Request 설치

      `$ pip install requests`

  ``` python
  '''
  requests를 통해 동행 복권 API예 요청을 보내고
  1등 번호를 가져와 python list로 만듦
  '''
  
  import requests
  
  # 1. requests 통해 요청 보내기
  url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
  response = requests.get(url)
  print(response.text)
  ```

  ![1566970571077](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566970571077.png)
  <bR>

  - dictionary ( {key:value,... } ) 형태로 출력 

  ``` python
  # .json() : json 형식의 문자열을 dictionary로 결과값 return
  res_dict = response.json()
  print(res_dict)
  ```

  ![1566970808246](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566970808246.png)

  - 1등 번호 6개 담긴 result list 출력

  ``` python
  # result = []
  # result.append (res_dict['drwtNo1'])
  # result.append (res_dict['drwtNo2'])
  # result.append (res_dict['drwtNo3'])
  # result.append (res_dict['drwtNo4'])
  # result.append (res_dict['drwtNo5'])
  # result.append (res_dict['drwtNo6'])
  for i in range(6):
      result.append (res_dict[f'drwtNo{i+1}'])
  print(result)
  ```

  ![1566971080265](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566971080265.png)



- #### crypto.py

  - bithumb API를 이용해 비트코인 현재가를 받아오기

    - data -> opening_price의 값
    - dictionary 구조에서는 res_dict\['data']['opening_price']로 타고 들어갈 수 있음

    ![1567165787114](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1567165787114.png)

  <br>

  ``` python
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
  ```

  ![1566973582994](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566973582994.png)

  <br>

--------------

#### git 공부하기 유용한 사이트

- git : [https://git-scm.com](https://git-scm.com/)

- gitignore 파일 생성 : <http://gitignore.io/api/java>

- 동행  로또 API :   <https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1>

- JSON Viewer : https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?hl=ko&hc_location=ufi

- Bithumb Open API : https://apidocs.bithumb.com/docs/ticker

- 

  |                       | >                                                            |
| --------------------- | ------------------------------------------------------------ |
  | JSON Viewer           | <https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?hl=ko&hc_location=ufi> |
  |                       | <https://apidocs.bithumb.com/docs/ticker>                    |
  | 논산훈련소 Tip Github | <https://github.com/krta2/awesome-nonsan>                    |
  | telegram web          | <https://web.telegram.org>                                   |
  | telegram api          | https://api.telegram.org/bot<token>/METHOD_NAME              |
  | telegram sendMessage  | https://api.telegram.org/bot<토큰>/sendMessage?chat_id=<나의chat_id>&text=<내용> |
  | chatbot 코드          | <https://github.com/edu-john/t4ircc_chatbot>                 |