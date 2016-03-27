#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, print_function

import random

import requests
import user_agent

import conf


def download(url):
    """访问网址.

        :param url: 网址
    """

    headers = {'User-Agent': user_agent.generate_user_agent()}

    proxies = {
        'http': random.choice(conf.HTTP_PROXIES) if conf.HTTP_PROXIES else None,
        'https': random.choice(conf.HTTPS_PROXIES) if conf.HTTPS_PROXIES else None,
    }

    response = requests.get(url, proxies=proxies, verify=False, headers=headers)
    print("%s ==> %s" % (url, response.status_code))
