#!usr/bin/env python
# coding: utf-8

import six


class Process(object):
    """数据处理, 从指定路径中读所有数据返回其所有行.
    """

    def __init__(self, parent_path):
        """初始化操作路径, 操作命令.

            :parameter parent_path: 操作路径
        """

        self._directory = parent_path
        self._all_lines = []

    def read_lines(self, file_path):
        pass

    def process_target_path(self, target_path):
        pass

    def run_work(self):
        """对指定的操作路径, 执行指定的操作命令.
        """

        if isinstance(self._directory, six.string_types):
            self.process_target_path(self._directory)
        elif isinstance(self._directory, (tuple, list)):
            for path in self._directory:
                self.process_target_path(path)
        else:
            pass

        print("Ok, Files are done!\r")

    def __call__(self):
        self.run_work()

        if self._all_lines:
            # 去重
            return list(set(self._all_lines))
