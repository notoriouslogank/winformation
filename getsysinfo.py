import subprocess
from dotenv import load_dotenv
import logging
import os
import sys
import platform
import fileinput

PLATFORM = sys.platform
WINFO = 'SYS_INFO.txt'
load_dotenv()

logging.basicConfig(filename='winfo.log', filemode='w', level=logging.DEBUG)
logging.debug(f'WINFO = {WINFO}')

def isPlatformSupported():
    logging.info(f'Platform: {PLATFORM}')
    if PLATFORM == 'linux':
        getLinuxInfo()
    elif PLATFORM == 'win32':
        getWinInfo()
    else:
        print(f'Platform {PLATFORM} not supported.')
        logging.critical(f'Unsupported platform: {PLATFORM}')
        sys.exit(1)

def getCPU():
    with open('/proc/cpuinfo', 'r') as c:
        info = c.readlines()
        cpuinfo = [x.strip().split(':')[1] for x in info if 'model name' in x]
        for index, item in  enumerate(cpuinfo):
            cpu = ('' + str(index) + ': ' + item)
            return cpu
        
def getMem():
    with open('/proc/meminfo', 'r') as f:
        lines = f.readlines()
        used = (" " + lines[0].strip())
        avail = (" " + lines[1].strip())
        return used, avail

def getDist():
    with open('/proc/version', 'r') as f:
        lines = f.readlines()
        dist = str(lines).split('(')[0]
        cleanEntry(dist)
        return dist

def getGPU():
    """Get GPU info, write output of command to a tmp file, read each line as output, delete the tmp file
    """
    cmd = "lspci -v -s $(lspci | grep ' VGA ' | cut -d ' ' -f 1)"
    standard_output = str(subprocess.getoutput(cmd))
    output = []
    output.append(standard_output.split('\n\t'))
        
def getLinuxInfo():
    """Get Linux system information and write it to a file
    """
    commands = [
                (f'System: {platform.system()}'),
                (getDist()),
                (f'Architecture: {platform.architecture()[0]}'),
                (f'Machine: {platform.machine()}'),
                (f'Node: {platform.node()}'),
                (f'CPU: {getCPU()}'),
                (f'GPU: {getGPU()}'),
                (getMem()[0]),
                (getMem()[1])
                ]
    info_dump = []
    for command in commands:
        info_dump.append(str(command).split('\r'))
    for entry in info_dump:
        logging.debug('Sanitizing entry...')
        entry = cleanEntry(entry)
        writeOutfile(entry)

def getWinInfo():
    """Get Windows system information and write it to a file
    """
    raw_info = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    info_dump = []
    for item in raw_info:
        info_dump.append(str(item.split('\r')[:-1]))
    for entry in info_dump:
        logging.debug('Sanitizing entry...')
        entry = cleanEntry(entry)
        writeOutfile(entry)
    
def cleanEntry(entry):
    """Sanitize each line of the output before writing
    """
    cleaned_entry = (str(entry).strip('[\'\"]')).strip() # Remove leading and trailing whitespaces and Python-related [] and '
    cleaned_entry = " ".join(cleaned_entry.split()) # Remove consecutive whitespace characters (to make output smaller onscreen)
    return cleaned_entry # Returns one individual entry, *NOT* the entire outfile; there might be a better way to do this

def writeOutfile(line):
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
    isPlatformSupported()