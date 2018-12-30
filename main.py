# -*- coding: utf-8 -*-
# 调试 scrapy

from scrapy.cmdline import execute
import sys, os

# 获取绝对路径 (只适合于当前电脑)
# sys.path.append('/Users/wsm/PycharmProjects/ArticleSpider')

# os.path.abspath(__file__) 获取当前文件路径
# os.path.dirname() 获取文件的父目录
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'jobbole'])