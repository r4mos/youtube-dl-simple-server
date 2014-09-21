#!/usr/bin/env python
#-*- encoding:utf-8 -*-

__author__  = 'Carlos Ramos'
__license__ = 'The MIT License'
__version__ = '0.1'

import sys
import argparse
from Initialization import Initialization

def main():
    parser = argparse.ArgumentParser(description='Download videos from some video platforms via http requests using youtube-dl')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('--verbose', action='store_true', help='show what the program is doing')
    args = parser.parse_args()

    try:
        Initialization(args.verbose)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
	main()