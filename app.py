from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


@app.route('/')
def booklist():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('mybooklist.html')

@app.route('/api/booklist', methods=['POST'])
def booklist():
	# 1. 클라이언트가 준 title, author, review 가져오기.

	# 2. DB에 정보 삽입하기
	# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/api/booklist',methods=['GET'])
def booklist():
    return jsonify({'result': 'success', 'booklist': booklist})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)