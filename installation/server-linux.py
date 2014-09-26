#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
import sys
import urllib2
import subprocess

installationPath = os.path.expanduser('~') + '/.config/ydlss'
serverLocalLocation = installationPath + '/youtube-dl-simple-server'
serverWebLocation = 'https://github.com/r4mos/youtube-dl-simple-server/raw/master/bin/server/linux/youtube-dl-simple-server'

try:
    print 'Cheeking installation folder'
    if not os.path.isdir(installationPath):
        os.makedirs(installationPath)

    print 'Downloading server'
    latest = urllib2.urlopen(serverWebLocation)
    output = open(serverLocalLocation, 'wb')
    output.write(latest.read())
    output.close()

    print 'Changing permissions'
    subprocess.check_output(['chmod', 'a+x', serverLocalLocation])

    print 'Adding to .profile file to autostart'
    profile = open (os.path.expanduser('~') + '/.profile', 'a')
    profile.write(serverLocalLocation + ' &\n')
    profile.close()

    print 'Starting server'
    print serverLocalLocation + ' --verbose'
    subprocess.Popen(serverLocalLocation + ' --verbose')
    
    print '\nDone.'
except:
    print 'Fail. An error occurred'
    sys.exit(1)