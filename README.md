youtube-dl-simple-server - download videos from some video platforms via http requests using youtube-dl

# USAGE
**youtube-dl-simple-server** [-h] [-v] [-u] [-p PORT] [--verbose]

# DESCRIPTION
It is a HTTP server that responds GET requests like:
http://localhost:49149/URL VIDEO

And start downloading.

# OPTIONS
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -u, --update          update or install youtube-dl and exit
    -p PORT, --port PORT  select server listening port (49149 by default)
    --verbose             show what the program is doing

# INSTALLATION
To function only need to install the server for your platform, but browser plugin makes it easier download videos

## LINUX SERVER
Download the installer, give execute permissions, run it and finally you can delete it:

    wget https://raw.githubusercontent.com/r4mos/youtube-dl-simple-server/master/installation/server-linux.py
    chmod +x server-linux.py
    ./server-linux.py
    rm server-linux.py

When you restart, it works

## WINDOWS SERVER
It's coming soon

## CHROME-CHROMIUM PLUGIN
First [download crx file](https://github.com/r4mos/youtube-dl-simple-server/raw/master/bin/plugin/chrome-chromium/chrome-chromium.crx).

Second, open chrome or chromiun with --enable-easy-off-store-extension-install flag. For example, in Chromium:

    chromium-browser --enable-easy-off-store-extension-install

If you use Windows, you should add flag in the shortcut

Then, open the extensions page (chrome://extensions) and drag and drop crx file

Finally, accept installation

# COMPILE
Linux: make

Windows: python setup.py py2exe (needs [py2exe](http://www.py2exe.org/))

# LINKS
[youtube-dl](https://github.com/rg3/youtube-dl)

[youtube-dl-simple-server](https://github.com/r4mos/youtube-dl-simple-server)

# LICENSE
The MIT License

Copyright (c) 2014 Carlos Ramos Mellado.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.