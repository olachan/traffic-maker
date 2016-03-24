#!usr/bin/env python
# coding: utf-8

import urlparse

import bs4
import requests

from base import Process
from conf import LINKS_IGNORE


class UrlProcess(Process):
    """路径处理, 从指定路径中读所有链接返回其所有行.
    """

    def __init__(self, parent_path):
        """初始化操作路径, 操作命令.

            :parameter parent_path: 操作路径
        """

        super(UrlProcess, self).__init__(parent_path)

        result = urlparse.urlsplit(parent_path) if parent_path else None
        head_url = "%s://%s" % (result.scheme, result.netloc) if result else ""
        self._head_url = head_url

    def process_target_path(self, target_path):
        """对指定路径执行操作.

            :param target_path: 指定路径
        """

        # 判断路径是否存在
        r = requests.get(target_path)

        if r.status_code != 200:
            print("Url does not exist!")
            return

        soup = bs4.BeautifulSoup(r.text, "lxml")
        for link in soup.find_all('a'):
            href_string = link.get('href')
            href_string = href_string.lower().strip('/').strip('javascript:;') if href_string else None
            if href_string:
                self._all_lines.append(href_string)

    def __call__(self):
        lines = super(UrlProcess, self).__call__()
        lines = filter(lambda x: x[x.rfind('.'):] not in LINKS_IGNORE, lines)

        for i in xrange(len(lines)):
            if lines[i] and not lines[i].startswith(self._head_url):
                lines[i] = urlparse.urljoin(self._head_url, lines[i])

        return lines
