#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os

class Paths():
    _ydlname = ''
    _ydlpath = ''

    def __init__(self):
        if (os.name == 'nt'):
            self._ydlname = 'youtube-dl.exe'
            self._ydlpath = ''
        else:
            self._ydlname = 'youtube-dl'
            self._ydlpath = os.path.expanduser('~') + '/.ydlss'

    def getYdlName(self):
        return self._ydlname

    def getYdlPath(self):
        return self._ydlpath

    def getYdlLocation(self):
        return self._ydlpath + '/' + self._ydlname