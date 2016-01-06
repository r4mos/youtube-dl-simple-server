#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import re
import subprocess
import urllib2
import threading
from Paths import Paths
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn

class HttpServerThread(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

class HttpServerHandler(BaseHTTPRequestHandler):
    def do_GET (self):
        self.send_response(200)
        if (re.match('/http(.+)', self.path)):
            url = re.findall(r'/(.+)', self.path)[0]

            try:
                outputYoutubeDl = subprocess.check_output([Paths().getYdlLocation(), '-g', '--get-filename', '--no-playlist', '-f', 'best', '--no-check-certificate', url])
                getVars = outputYoutubeDl.split('\n')

                if len(getVars) > 3: #'URL','Name',''
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write('<h2>Unsupported url</h2>')
                    self.wfile.write('<p>Unexpected response from youtube-dl</p>')

                else:
                    trueUrl = getVars[0]
                    nameExt = getVars[1]

                    req = urllib2.urlopen(trueUrl, context=Paths().getSslCtx())
                    reqType = req.info().getheader('Content-Type')
                    reqLength = req.info().getheader('Content-Length')

                    self.send_header('Content-type', reqType)
                    self.send_header('Content-Length', reqLength)
                    self.send_header('Content-Disposition', 'attachment; filename="' + nameExt + '"')
                    self.end_headers()

                    while True:
                        chunk = req.read(524288) #512*1024
                        if not chunk:
                            break
                        self.wfile.write(chunk)

            except:
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('<h2>Unsupported url</h2>')
                self.wfile.write('<p>youtube-dl can\'t find video URL</p>')

        else:
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            output  = 'Download videos from some video platforms via http requests using youtube-dl<br /><br />'
            output += 'USAGE:<br />'
            output += 'http://localhost:49149/URL VIDEO<br /><br />'
            output += 'LINKS:<br />'
            output += '<a href="https://github.com/rg3/youtube-dl">youtube-dl</a><br />'
            output += '<a href="https://github.com/r4mos/youtube-dl-simple-server">youtube-dl-simple-server</a>'
            self.wfile.write(output)

        return
