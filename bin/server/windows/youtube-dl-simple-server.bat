@ECHO off
ping 1.1.1.1 -w 5000 > nul
START /B __main__.exe --verbose
exit