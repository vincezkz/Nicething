#coding: utf-8
from flask import Flask
from flask import render_template
from flask import request
import Server
import Common
app = Flask(__name__)

@app.route('/')
def hello_world():
    name='hello！！！！world2'
    return render_template('hellowork.html', name=name)

@app.route('/login',methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        _userserver = Server.UserServer()
        username=request.form['username']
        password=request.form['password']
        if _userserver.loginserver(username,password) == Common.LoginStatus.success:
            message = "Login Success!"
        elif _userserver.loginserver() == Common.LoginStatus.fail:
            message = "Password is wrong!"
        else:
            message = "User is NoExist!"
        return render_template('login.html',message)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    pass




if __name__ == '__main__':
    app.run()