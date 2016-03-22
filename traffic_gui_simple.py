# !usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import os
import time

from splinter import Browser

import db

dir_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "logs")

if __name__ == '__main__':
    site_pages = db.gather_urls(dir_path)

    with Browser() as browser:
        for i, page in enumerate(site_pages):
            browser.visit(page.strip('\n'))
            time.sleep(5)
