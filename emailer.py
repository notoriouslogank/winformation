import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()
USER = os.getenv('USERNAME')
PASS = os.getenv('PASSWORD')
WINFORMATION = os.getenv('WINFORMATION')

email = EmailMessage()
email['from'] = 'WINFORMATION'
email['to'] = USER
email['subject'] = 'WINFO'

def cast_file_to_message(file):
   """Read WINFORMATION.txt and cast it as a string into the body of an email."""
   with open(file, 'r') as f:
        message = f.read()
        return message

def send_mail():
    """Send email."""
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(USER, PASS)
        smtp.send_message(email)
        print('Sent successfully!')

if __name__=="__main__":
    email.set_content(cast_file_to_message(WINFORMATION))
    send_mail()