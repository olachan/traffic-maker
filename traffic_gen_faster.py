# !usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import random

import requests
import tomorrow
import user_agent

from conf import HTTP_PROXIES, HTTPS_PROXIES
from db import all_file_lines


def gather_urls():
    """收集目标网址.
    """

    urls_list = []
    for kind in ['txt', 'xml']:
        urls_list.extend(all_file_lines(kind))
    return urls_list


@tomorrow.threads(5)
def download(url):
    """访问网址.

        :param url: 网址
    """

    headers = {'User-Agent': user_agent.generate_user_agent()}

    proxies = {
        'http': random.choice(HTTP_PROXIES),
        'https': random.choice(HTTPS_PROXIES),
    }

    response = requests.get(url, proxies=proxies, verify=False, headers=headers)
    print("%s ==> %s" % (url, response.status_code))


def main():
    for url in gather_urls():
        download(url.strip('\n'))


if __name__ == "__main__":
    main()
