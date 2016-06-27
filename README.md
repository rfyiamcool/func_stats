# func_stats

使用表格方式显示函数调用统计, 没有使用装饰器来实现函数的统计，而是创建pointer的来实现, 这样更加的方便方式，不管在哪个上下文，你只要复用你定制的pointer就可以增加统计。 

注意:
整个项目里就一个依赖外部的模块, prettytable.py , 索性直接把该模块引入到项目中.

#### For test

```
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
```

#### Result:
```
+---------------+----------+------+------+----------+---------+---------+
| Point        | Method   | Line | Hits | Avg Time | Runtime | Percent |
+---------------+----------+------+------+----------+---------+---------+
| once counter  | <module> |    8 |    1 |  0.00001 | 0.00001 |    0.00 |
| loop counter  | <module> |   11 |    4 |  0.00000 | 0.00001 |    0.00 |
| t1 complated  | <module> |   19 |    2 |  0.05046 | 0.10091 |    9.90 |
| sleep counter | <module> |   16 |   10 |  0.09184 | 0.91837 |   90.07 |
+---------------+----------+------+------+----------+---------+---------+
Total runtime: 1.02
```
