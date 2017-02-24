from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    name='hello world1'
    return render_template('hellowork.html', name=name)




if __name__ == '__main__':
    app.run()