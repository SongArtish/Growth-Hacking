# Note



## Glitch

온라인 개발환경이다.

- https://glitch.com으로 접속해 우측 상단의 `Remix`를 클릭한다.
- 이를 통해서 완성된 코드를 로딩한다.
- 온프레미스서버(Window 내 자체서버)에서 작업 도중 문제가 생기면 온라인 개발환경 사용!



## Flask Server

1. Flask를 이용하면 사용자 정의 웹서버를 만들 수 있음
2. 사용자의 요청이 들어올 때마다 동적으로 HTML 코드를 만들어내는 웹서버임

```python
# server.py
from flask import Flask
import random

app = Flask(__name__) # __name__: 모듈의 이름을 가지고 있는 변수로, 현재 파일의 이름을 나타냄

@app.route('/')
def index():
    # return 'hi'
    return 'random : <strong>' + str(random.random()) + '</strong>'

app.run(debug=True)
# 만약 문제가 생기면 run method에서 포트번호 변경가능
# app.run(port=5001, debug=True)
```



## Routing

사용자의 요청을 어떤 함수가 응답할 것인가를 연결하는 것

- 외부에서 주소요청이 들어오면 이를 담당하는 것이 함수인데, 이 함수의 작업을 진행하는 것이 routing임
- Routing 을 진행하는 작업자는 router임
- `@app.route`를 이용해 경로를 지정하며, 해당 코드 아래에 요청을 처리할 함수를 지정
- URI 경로 상 변하는 부분이 있다면 `<변수이름:데이터타입>`의 형식으로 패턴을 지정할 수 있음

```python
@app.route('/read/<int:id>/')
def read(id):
    print(id)
    return 'Read ' + str(id)
```



## TEST