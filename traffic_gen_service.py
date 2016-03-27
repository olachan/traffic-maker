# !usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import random
from functools import partial

from twisted.internet import task, reactor

import common

limits = (1, 2, 3)
intervals = (30, 50, 70, 100)


@common.skip_hours
def fake_accessor(pages_count=1):
    """模拟访问网页.

        :param pages_count: 每次访问数量
    """
    print(pages_count)
    pass


def imitate_visitors(always=False):
    """模拟访客.

        :param always: 是否一直运行
    """

    if always:
        # 纳入间隔时间后再次执行
        create_data = task.LoopingCall(fake_accessor, limits[0])
        create_data.start(intervals[0])
        reactor.run()
    else:
        cb = partial(fake_accessor, pages_count=random.choice(limits))
        common.NoInterval.demo(cb, intervals=intervals)


if __name__ == '__main__':
    imitate_visitors()
