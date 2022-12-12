 #project main file
from flask import Flask,render_template,request,redirect
import pymysql
#creating object for class Flask
app=Flask(__name__)
@app.route('/')
def index():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todolist")
        cu=db.cursor()
        sql="select * from labrr"
        #sql="select * from task where id=2"
        cu.execute(sql)
        data=cu.fetchall()
        return render_template('first.html',d=data)
    except Exception as e:
        print("Error:",e)
    

@app.route('/form')
def create():
    return render_template('second.html')
 
@app.route('/store', methods=['POST'])
def store(): 
    t=request.form['bookname']
    det=request.form['author']
    dt=request.form['recievingdate']
    yt=request.form['returndate']
    st=request.form['studentname']
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todolist")
        cu=db.cursor()
        sql="insert into labrr(bookname,author,recievingdate,returndate,studentname)values('{}','{}','{}','{}','{}')".format(t,det,dt,yt,st)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    
    except Exception as e:
        print("Error:", e)
        
@app.route('/delete/<rid>')
def delete(rid):
    #return "ID is:"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todolist")
        cu=db.cursor()
        sql="delete from labrr where id={}".format(rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print("Error:",e)
        
        
        
        
@app.route('/edit/<rid>')
def edit(rid):
    #return "ID is:"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todolist")
        cu=db.cursor()
        sql="select * from labrr where id= '{}'".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('third.html',d=data)
        
    except Exception as e:
        print("Error:",e)
 
@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    #return "ID to be  update in db is:"+rid
    t=request.form['bookname']
    det=request.form['author']
    dt=request.form['recievingdate']
    yt=request.form['returndate']
    st=request.form['studentname']
    
    #return t+det+dt
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todolist")
        cu=db.cursor()
        sql="update labrr SET bookname='{}',author='{}',recievingdate='{}',returndate='{}',studentname='{}' where id='{}'".format(t,det,dt,yt,st,rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception as e:
        print("Error:",e)
        
 
#accesing class method run-to start a server
app.run(debug=True) 
 
