import argparse, paramiko, sys


# Using SSH like TELNET: connecting and running two commands


class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):

    def missing_host_key(self, client, hostname, key):
        return


def main(hostname, username):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(AllowAnythingPolicy())
    client.connect(hostname, username=username)

    channel = client.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')

    stdin.write(b'echo Hello, world\rexit\r')
    output = stdout.read()
    client.close()

    sys.stdout.buffer.write(output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Connect over SSH')
    parser.add_argument('hostname', help='Remote machine name')
    parser.add_argument('username', help='Username on the remote machine')
    args = parser.parse_args()
    main(args.hostname, args.username)
