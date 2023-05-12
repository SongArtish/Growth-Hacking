from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   # 플라스크 객체 생성

# 여기서 nomadlogos는 DB 이름임
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/nomadlogos'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username