from flask import Flask, render_template, redirect, request, session
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
PASSWORD=os.getenv('password')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="{}".format(PASSWORD),
  database="week6_DB"
)
# print(mydb) #連線完成
mycursor=mydb.cursor() #建立cursor物件
app=Flask(__name__,static_folder='public',static_url_path='/')
app.secret_key='12345678'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    name=request.form['name']
    account=request.form['account']
    password=request.form['password']
    # print(name, account,password)
    if name=="" or account=="" or password=="":
        return redirect('/error?message=任一欄位不可有空值')
    else:
        sql='select account from member where account=%s'
        val=(account,) #這寫法比較特別要注意
        mycursor.execute(sql,val)
        result = mycursor.fetchall()
    if result!=[]:
        return redirect('/error?message=帳號已有人註冊')
    else:
        sql='insert into member(name, account,password) values (%s,%s,%s)'
        val=(name, account, password)
        mycursor.execute(sql,val)
        mydb.commit()
        return redirect('/')

@app.route('/signin', methods=['POST'] )
def signin():
    account=request.form['account']
    password=request.form['password']
    sql="select * from member where account=(%s) and password=(%s)"
    val=(account,password)
    mycursor.execute(sql,val)
    # mycursor.execute("select * from member where account='{}' and password='{}'".format(account,password))
    result = mycursor.fetchone()
    print(result)
    if result!=None:
        session['user_ID']=result[0]
        session['name']=result[1]
        session['account']=result[2]
        return redirect('/member')
    else:
        return redirect('/error?message=帳號或密碼輸入錯誤')

@app.route('/signout')
def signout():
    del session['name']
    return redirect('/')

@app.route('/member')
def member():
    if 'name' in session:
        sql="select message.id, name, message from member inner join message on member.id=message.user_ID;"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        result.sort(reverse = True)
        messages=''
        for i in result:
            messages+="{}:{}<br>".format(i[1],i[2])
        return render_template('member.html',username=session['name'],message=messages)
    else:
        return redirect('/')

@app.route('/error')
def error():
    message=request.args.get('message',"發生錯誤")
    return render_template('error.html',msg=message)

@app.route('/message', methods=['post'] )
def message():
    message=request.form['message']
    sql='insert into message (user_ID, message) values(%s,%s)'
    val=(session['user_ID'], message)
    mycursor.execute(sql,val)
    mydb.commit()
    return redirect('/member')

app.run(port=3000)