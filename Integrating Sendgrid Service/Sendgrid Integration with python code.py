#Email
app.config['SECRET_KEY'] = 'top-secret!'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = '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'
app.config['MAIL_DEFAULT_SENDER'] = 'ZrPlasmaDonor@outlook.com'
mail = Mail(app)

if __name__ == '__main__':
  app.run(debug=True)

def sendEmail(email, data):
  recipient = email
  msg = Message('Plasma Donar', recipients=[recipient])
  msg.body = ('')
  msg.html = data
  #mail.send(msg)
