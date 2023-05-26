from flask import Flask, render_template, request
from static.data.topics import topics

app = Flask(__name__) # __name__: 모듈의 이름을 가지고 있는 변수로, 현재 파일의 이름을 나타냄

@app.route('/')
def index():
    return render_template('index.html', topics=topics, data=None)

@app.route('/create/', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html', data=None)
    elif request.method == 'POST':
        data = {
            'id': len(topics),
            'title': request.form['title'],
            'body': request.form['body']
        }
        topics.append(data)
        return render_template('index.html', topics=topics, data=data)    

@app.route('/read/<int:id>/')
def read(id):
    data = {
        'id': id,
        'title': '',
        'body': ''
    }
    for topic in topics:
        if id == topic['id']:
            data['title'] = topic['title']
            data['body'] = topic['body']
            break
    return render_template('index.html', topics=topics, data=data)

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        data = {
            'id': id,
            'title': '',
            'body': ''
        }
        for topic in topics:
            if id == topic['id']:
                data['title'] = topic['title']
                data['body'] = topic['body']
                break
        return render_template('create.html', data=data)
    elif request.method == 'POST':
        pass

if __name__ == '__main__':
    app.run(debug=True)
# 포트번호 변경 가능: app.run(port=5001, debug=True)