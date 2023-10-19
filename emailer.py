import smtplib
import os
import logging
from dotenv import load_dotenv
from email.message import EmailMessage

logging.basicConfig(filename='winfo.log', filemode='a', level=logging.DEBUG)

load_dotenv()
USER = os.getenv('USERNAME')
logging.debug(f'USER = {USER}')
PASS = os.getenv('PASSWORD')
logging.debug(f'PASS successfully sourced from .env')
WINFO = os.getenv('WINFORMATION')
logging.debug(f'WINFO = {WINFO}')

email = EmailMessage()
email['from'] = 'WINFORMATION'
email['to'] = USER
email['subject'] = 'WINFO'

def cast_file_to_message(file):
   """Read WINFORMATION.txt and cast it as a string into the body of an email."""
   logging.debug('Casting file to message...')
   with open(file, 'r') as f:
        message = f.read()
        logging.debug('File cast to message.')
        return message

def send_mail():
    """Send email."""
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(USER, PASS)
        smtp.send_message(email)
        logging.debug('Message sent!')
        print('Message sent successfully!')


if __name__=="__main__":
    email.set_content(cast_file_to_message('WINFO'))
    send_mail()
