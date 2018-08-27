#!/bin/env python


import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type, add_type


dfltSite = 'ftp://speedtest.tele2.net/'
dfltRdir = '.'
dfltUser = ''


class FtpTools:

    def get_localdir(self):
        return(len(sys.argv) > 1 and sys.argv[1]) or '.'

    def get_cleanall(self):
        return input('Clean target dir first?')[:1] in ['y', 'Y']

    def get_password(self):
        return getpass(
            'Password for %s on %s:' % (self.remoteuser, self.remotesite))

    def config_transfer(self, site=dfltSite, rdir=dfltRdir, user=dfltUser):

        self.nonpassive = False
        self.remotesite = False
        self.remotedir = rdir
        self.remoteuser = user
        self.localdir = self.get_localdir()
        self.cleanall = self.get_cleanall()
        self.remotepass = self.get_password()

    def is_text_kind(self, remotename, trace=True):

        add_type('text/x-python-win', '.pyw')
        mimetype, encoding = guess_type(remotename, strict=False)
        mimetype = mimetype or '?/?'
        maintype = mimetype.split('/')[0]
        if trace: print(maintype, encoding or '')
        return maintype == 'text' and encoding == None

    def connect_Ftp(self):
        print('Connecting')
        connection = ftplib.FTP(self.remotesite)
        connection.login(self.remoteuser, self.remotepass)
        connection.cwd(self.remotedir)
        if self.nonpassive:
            connection.set_pasv(False)
        self.connection = connection

    def clean_locals(self):
        if self.cleanall:
            for localname in os.listdir(self.localdir):
                try:
                    print('deleting local', localname)
                    os.remove(os.path.join(self.localdir, localname))
                except:
                    print('cannot delete local', localname)

    def clean_remotes(self):
        if self.cleanall:
            for remotename in self.connection.nlst():
                try:
                    print('deleting remote', remotename)
                    self.connection.delete(remotename)
                except:
                    print('cannot delete remote', remotename)

    def download_one(self, remotename, localpath):
        if self.is_text_kind(remotename):
            localfile = open(localpath, 'w', encoding=self.connection.encoding)
            def callback(line): localfile.write(line + '\n')
            self.connection.retrlines('RETR ' + remotename, callback)
        else:
            localfile = open(localpath, 'wb')
            self.connection.retrbinary('RETR ' + remotename, localfile.write)
        localfile.close()

    def upload_one(self, localname, localpath, remotename):
        if self.is_text_kind(localname):
            localfile = open(localpath, 'rb')
            self.connection.storlines('STOR ' + remotename, localfile)
        else:
            localfile = open(localpath, 'rb')
            self.connection.storbinary('STOR ' + remotename, localfile)
        localfile.close()

    def download_dir(self):
        localfiles = os.listdir(self.localdir)
        for localname in localfiles:
            localpath = os.path.join(self.localdir, localname)
            print('uploading', localpath, 'to', localname, 'as', end=' ')
            self.upload_one(localname, localpath, localname)
        print('Done:', len(localfiles), 'files uploaded.')

    def run(self, clean_target=lambda:None, transfer_act=lambda:None):

        self.connect_Ftp()
        clean_target()
        transfer_act()
        self.connection.quit()


if __name__ == '__main__':
    ftp = FtpTools()
    xfermode = 'download'
    if len(sys.argv) > 1:
        xfermode = sys.argv.pop(1)   # get+del 2nd arg
    if xfermode == 'download':
        ftp.config_transfer()
        ftp.run(clean_target=ftp.clean_locals(), transfer_act=ftp.download_dir())
    elif xfermode == 'upload':
        ftp.config_transfer(site='learning-python.com', rdir='books', user='lutz')
        ftp.run(clean_target=ftp.clean_remotes, transfer_act=ftp.upload_one)
    else:
        print('Usage: ftptools.py ["download" | "upload"] [localdir]')
