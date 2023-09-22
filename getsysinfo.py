import subprocess
from dotenv import load_dotenv
import logging
import sys
import platform

PLATFORM = sys.platform
WINFO = 'SYS_INFO.txt'

try:
    load_dotenv('.env')
except FileNotFoundError:
    logging.error('.env file not found!')
    
logging.basicConfig(filename='winfo.log', filemode='w', level=logging.DEBUG)
logging.debug(f'WINFO = {WINFO}')

def isPlatformSupported():
    """Verify current platform is supported.
    
    Returns:
        None
    """
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
    """Get processor information (Linux only) and return cpu

    Returns:
        str: Processor information
    """
    with open('/proc/cpuinfo', 'r') as c:
        info = c.readlines()
        cpuinfo = [x.strip().split(':')[1] for x in info if 'model name' in x]
        for index, item in  enumerate(cpuinfo):
            cpu = ('' + str(index) + ': ' + item)
            logging.info('Got CPU info.')
            return cpu
        
def getMem():
    """Get RAM information (Linux only) and return used; avail
    
    Returns:
        str: Used memory; available memory
    """
    with open('/proc/meminfo', 'r') as f:
        lines = f.readlines()
        used = (" " + lines[0].strip())
        avail = (" " + lines[1].strip())
        logging.info('Got RAM info.')
        return used, avail

def getDist():
    """Get distribution information (Linux only) and return dist

    Returns:
        str: Linux distribution information
    """
    with open('/proc/version', 'r') as f:
        lines = f.readlines()
        dist = str(lines).split('(')[0]
        cleanEntry(dist)
        logging.info('Got dist info.')
        return dist

def getGPU():
    """Get GPU information and return a list 
    """
    cmd = "lspci -v -s $(lspci | grep ' VGA ' | cut -d ' ' -f 1)"
    standard_output = str(subprocess.getoutput(cmd))
    output = []
    output.append(standard_output.split('\n\t'))
    logging.info('Got GPU info.')
        
def getLinuxInfo():
    """Aggregate Linux system info into a list and send to writeOutFile()
    """
    commands = [
                (f'System: {platform.system()}'),
                (getDist()),
                (f'Architecture: {platform.architecture()[0]}'),
                (f'Machine: {platform.machine()}'),
                (f'Node: {platform.node()}'),
                (f'CPU: {getCPU()}'),
                (f'GPU: {getGPU()}'),
                (getMem()[0]), # Used  memory
                (getMem()[1])  # Available memory
                ]
    info_dump = []
    logging.info('Running commands...')
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
        entry = cleanEntry(entry)
        writeOutfile(entry)
    
def cleanEntry(entry):
    """Sanitize each line of the output before writing
    """
    cleaned_entry = (str(entry).strip('[\'\"]')).strip() # Remove leading and trailing whitespaces and Python-related [] and '
    cleaned_entry = " ".join(cleaned_entry.split()) # Remove consecutive whitespace characters (to make output smaller onscreen)
    logging.info('Sanitizing entry...')
    return cleaned_entry # Returns one individual entry, *NOT* the entire outfile; there might be a better way to do this

def writeOutfile(line):
    """Write the system information output file to WINFO.
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