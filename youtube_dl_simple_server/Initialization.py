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
        self.show('Initializing')

        self.show('Checking for youtube-dl')
        if (not os.path.exists('/usr/local/bin/youtube-dl')):
            self.show('You need youtube-dl to catch links')
            self.downloadYdl()

        self.show('youtube-dl --version\n' + subprocess.check_output(["youtube-dl", "--version"]))

        if (os.geteuid() == 0):
            self.show('For safety, you can\'t start the server as root')
        else:
            self.show('Running HTTP server')
            httpd = ThreadedHTTPServer(('localhost', 49149), HttpServerHandler)
            httpd.serve_forever()
    
    def downloadYdl (self):
        if (os.geteuid() != 0):
            self.show('You need root permss for auto-install. Try this:')
            self.show('sudo !!')
            sys.exit(1)
        else:
            self.show('Downloading youtube-dl')
            try:
                latest = urllib2.urlopen("https://yt-dl.org/latest/youtube-dl")
            except:
                self.show('No Internet connexion')
                sys.exit(1)
            output = open('/usr/local/bin/youtube-dl','wb')
            output.write(latest.read())
            output.close()

            self.show('Changing permissions to youtube-dl')
            subprocess.check_output(["chmod", "a+x", "/usr/local/bin/youtube-dl"])

            self.show('\nRestart youtube-dl-simple-server')
            sys.exit(0)


    def show (self, s):
        if (self._verbose):
            print s