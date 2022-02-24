# Email Varification Using OTP in Flask

from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from random import randint

app = Flask(__name__)
mail = Mail(app)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'barlapudiraghunadh9@gmail.com'  # give your mail_id
app.config['MAIL_PASSWORD'] = 'Raghu_123'  # you have to give your password of gmail account
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
otp = randint(000000, 999999)


@app.route('/')
def index():
    return ''


@app.route('/verify', methods=["POST"])
def verify():
    email = request.json['email']
    msg = Message(subject='OTP', sender='naveen.netha0213@gmail.com', recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    return ''


@app.route('/validate', methods=['POST'])
def validate():
    user_otp = request.json['otp']
    if otp == int(user_otp):
        return "Email varification succesfull3>"
    return "<h3>Please Try Again</h3>"


if __name__ == '__main__':
    app.run(debug=True)
