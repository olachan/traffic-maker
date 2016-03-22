#!usr/bin/env python
# coding: utf-8

import os
import xml.dom.minidom as xml_dom

from base import Process


class FileProcess(Process):
    """文件处理, 从指定目录中读所有文件返回其所有行.
    """

    def process_target_path(self, target_path):
        """对指定目录执行操作.

            :param target_path: 指定目录
        """

        # 判断路径是否存在
        if not os.path.exists(target_path):
            print("Directory does not exist!")
            return

        for i in os.listdir(target_path):
            sub_path = os.path.join(target_path, i)
            if os.path.isdir(sub_path):
                self.process_target_path(sub_path)
            elif os.path.isfile(sub_path):
                self.read_lines(sub_path)
            else:
                pass


class TXTProcess(FileProcess):
    """适用于行分隔的网址.
    """

    def read_lines(self, file_path):
        """读取无格式文本文件.

            :parameter file_path: 文件
        """

        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                lines = [item for item in f.readlines() if item.startswith('http')]
                if lines:
                    self._all_lines.extend(lines)


class XMLProcess(FileProcess):
    """适用于站点地图(sitemap.xml).
    """

    def read_lines(self, file_path):
        """读取有格式文本文件.

            :parameter file_path: 文件
        """

        node_flag = 'loc'  # 节点标识

        if os.path.exists(file_path) and os.path.isfile(file_path):
            try:
                xml_file = xml_dom.parse(file_path)
            except Exception, ex:
                print(ex)
                lines = None
            else:
                items = xml_file.documentElement.getElementsByTagName(node_flag)
                lines = [item.firstChild.data for item in items]

            if lines:
                self._all_lines.extend(lines)


def all_file_lines(dir_path, kind='txt'):
    """文本文件所有行.

        :param dir_path: 文件目录
        :param kind: 文件类型
    """

    if kind not in ['txt', 'xml', 'url']:
        return

    file_list, file_lines = None, None

    if kind == 'txt':
        file_list = TXTProcess(parent_path=dir_path)
    elif kind == 'xml':
        file_list = XMLProcess(parent_path=dir_path)

    if file_list:
        file_lines = file_list()

    return file_lines


def gather_urls(dir_path):
    """收集目标网址.

        :param dir_path: 文件目录
    """

    urls_list = []
    for kind in ['txt', 'xml']:
        urls_list.extend(all_file_lines(dir_path, kind))
    return urls_list
