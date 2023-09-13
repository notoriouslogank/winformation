import emailer
import getsysinfo
import sys
#import logging

#logging.basicConfig()
def main():
    getsysinfo()
    emailer()
    sys.exit()
main()