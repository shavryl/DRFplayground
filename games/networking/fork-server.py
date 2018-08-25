"""
Server side: open a socket on a port, listen for a message from a client,
and send an echo reply; forks a process to handle each client connection;
child processes share parent's socket descriptors; fork is less portable
than threads--not yet on Windows, unless Cygwin or similar installed;
"""

import os, time, sys, signal, _signal
from socket import *
myPort = 50007
myHost = ''

activeChildren = []

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)


def now():
    return time.ctime(time.time())


def reap_children():
    while activeChildren:
        pid, stat = os.waitpid(0, os.WNOHANG)
        if not pid: break
        activeChildren.remove(pid)


def hangle_client(connection):
    # simulate a blocking activity
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data: break
        reply = 'Echo =>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()
    os._exit(0)


def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print('Server connected by', address, end=' ')
        print('at', now())
        # clean up exited children now
        reap_children()
        child_pid = os.fork()
        if child_pid == 0:
            hangle_client(connection)
        else:
            activeChildren.append(child_pid)


dispatcher()
