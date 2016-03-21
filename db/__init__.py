#!usr/bin/env python
# coding: utf-8

import os

from files import TXTProcess, XMLProcess

logs_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "logs")


def all_file_lines(kind='txt'):
    """文本文件所有行.

        :param kind: 文件类型
    """

    if kind not in ['txt', 'xml']:
        return

    file_list, file_lines = None, None

    if kind == 'txt':
        file_list = TXTProcess(parent_path=logs_dir)
    elif kind == 'xml':
        file_list = XMLProcess(parent_path=logs_dir)

    if file_list:
        file_lines = file_list()

    return file_lines
