from flask import Flask,render_template
import json
from flask import make_response
from flask_cors import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    error = '用户名或密码错误！'
    return render_template('index.html')

@app.route('/signin', methods=['GET','POST'])
def login():
	error = '用户名或密码错误！'
	user = 'admin'
	if True :
		return render_template('main.html', user = user)
	else:
		return render_template('index.html', error = error)  

@app.route('/tree', methods=['GET','POST'])
def tree():
    return app.send_static_file('treeData.json')

@app.route('/ytcombobox', methods=['GET','POST'])
def ytcombobox():
    return app.send_static_file('ytcomboboxData.json')

@app.route('/test', methods=['GET','POST'])
def test():
    return '{"success":"true"}'

@app.route('/ck_info', methods=['GET','POST'])
def ck_info():
    return app.send_static_file('ck_info.html')

if __name__ == '__main__':
    app.run()
