"""Gunicorn configuration."""
import multiprocessing

bind = '127.0.0.1:9000'

workers = multiprocessing.cpu_count()
worker_class = 'gevent'
timeout = 10 * 60
keepalive = 24 * 60 * 60

accesslog = '-'
