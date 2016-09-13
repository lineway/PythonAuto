# coding:utf-8
__author__ = 'PieLs'

import psutil
import datetime

'''
CPU信息
'''
psutil.cpu_times()                          # 获取CPU完整信息
psutil.cpu_times(percpu=True)               # 获取所有逻辑CPU信息
psutil.cpu_times().user                     # 获取单项数据，默认logical=True
psutil.cpu_count()                          # 获取CPU个数

'''
内存信息
'''
psutil.virtual_memory()                     # 获取内存完整信息
psutil.swap_memory()                        # 获取swap分区信息

'''
磁盘信息
'''
psutil.disk_partitions()                    # 获取磁盘完整信息
psutil.disk_usage('/')                      # 获取分区'/'的使用情况
psutil.disk_io_counters()                   # 获取磁盘总的IO个数
psutil.disk_io_counters(perdisk=True)       # 获取单个磁盘的IO数

'''
网络信息
'''

psutil.net_io_counters()                    # 获取网络总的IO量
psutil.net_io_counters(pernic=True)         # 获取每个网络接口的IO量

'''
其他系统信息
'''
psutil.users()                              # 返回登录系统的用户信息
psutil.boot_time()                          # 返回开机时间,以Linux时间戳格式返回
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H: %M: %S")   # 转换时间格式

