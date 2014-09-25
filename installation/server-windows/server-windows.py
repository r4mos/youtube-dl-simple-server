# -*- coding: cp1252 -*-

import os
import sys
import urllib2
import subprocess

installationPath = os.environ['APPDATA'] + '\ydlss'
serverLocalLocation = installationPath + '\youtube-dl-simple-server.exe'

serverWebLocation = 'https://github.com/r4mos/youtube-dl-simple-server/raw/master/bin/server/windows/'
serverWebFiles = {'__init__.exe', 'hstart.exe', 'youtube-dl-simple-server.exe', '_hashlib.pyd', '_socket.pyd', '_ssl.pyd', 'bz2.pyd', 'library.zip', 'python27.dll', 'select.pyd', 'unicodedata.pyd', 'w9xpopen.exe', 'youtube-dl-simple-server.bat'}

try:
    print 'Cheeking installation folder'
    if not os.path.isdir(installationPath):
        os.makedirs(installationPath)

    print 'Downloading server'
    for f in serverWebFiles:
        latest = urllib2.urlopen(serverWebLocation + f)
        output = open(installationPath + '\\' + f, 'wb')
        output.write(latest.read())
        output.close()
    
    print 'Adding to Init folder to autostart'
    #Windows on English
    if os.path.isdir(os.environ['USERPROFILE'] + '\Start Menu\Programs\StartUp'):
        path = os.environ['USERPROFILE'] + '\Start Menu\Programs\StartUp'
    elif os.path.isdir(os.environ['USERPROFILE'] + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'):
        path = os.environ['USERPROFILE'] + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    #Windows on Spanish
    elif os.path.isdir(os.environ['USERPROFILE'] + '\Menú Inicio\Programs\StartUp'):
        path = os.environ['USERPROFILE'] + '\Menú Inicio\Programs\StartUp'
    elif os.path.isdir(os.environ['USERPROFILE'] + '\Menú Inicio\Programas\Inicio'):
        path = os.environ['USERPROFILE'] + '\Menú Inicio\Programas\Inicio'
    else:
        path = ''

    if path != '':
        latest = urllib2.urlopen('https://github.com/r4mos/youtube-dl-simple-server/raw/master/bin/server/windows/run_youtube-dl-simple-server.lnk')
        lnk = open(path + '\\run_youtube-dl-simple-server.lnk', 'wb')
        lnk.write(latest.read())
        lnk.close()

        print '\nCompleted installation but server is stopped'
        print 'Reboot your computer or start the server manually:'
        print 'Execute ' + installationPath + '\youtube-dl-simple-server.exe'
    else:
        print 'Autostart fail'
        print '\nCompleted installation but server is stopped and it doesn\'t autostart on reboot'
        print 'Start the server manually:'
        print 'Execute ' + installationPath + '\youtube-dl-simple-server.exe'
except:
    print 'Fail. An error occurred'
    sys.exit(1)
