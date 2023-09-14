import emailer as e
import os
from dotenv import load_dotenv
import getsysinfo as gi

load_dotenv()
WINFORMATION = os.getenv('WINFORMATION')

if __name__ == "__main__":
    gi.get_sysinfo()
    e.email.set_content(e.cast_file_to_message(WINFORMATION))
    e.send_mail()