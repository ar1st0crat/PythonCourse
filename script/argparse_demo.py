import argparse
import sys


def check_arg(args=None):
    ''' parsing demo function '''

    parser = argparse.ArgumentParser(
        description='Script to learn basic argparse')

    parser.add_argument('-H', '--host',
                        help='host ip',
                        required='True',
                        default='localhost')
    parser.add_argument('-p', '--port',
                        help='port of the web server',
                        default='8080')
    parser.add_argument('-u', '--user',
                        help='user name',
                        default='root')
    parser.add_argument('-m', '--misc',
                        help='miscellaneous',
                        action='store_true')

    parsed = parser.parse_args(args)
    return parsed.host, parsed.port, parsed.user, parsed.misc


if __name__ == '__main__':
    h, p, u, m = check_arg(sys.argv[1:])
    print('host = {}'.format(h))
    print('port = {}'.format(p))
    print('user = {}'.format(u))
    print('misc = {}'.format(m))