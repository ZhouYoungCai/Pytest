if __name__ == '__main__':
    # 运行当前目录下所有的 用例
    pytest.main()
#coding:utf-8
from pytest import *

# package
# __init__.py
import re
import urllib
import sys
import os
# a.py
import package 
print(package.re, package.urllib, package.sys, package.os)
