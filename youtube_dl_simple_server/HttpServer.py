#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import cgi
import re
import subprocess
import urllib2
import os.path
import threading
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

class HttpServerHandler (BaseHTTPRequestHandler):
    def do_GET (self):
        self.send_response(200)
        self.end_headers()

        if (re.match('/http(.+)', self.path)):
            url = re.findall(r'/(.+)', self.path)[0]

            try:
                outputYoutubeDl = subprocess.check_output(["youtube-dl", "-g", "--get-filename", "-e", "--no-playlist", url])

                getVars = outputYoutubeDl.split("\n")
                nameOut = getVars[0]
                trueUrl = getVars[1]
                nameExt = getVars[2]

                output  = '<html>'
                output += '  <form action="/' + nameExt + '" method="post">'
                output += '    <input type="hidden" name="vid" value="' + trueUrl + '">'
                output += '    <input type="submit" value="Download video">'
                output += '  </form>'
                output += '</html>'
                self.wfile.write(output)
            except:
                self.wfile.write("Unsupported url")
        
        else:
            output  = "Download videos from some video platforms via http requests using youtube-dl\n\n"
            output += "USAGE:\n"
            output += "http://localhost:49149/url=<URL VIDEO>\n\n"
            output += "LINKS:\n"
            output += "[youtube-dl](https://github.com/rg3/youtube-dl)\n"
            output += "[youtube-dl-simple-server](https://github.com/r4mos/youtube-dl-simple-server)\n\n"
            output += "LICENSE:\n"
            output += open('LICENSE','rb').read()
            self.wfile.write(output)

        return

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        try:
            req = urllib2.urlopen(postvars['vid'][0])
            while True:
                chunk = req.read(524288) #512*1024
                if not chunk:
                    break
                self.wfile.write(chunk)

        except:
            self.wfile.write("Download not available")

        return