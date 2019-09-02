# 0828_Github 특강 4 - Telegram

- ㅇ

![1566973636546](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566973636546.png)

commit 을 순서대로 하고 싶을때 , 스냅샷 따로 찍고픔!

-> add를 따로 따로



![1566973953353](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566973953353.png)





.gitignore 파일 추가해서 추적하지 않을 파일명 추가

commit msg : 명령형으로 쓰자



- git tagging

  - git tag : tag 조회하기
  - git tag  -a (annotated) TAG_NAME -m (msg) "설명" (커밋해시,이름표)
  - git tag -d TAG_NAME : TAG 삭제
  - git checkout TAG_NAME
    - v1

  ![1566969354791](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566969354791.png)

  - ​	v2

![1566969368606](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566969368606.png)

![1566969854068](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1566969854068.png)





### telegram 예제

1. 텔레그램가입

2. BotFather

   /newbot

   user이름 입력

   bot이름 입력

3. user이름으로 검색

4. 사용할 method 

   getMe

   getUpdates

   sendMessage

5. <https://api.telegram.org/bot<token\>/getMe>

https://api.telegram.org/bot\<token\>/sendMessage?chat_id=939575516&text=고통없쉬

## chatbot 예제

mkdir chatbot



telegram web  <https://web.telegram.org>  telegram api  https://api.telegram.org/bot<token>/METHOD_NAME  telegram sendMessage  https://api.telegram.org/bot<토큰>/sendMessage?chat_id=<나의chat_id>&text=<내용>  chatbot 코드  <https://github.com/edu-john/t4ircc_chatbot>

