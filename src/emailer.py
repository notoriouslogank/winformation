import smtplib
from email.message import EmailMessage

WINFORMATION = 'WINFORMATION.txt'
email = EmailMessage()
email['from'] = 'WINFORMATION'
email['to'] = 'logankdevemail+winfo@gmail.com'
email['subject'] = 'WINFO'

def cast_file_to_message(file):
    with open(file, 'r') as f:
        message = f.read()
        return message

def send_mail():
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('logankdevemail@gmail.com', 'upbx opzt fcer ctdz')
        smtp.send_message(email)
        print('Check your email.')

email.set_content(cast_file_to_message(WINFORMATION))
send_mail()