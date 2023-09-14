import subprocess
from dotenv import load_dotenv
import logging
import os

logging.basicConfig(filename='winfo.log', filemode='w', level=logging.DEBUG)

load_dotenv()
WINFO = os.getenv('WINFORMATION')
logging.debug(f'WINFO = {WINFO}')

raw_info = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
info_dump = []

def get_sysinfo():
    """Get system information and write it to a file
    """
    for item in raw_info:
        info_dump.append(str(item.split('\r')[:-1]))
    for entry in info_dump:
        logging.debug('Sanitizing entry...')
        entry = clean_entry(entry)
        write_outfile(entry)
    
def clean_entry(entry):
    """Sanitize each line of the output before writing
    """
    cleaned_entry = (str(entry).strip('[\']')).strip() # Remove leading and trailing whitespaces and Python-related [] and '
    cleaned_entry = " ".join(cleaned_entry.split()) # Remove consecutive whitespace characters (to make output smaller onscreen)
    return cleaned_entry # Returns one individual entry, *NOT* the entire outfile; there might be a better way to do this

def write_outfile(line):
    """Write each line of the system info to an output file
    """
    # TODO: Send this outfile to the root dir
    # TODO: Or, maybe make it write to a tmp file here then format it later?
    logging.debug('Writing outfile...')
    with open(WINFO, 'a') as output:
        output.write(line)
        output.write('\r')
    logging.debug('Done.')

if __name__=="__main__":
    get_sysinfo()
    