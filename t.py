#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

from func_stats.func_stats import CreateStats
b = CreateStats()

b.point("once counter")

for i in range(1,5):
    b.point("loop counter")

b.point("t1 complated")

for i in range(10):
    b.point('sleep counter')
    time.sleep(0.1)

b.point("t1 complated")

b.display()
