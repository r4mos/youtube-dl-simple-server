#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
import sys
import urllib2
import subprocess
import BaseHTTPServer
from HttpServer import HttpServerHandler, ThreadedHTTPServer

class Initialization ():
    def __init__(self, verbose):
        self._verbose = verbose

        self.show('\nChecking for youtube-dl')
        if (not os.path.exists('/usr/local/bin/youtube-dl')):
            self.show('You need youtube-dl to catch links')
            self.downloadYdlLatest()

        self.show('\nChecking youtube-dl version')
        version = subprocess.check_output(['youtube-dl', '--version']).replace('\n', '')
        latestVersion = self.getVersionYdlLatest()
        self.show(' - Latest youtube-dl ' + latestVersion)
        self.show(' - Yours  youtube-dl ' + version)
        if version != latestVersion:
            self.show(' You should update youtube-dl:')
            self.show(' sudo youtube-dl -U')

        if (os.geteuid() == 0):
            self.show('\nFor safety, you can\'t start the server as root. Run again')
        else:
            self.show('\nRunning HTTP server')
            httpd = ThreadedHTTPServer(('localhost', 49149), HttpServerHandler)
            httpd.serve_forever()
    
    def downloadYdlLatest (self):
        if (os.geteuid() != 0):
            self.show('You need root permss for auto-install. Try this:')
            self.show('sudo !!')
            sys.exit(1)
        else:
            self.show('Downloading youtube-dl')
            try:
                latest = urllib2.urlopen('https://yt-dl.org/latest/youtube-dl')
            except:
                self.show('No Internet connexion')
                sys.exit(1)
            output = open('/usr/local/bin/youtube-dl','wb')
            output.write(latest.read())
            output.close()

            self.show('Changing permissions to youtube-dl')
            subprocess.check_output(['chmod', 'a+x', '/usr/local/bin/youtube-dl'])

            self.show('\nRestart youtube-dl-simple-server')
            sys.exit(0)

    def getVersionYdlLatest (self):
        try:
            latestVersion = urllib2.urlopen('https://yt-dl.org/latest/version').read()
        except:
            self.show('No Internet connexion')
            sys.exit(1)
        return latestVersion

    def show (self, s):
        if (self._verbose):
            print s