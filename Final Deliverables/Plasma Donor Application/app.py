from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session,flash
from markupsafe import escape
import sendgrid
import os
import sys
import ibm_db
from flask_mail import Mail, Message
from emailSender import *
from flask import Response

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=qdz26030;PWD=hC55ak4dG6UPcHuX;","","")
app = Flask(__name__)

sql = "SELECT * FROM mailer"
stmt = ibm_db.prepare(conn, sql)
ibm_db.execute(stmt)
key = ibm_db.fetch_assoc(stmt)


#Email
app.config['SECRET_KEY'] = 'top-secret!'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = str(key['KEY'])
app.config['MAIL_DEFAULT_SENDER'] = 'PlasmaDonorZr@outlook.com'
mail = Mail(app)



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
@app.route('/process')
def process():
  return render_template('process.html')

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
      flash("You are already a member, please login using your details")
      return render_template('requester.html')
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

    flash("Your Data saved successfuly.")
    return render_template('register.html')

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
      flash("Login unsuccessful. Incorrect username / password !")
      return render_template('login.html') 



@app.route('/donor',methods = ['POST', 'GET'])
def donor():
  if request.method == 'POST':

    name = request.form['name']
    email = request.form['email']
    phnum = request.form['phnum']
    phnum2=request.form['phnum2']
    blood=request.form['bloodgrp']
    states=request.form['state']
    district=request.form['district']
    address=request.form['address']
    

    sql = "SELECT * FROM donor WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      flash("You are already a member as donor!!")
      return render_template('donor.html')
    else:
      insert_sql = "INSERT INTO donor VALUES (?,?,?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, phnum)
      ibm_db.bind_param(prep_stmt, 4, phnum2)
      ibm_db.bind_param(prep_stmt, 5, blood)
      ibm_db.bind_param(prep_stmt, 6, states)
      ibm_db.bind_param(prep_stmt, 7, district)
      ibm_db.bind_param(prep_stmt, 8, address)
      ibm_db.execute(prep_stmt)
    
    flash("Successfuly registered as donor.")
    return render_template('donor.html')



@app.route('/requested',methods = ['POST', 'GET'])
def requested():
  if request.method == 'POST':
    
    name = request.form['name']
    lname=request.form['lname']
    email = request.form['email']
    phnumr = request.form['phnumr']
    phnumr2=request.form['phnumr2']
    address=request.form['address']
    bloodgrp=request.form['blood']
    sql = "SELECT * FROM requester WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    
   
    insert_sql = "INSERT INTO requester VALUES (?,?,?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, name)
    ibm_db.bind_param(prep_stmt, 2, lname)
    ibm_db.bind_param(prep_stmt, 3, email)
    ibm_db.bind_param(prep_stmt, 4, phnumr)
    ibm_db.bind_param(prep_stmt, 5, phnumr2)
    ibm_db.bind_param(prep_stmt, 6, address)
    ibm_db.bind_param(prep_stmt, 7, bloodgrp)
    ibm_db.execute(prep_stmt)
    bloodgrp = request.form['blood']
    state = request.form['state']
    district = request.form['district']
    ph = request.form['phnumr']
   
    reqDetails = dict()
    reqDetails['Name'] = name + " " + lname
    reqDetails['Email'] = email
    reqDetails['State'] =  state
    reqDetails['City'] =  district
    reqDetails['bloodgrp'] = bloodgrp
    reqDetails['phone'] = ph

    sql = "SELECT * FROM donor WHERE blood=? and states=? and district=?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,bloodgrp)
    ibm_db.bind_param(stmt,2,state)
    ibm_db.bind_param(stmt,3,district)
    ibm_db.execute(stmt)
    data = ibm_db.fetch_assoc(stmt)
    donorFoundFlag = False
    donorList = []
    if data!= False:
      while data != False:
        donorList.append(data)
        data = ibm_db.fetch_assoc(stmt)
      
      sendEmail(email, successMail(reqDetails,donorList))  #Send an Email to Requestor
      for i in donorList:
        mailTemplate = sendEmailToDoanar(i['NAME'],  reqDetails)
        sendEmail(i['EMAIL'], mailTemplate) #Send an Email to Donor
          
     
    else:
      #When no donor found 
      pass
  return ('', 204)

 
    


if __name__ == '__main__':
  app.run(debug=True)

def sendEmail(email, data):
  recipient = email
  msg = Message('Plasma Donar', recipients=[recipient])
  msg.body = ('')
  msg.html = data
  mail.send(msg)
