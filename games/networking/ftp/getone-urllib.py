#!/usr/local/bin/python
"""
A Python script to download a file by FTP by its URL string; use higher-level
urllib instead of ftplib to fetch file;  urllib supports FTP, HTTP, client-side
HTTPS, and local files, and handles proxies, redirects, cookies, and more;
urllib also allows downloads of html pages, images, text, etc.;  see also
Python html/xml parsers for web pages fetched by urllib in Chapter 19;
"""


import os, getpass
from urllib.request import urlopen
filename = '50MB.zip'
password = getpass.getpass('anonymous')

remoteaddr = 'ftp://speedtest.tele2.net/%s' % filename
print('Downloading', remoteaddr)

remotefile = urlopen(remoteaddr)
localfile = open(filename, 'wb')
localfile.write(remotefile.read())
localfile.close()
remotefile.close()
