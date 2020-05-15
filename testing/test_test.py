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


class TestTest:
    @staticmethod
    def setup_class():
        print("set up")
        # pytest.skip("NOT implement")

    # @pytest.mark.other
    def test_needsfiles(self, tmpdir):
        print(tmpdir)
        print(type(self.test_needsfiles))
        assert True

    def test_demo1(self):
        assert 1 == 1
        pytest.fail(msg="预期失败", pytrace=False)


if __name__ == '__main__':
    pytest.main()
