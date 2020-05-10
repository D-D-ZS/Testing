#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/10 11:23  
# Author  : DanDan Zhao 
# File    : test_calc_add.py  
#
import pytest
import yaml
from python.calc import Calc


class TestCalc:

    def setup(self):
        self.calc = Calc()
        pass

    @pytest.mark.parametrize("v1, v2, v3", yaml.safe_load(open("../data/add.yml")))
    def test_add(self, v1, v2, v3):
        print(v1, v2, v3)
        try:
            result = self.calc.add(v1, v2)
        except TypeError as e:
            result = "TypeError"
        print(result)
        assert v3 == result

    @pytest.mark.parametrize("v1, v2, v3", yaml.safe_load(open("../data/div.yml")))
    def test_div(self, v1, v2, v3):
        # self.calc = Calc()
        try:
            result = self.calc.div(v1, v2)
        except TypeError as e:
            result = "TypeError"
        except ZeroDivisionError as e:
            result = "ZeroDivisionError"

        assert v3 == result


if __name__ == '__main__':
    pytest.main()
