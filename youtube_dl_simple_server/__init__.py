#!/usr/bin/env python
#-*- encoding:utf-8 -*-

__author__  = 'Carlos Ramos'
__license__ = 'The MIT License'
__version__ = '0.1'

import os
import sys
import urllib2
import subprocess
from argparse import ArgumentParser, RawTextHelpFormatter
from HttpServer import HttpServerHandler, ThreadedHTTPServer

def main():
    parser = ArgumentParser(description='Download videos from some video platforms via http requests using youtube-dl', formatter_class=RawTextHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('-u', '--update', action='store_true', help='update or install youtube-dl and exit (needs root)\n\n')
    parser.add_argument('-p', '--port', type=int, default=49149, help='select server listening port (49149 by default)')
    parser.add_argument('--verbose', action='store_true', help='show what the program is doing')
    args = parser.parse_args()

    try:
        if (args.update):
            update(args.verbose)
        else:
            checkYoutubedl(args.verbose)
            runServer(args.verbose, args.port)
    except KeyboardInterrupt:
        sys.exit(0)

def update(v):
    show('Updating\n', v)
    if (os.geteuid() != 0):
        print 'You need root permss for install. Try this:'
        print 'sudo !!'
        sys.exit(1)
    else:
        show('Downloading latest version', v)
        try:
            latest = urllib2.urlopen('https://yt-dl.org/latest/youtube-dl')
        except:
            show('\nNo Internet connexion', v)
            sys.exit(1)
        output = open('/usr/local/bin/youtube-dl','wb')
        output.write(latest.read())
        output.close()

        show('Changing permissions', v)
        subprocess.check_output(['chmod', 'a+x', '/usr/local/bin/youtube-dl'])

        print '\nUpdated successfully'
        sys.exit(0)

def checkYoutubedl(v):
    show('Cheecking youtube-dl\n', v)
    if (not os.path.exists('/usr/local/bin/youtube-dl')):
        print 'You need youtube-dl to catch links. Try this:'
        print 'sudo youtube-dl-simple-server -u'
        sys.exit(1)
    else:
        show('Cheecking youtube-dl version', v)
        version = subprocess.check_output(['youtube-dl', '--version']).replace('\n', '')
        try:
            latestVersion = urllib2.urlopen('https://yt-dl.org/latest/version').read()
            show(' - Latest ' + latestVersion, v)
            show(' - Yours  ' + version, v)
            if version != latestVersion:
                show(' You should update youtube-dl:', v)
                show(' sudo youtube-dl-simple-server -u', v)
        except:
            show('\nNo Internet connexion', v)
            sys.exit(1)

def runServer(v, port):
    show('\nRunning serer at http://localhost:' + str(port), v)
    httpd = ThreadedHTTPServer(('localhost', port), HttpServerHandler)
    httpd.serve_forever()

def show (s, v):
    if (v):
        print s

if __name__ == '__main__':
    main()
