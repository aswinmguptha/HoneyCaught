#!/usr/bin/python

import os
import sys
import time
import argparse

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
        print '[+] Host is up'
        print '\n'
        if args.module == None:
            print 'Which module do you wish to scan?'
            print '\t[1] beeswarm'
            module = raw_input()
        else:
            module = args.module
        if module == '1':
            os.system('python modules/beeswarm.py {}'.format(args.host))
        else:
            print 'No such modules found'

def main():
    is_up(args.host)

if __name__ == '__main__':
    banner()
    start = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--host', help='url/host to scan.')
    parser.add_argument('-p', '--port', help='Port where HoneyPot service is running. If no port is given, default port [80] will be used.', type=int, default=80)
    parser.add_argument('-m', '--module', help='Module to run against the target (use the module\'s serial number). To see the  available modules, use \'-l\' option.')
    parser.add_argument('-l', '--list-modules', help='List available modules.')
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    main()
