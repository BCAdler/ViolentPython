'''
Created on Sep 23, 2015

@author: Brandon Adler
'''

import optparse
import socket
from socket import *
    
# Takes 2 args and attempts to create connection to the target host(tgtHost)
# and on the target port(tggtPort)
def connScan(tgtHost, tgtPort):
    try: # Try block used because it throws exception if the port is closed
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n') # Sends information to port to see the response
        results = connSkt.recv(100)
        print('[+]%d/tcp open'% tgtPort)
        print('[+] ' + str(results))
        connSkt.close()
    except:
        print('[-]%d/tcp closed'% tgtPort)

# Will attempt to resolve IP to friendly hostname and will enumerate thorough
# each port and attempt to connect using the connScan function
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host"%tgtHost)
        return
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port ' + tgtPort)
        connScan(tgtHost, int(tgtPort))
        
def main():
    # Parses the target hostname and port to scan via command line options and user interaction
    parser = optparse.OptionParser('usage %prog |H' "<target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target port')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by a comma')
    (options, args) = parser.parse_args()
    print(parser.parse_args())
    tgtHost = options.tgtHost
    print(options.tgtPort)
    tgtPorts = str(options.tgtPort).split(", ")
    print(tgtPorts)
    if (tgtHost == None) | (tgtPorts[0] == None):
        print('[-] You must specify a target host and port[s]')
        exit(0)
    portScan(tgtHost, tgtPorts)
if __name__ == '__main__':
    main()