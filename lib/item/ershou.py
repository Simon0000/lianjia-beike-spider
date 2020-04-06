#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShou(object):
    def __init__(self, district, area, community, price, desc, link, name):
        self.district = district
        self.area = area
        self.community = community
        self.price = price
        self.desc = desc
        self.link=link
        self.name = name
        


    def text(self):
        return self.district + ";" + \
                self.area + ";" + \
                self.community + ";" + \
                self.price + ";" + \
                self.desc + ";" + \
                self.link + ";" + \
                self.name
