#!usr/bin/env python
# coding: utf-8

import requests

from base import Process


class UrlProcess(Process):
    """路径处理, 从指定路径中读所有链接返回其所有行.
    """

    def process_target_path(self, target_path):
        """对指定路径执行操作.

            :param target_path: 指定路径
        """

        # 判断路径是否存在
        r = requests.head(target_path)

        if r.status_code != 200:
            print("Url does not exist!")
            return

        pass
