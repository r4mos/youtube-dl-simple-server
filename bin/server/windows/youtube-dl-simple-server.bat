@ECHO off
ping 1.1.1.1 -w 5000 > nul
START /B youtube-dl-simple-server.exe --verbose
exit