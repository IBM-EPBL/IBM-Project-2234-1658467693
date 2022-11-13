from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import sendgrid
import os
import sys
import ibm_db
from flask_mail import Mail, Message
from emailSender import successMail
from flask import Response

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=qdz26030;PWD=hC55ak4dG6UPcHuX;","","")
app = Flask(__name__)




@app.route('/')
def home():
  return render_template('home.html')
@app.route('/log')
def log():
  return render_template('login.html')
@app.route('/signup')
def signup():
  return render_template('register.html')
@app.route('/contact')
def contact():
  return render_template('contact.html')
@app.route('/donorpage')
def donorpage():
  return render_template('donor.html')
@app.route('/eligi')
def eligi():
  return render_template('eligibility.html')
@app.route('/req')
def req():
  return render_template('requester.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    phnum = request.form['phnum']
    phnum2=request.form['phnum2']
    pas = request.form['pas']
    pas2=request.form['pas2']
    gen=request.form['gen']

    sql = "SELECT * FROM user WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('home.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO user VALUES (?,?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, phnum)
      ibm_db.bind_param(prep_stmt, 4, phnum2)
      ibm_db.bind_param(prep_stmt, 5, pas)
      ibm_db.bind_param(prep_stmt, 6, pas2)
      ibm_db.bind_param(prep_stmt, 7, gen)
      ibm_db.execute(prep_stmt)
    
    return render_template('home.html', msg="Student Data saved successfuly.")

@app.route('/loginpage',methods=['POST'])

def loginpage():
    user = request.form['user']
    passw = request.form['passw']
    sql = "SELECT * FROM user WHERE email =? AND pas=?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,user)
    ibm_db.bind_param(stmt,2,passw)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    if account:
            return render_template('home.html')
    else:
        return render_template('login.html', pred="Login unsuccessful. Incorrect username / password !") 



