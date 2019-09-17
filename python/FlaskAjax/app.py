from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/data',methods=['GET','POST'])
def getdata():
    print('hello')
    data = request.args.get


    return 'list'




if __name__ == '__main__':
    app.run()
