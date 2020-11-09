#!/usr/bin/env python3
from pprint import pprint
import paramiko 

hostname = '192.168.1.72'
port = 22
username = 'oadetiba'
password = 'Password!23'

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    ifconfig_out = s.exec_command('ip address')
    #stdin, stdout, stderr = s.exec_command('ip address')
    pprint(ifconfig_out)
    s.close()
