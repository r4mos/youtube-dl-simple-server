youtube-dl-simple-server - download videos from some video platforms via http requests using youtube-dl

# USAGE
**youtube-dl-simple-server** [-h] [-v] [-u] [-s SERVER] [-p PORT] [--verbose]

# DESCRIPTION
It is a HTTP server that responds GET requests like:
http://localhost:49149/URL VIDEO

And start downloading.

# OPTIONS
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -u, --update          update or install youtube-dl and exit
    -s SERVER, --server SERVER
                        select server (localhost by default)
    -p PORT, --port PORT  select server listening port (49149 by default)
    --verbose             show what the program is doing

# INSTALLATION
For function only need install the server for your platform, but browser plugin makes it easier download videos

## LINUX SERVER
Download the installer, give execute permissions, run it and finally you can delete it:

    wget https://raw.githubusercontent.com/r4mos/youtube-dl-simple-server/master/installation/server-linux.py
    chmod +x server-linux.py
    ./server-linux.py
    rm server-linux.py

When you restart, it works. You can also start it manually:

    ~/.config/ydlss/youtube-dl-simple-server

To uninstall, delete the following folder:

    ~/.config/ydlss/


## WINDOWS SERVER
Download the [installer](https://github.com/r4mos/youtube-dl-simple-server/raw/master/installation/server-windows/installer.zip), unzip and execute server-windows.exe

If you haven't Windows on English or Spanish, it is possible that the server does not autostart

To start it manually run:

	%APPDATA%\ydlss\youtube-dl-simple-server.exe

To autostart, make a shortcut in "StartUp" (in your start menu) with the following path:

	%APPDATA%\ydlss\hstart.exe /NOCONSOLE "%APPDATA%\ydlss\youtube-dl-simple-server.bat"

To uninstall, delete the following folder:

    %APPDATA%\ydlss\

If you don't know where is %APPDATA%, visit this [link](https://www.youtube.com/watch?v=iUqsvpWn9bY)

## CHROME-CHROMIUM PLUGIN
Go to [webstore](https://chrome.google.com/webstore/detail/youtube-dl-simple-server/kpfoekjfnlmomdeipjojapkhhpbgmmoc/) and install

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
