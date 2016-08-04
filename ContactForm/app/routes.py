from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
 
mail = Mail()
 
app = Flask(__name__)
 
app.secret_key = 'secretpanda7781'
 
app.config["MAIL_SERVER"] = "send.one.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@kristenhuber.com'
app.config["MAIL_PASSWORD"] = 'whiteRabbit7781'
 
mail.init_app(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    msg = Message(form.subject.data, sender='contact@kristenhuber.com', recipients=['kristen.huber.19@gmail.com'])
    msg.body = """
    From: %s &lt;%s&gt;
    %s
    """ % (form.name.data, form.email.data, form.message.data)
    mail.send(msg)
    return render_template('contact.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

if __name__=='__main__':
  app.run(debug=True)
