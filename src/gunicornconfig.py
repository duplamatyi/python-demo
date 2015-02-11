from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count() * 2 + 1


bind = 'unix://tmp/supervisord.sock'
max_requests = 1
worker_class = 'gevent'
workers = max_workers()
reload = True
