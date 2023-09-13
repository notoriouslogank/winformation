## Module to send the emails, once created

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'WINFORMATION'
email['to'] = 'logankdevemail+winfo@gmail.com'
email['subject'] = 'WINFO'

email.set_content('Hello')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('logankdevemail@gmail.com', 'upbx opzt fcer ctdz')
    smtp.send_message(email)
    print('Check your email.')