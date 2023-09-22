import emailer as e
import os
from dotenv import load_dotenv
import getsysinfo


if __name__ == "__main__":
    load_dotenv()
    SYS_INFO = "SYS_INFO.txt"
    getsysinfo.get_sysinfo()
    e.email.set_content(e.cast_file_to_message(SYS_INFO))
    e.send_mail()
