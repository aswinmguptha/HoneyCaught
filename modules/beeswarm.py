#!/usr/bin/python

import nmap
import sys
import time

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
    url = sys.argv[1]
    print url
    nmap_scan(url)

if __name__ == '__main__':
    start = time.time()
    main()
