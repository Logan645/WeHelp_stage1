from flask import Flask, render_template, request, session, redirect
import pymongo
import certifi
import os
from dotenv import load_dotenv
load_dotenv() #敏感資料應該用.env黨來排除，避免將帳號密碼發佈到github這類公開社群
Account=os.getenv('Account')
PASSWORDS=os.getenv('PASSWORDS')

app=Flask(__name__,static_folder='public',static_url_path='/')
app.secret_key='12345678'
client = pymongo.MongoClient(
    f"mongodb+srv://{Account}:{PASSWORDS}@mycluster.g4ddrju.mongodb.net/?retryWrites=true&w=majority",
tlsCAFile=certifi.where()
)
db = client.login_data #選擇要操作的database

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/member')
def member_page():
    if 'accountID' in session:
        return render_template('member.html')
    else:
        return redirect('/')

@app.route('/error')
def error():
    message=request.args.get('msg','發生問題，請聯繫客服')
    return render_template('error.html',error_msg=message)

@app.route('/signin', methods=["POST"])
def signin():
    account_ID=request.form['account_ID']
    print(account_ID)
    passwords=request.form['passwords']
    collecttion=db.member_data
    data=collecttion.find_one({
        "$and":[
            {"accountID":account_ID},
            {"passwords":passwords}
        ]
    })
    if account_ID == "" or passwords== "": #空字串用""，不是None，也不是Null
        return redirect('/error?msg=請輸入帳號、密碼')
    elif data==None:
        return redirect('/error?msg=帳號、或密碼輸入錯誤')
    else:
        session['accountID']=data['accountID']
        print('登入成功')
        return redirect('/member')
    # return redirect('/error?msg=請輸入帳號、密碼')
    # return redirect('/member')

@app.route('/signout')
def signout():
    del session['accountID']
    return redirect('/')

#原本要以這個路由轉介到/square/<Number>，但對前端多一點了解後，可以直接在前端完成，來少做一次連線
# @app.route('/calculate')
# def calculate():
#      number=request.values.get('number')
#      return redirect('/square/{}'.format(number))
 
@app.route('/square/<Number>')
def square(Number):
    # number=request.args.get('number','')
    # number=request.values.get('number')
    num=int(Number) #一開始接收到的數字是字串
    square_number=num*num
    # return square_number
    return render_template('square.html',number=square_number)

app.run(port='3000')
