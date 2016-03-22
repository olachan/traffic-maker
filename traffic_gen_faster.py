# !usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import requests
import tomorrow
from user_agent import generate_user_agent

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
    response = requests.get(url, headers={'User-Agent': generate_user_agent()})
    print("%s ==> %s" % (url, response.status_code))


def main():
    for url in gather_urls():
        download(url.strip('\n'))


if __name__ == "__main__":
    main()
