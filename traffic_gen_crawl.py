# !usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import time

import gevent

import common
import db


def main(site_url):
    urls = db.collect_urls(site_url)
    tasks = [gevent.spawn(common.download, url) for url in urls]
    gevent.joinall(tasks)


if __name__ == '__main__':
    start = time.time()
    main('http://www.163.com/')
    print(time.time() - start)
