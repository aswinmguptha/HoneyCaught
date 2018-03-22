#!/usr/bin/python

import nmap
import os
import sys
import time

def banner():
    print '''
  _   _                         ____                  _     _   
 | | | | ___  _ __   ___ _   _ / ___|__ _ _   _  __ _| |__ | |_ 
 | |_| |/ _ \| '_ \ / _ \ | | | |   / _` | | | |/ _` | '_ \| __|
 |  _  | (_) | | | |  __/ |_| | |___ (_| | |_| | (_| | | | | |_ 
 |_| |_|\___/|_| |_|\___|\__, |\____\__,_|\__,_|\__, |_| |_|\__|
                         |___/                  |___/           	

	author: Aswin M Guptha (aswinmguptha)
'''

def is_up(url):
    print '[+] Scanning host'
    host_state  = True if os.system("ping -c 1 -w2 " + url + " > /dev/null 2>&1") is 0 else False
    if not host_state:
        print '\n'
        print '[-] Host is down'
        time.sleep(1)
        print '[-] Aborting scan'
        time.sleep(2)
        sys.exit()
    else:
        print '\n'
        print '[+] Host is up'
        nmap_scan(url)

def nmap_scan(url):
    nm = nmap.PortScanner()
    print '\n'
    print '[+] Scanning ' + str(url) + ' for HoneyPot'
    time.sleep(1)
    print '[+] Scanning port 5000 for scanning beeswarm'
    scan = nm.scan(hosts=url, arguments='-p 5000')
    ip = scan['scan'].keys()[0]
    if scan['scan'][ip]['tcp'][5000]['state'] == 'open':
        end = time.time()
        difference = end - start
        print '\n'
        print '[*] Scanning finished'
        print 'Time taken for scanning: %s seconds'.format(str(round(difference, 3)))
        print '\n'
        print 'The system is possibily running on a HoneyPot besswarm system'
    else:
        end = time.time()
        difference = end - start
        print '\n\n'
        print '[*] Scanning finished'
        print 'Time taken for scanning: {} seconds'.format(str(round(difference, 3)))
        print '\n'
        print 'No Honeypot systems detected'

def main():
    banner()
    url = raw_input('Enter the url that you wish to scan: ')
    is_up(url)

if __name__ == '__main__':
    start = time.time()
    main()
