# !usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import os

import tomorrow

import common
import db

dir_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "logs")


@tomorrow.threads(5)
def download(url):
    common.download(url)


def main():
    for url in db.gather_urls(dir_path):
        download(url.strip('\n'))


if __name__ == "__main__":
    main()
