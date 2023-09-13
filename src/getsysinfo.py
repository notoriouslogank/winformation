import subprocess

raw_info = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
info_dump = []

def write_outfile(line):
    # TODO: Send this outfile to the root dir
    # TODO: Or, maybe make it write to a tmp file here then format it later?
    with open('../WINFORMATION.txt', 'a') as output:
        output.write(line)
        output.write('\n')

def get_sysinfo():
    for item in raw_info:
        info_dump.append(str(item.split('\r')[:-1]))
    for entry in info_dump:
        write_outfile(entry)

get_sysinfo()