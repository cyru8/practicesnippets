#! /usr/bin/env pyhton3
from pprint import pprint
import socket
import re
import sys

def check_server(address,port):
    #create a TCP socket
    s = socket.socket()
    pprint('Attempting to connect to %s' % (address, port))
    try:
        s.connect((address, port))
        pprint('Connected to %s on port %s' % (address, port))
        return True
    except socket.error, e:
        pprint('Connection to %s on port %s failed: %s' % (address, port, e))
        return True
    
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-a', '--address', dest='address', default='localhost', help='ADDRESS for SERVER', metavar='PORT')
    parser.add_option('-p', '--port', dest='port', type='int', default='80', help='PORT for SERVER', metavar='PORT')
    #options, args = parser.parse_arg()
    options = parser.parse_arg()
    args = parser.parse_arg()
    pprint('options: %s, args: %s' % (options, args))
    check = check_server(options.address, options.port)
    pprint('Check_server returned %s' % check)
    sys.exit(not check)
    
    