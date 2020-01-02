#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   RiceProblem.py
@Time    :   2020/01/02 17:11
@Author  :   ZheZi 
@Version :   1.0
@Contact :   XXXXXXX@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   好好吃饭 - 一款解决吃饭选择的神器
'''
import random
import time

from dingtalkchatbot.chatbot import DingtalkChatbot

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=744158b8fe11e364d96d5d534a27520b1ea5cb7689a445c3eb5c6eaf2416f7d4'

with open('DiningDestination.txt', 'r+', encoding='utf-8') as f:
    destination_list = [str(destination).replace('\n', '') for destination in f]

time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
title = '各位老板们好，当前北京时间\n{}\n\n今日觅食区域列表如下\n'.format(time_now)
tail = '开始进行人工智能随机选择，请稍等5秒....'

choosable = title + '\n'.join(destination_list)

result = '今日觅食目标  [加油]{}[加油]'.format(random.choice(destination_list))

ding_obj = DingtalkChatbot(webhook)
ding_obj.send_text(choosable)
print(choosable)
ding_obj.send_text(tail)
print(tail)
time.sleep(5)
ding_obj.send_text(result)
print(result)