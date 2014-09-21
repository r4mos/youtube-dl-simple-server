youtube-dl-simple-server - download videos from some video platforms via http requests using youtube-dl

# USAGE
**youtube-dl-simple-server** [OPTIONS]

# REQUIEREMENTS
  Linux platform (for now)
  python 2.7. I haven't tested on other versions (for now)

# DESCRIPTION
It is a HTTP server that responds GET requests like:
http://localhost:49149/<URL VIDEO>

If video's URL works with youtube-dl, displays a button for starting download. If not, is notified with a message like "Download not available".

This server is designed to work with one browser plugin for users.

# OPTIONS
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  --verbose      show what the program is doing


# LINKS
[youtube-dl](https://github.com/rg3/youtube-dl)
[youtube-dl-simple-server](https://github.com/r4mos/youtube-dl-simple-server)

# LICENSE
The MIT License

Copyright (c) 2014 Carlos Ramos Mellado.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.