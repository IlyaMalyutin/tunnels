import os
import sys
import time
import socket
import logging
import logging.config
import subprocess
from multiprocessing import Process

import config

os.makedirs('logs', exist_ok=True)
logging.config.dictConfig(config.logging_conf)
logger = logging.getLogger('tunnels')

CMD = 0
PORT = 1


def run_cmd(args):
    """
    :param args: tuple
    :return: str
    """
    logger.info('Start: {}'.format(args))
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = proc.communicate()
    logger.info('output: {}, return_code: {}, err: {}'.format(output, proc.wait(), err))
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
    death_count = 0
    max_death_count = len(config.tunnels) * 3

    while True:
        for tunnel in threads:
            if not ping(tunnel[PORT]):
                threads[tunnel].terminate()
                death_count += 1
            else:
                death_count = 0

            if not threads[tunnel].is_alive():
                threads[tunnel] = start_process(tunnel[CMD].split(' '))
                logger.info('started killed process: {}'.format(tunnel))

        if death_count >= max_death_count:
            logger.info('exceeded death count!')
            return -1
        time.sleep(config.SLEEP)


if __name__ == '__main__':
    start()
