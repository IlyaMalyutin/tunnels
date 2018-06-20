import os
import sys
import time
import socket
import subprocess
from multiprocessing import Process

import config


CMD = 0
PORT = 1


def run_cmd(args):
    """
    :param args: tuple
    :return: str
    """
    print('Start: {}'.format(args))
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = proc.communicate()
    print('output: {}, return_code: {}, err: {}'.format(output, proc.wait(), err))
    return output


def start_process(args):
    """
    :param args: tuple
    :return: Process
    """
    p = Process(target=run_cmd, args=(args,))
    p.start()
    return p


def ping(port):
    """
    :param port: str
    :return: bool
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect(('127.0.0.1', int(port)))
        s.shutdown(socket.SHUT_RD)
    except (socket.timeout, ConnectionRefusedError):
        return False
    return True


def start():
    """
    Inter point
    :return:
    """
    threads = {}

    for tunnel in config.tunnels:
        threads[tunnel] = start_process(tunnel[CMD].split(' '))

    time.sleep(config.SLEEP)

    while True:
        for tunnel in threads:
            if not ping(tunnel[PORT]):
                threads[tunnel].terminate()
            if not threads[tunnel].is_alive():
                threads[tunnel] = start_process(tunnel[CMD].split(' '))
                print('started killed process: {}'.format(tunnel))
        time.sleep(config.SLEEP)


if __name__ == '__main__':
    start()
