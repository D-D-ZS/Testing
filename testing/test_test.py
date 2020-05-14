#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/12 20:29  
# Author  : DanDan Zhao 
# File    : test_test.py  
#

# 为每一次测试创建唯一的临时目录
import pytest


@pytest.mark.other
def test_needsfiles(tmpdir):
    print(tmpdir)
    print(type(test_needsfiles))
    assert True


@pytest.fail(msg="预期失败", pytrace=False)
def test_demo1():
    assert 1 == 0


if __name__ == '__main__':
    pytest.main()
