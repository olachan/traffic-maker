# !usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import os
import random

import requests
import tomorrow
import user_agent

import conf
import db

dir_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "logs")


@tomorrow.threads(5)
def download(url):
    """访问网址.

        :param url: 网址
    """

    headers = {'User-Agent': user_agent.generate_user_agent()}

    proxies = {
        'http': random.choice(conf.HTTP_PROXIES),
        'https': random.choice(conf.HTTPS_PROXIES),
    }

    response = requests.get(url, proxies=proxies, verify=False, headers=headers)
    print("%s ==> %s" % (url, response.status_code))


def main():
    for url in db.gather_urls(dir_path):
        download(url.strip('\n'))


if __name__ == "__main__":
    main()
