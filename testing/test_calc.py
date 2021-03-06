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
from src.calc import Calc


class TestCalc:

    def setup(self):
        self.calc = Calc()
        pass

    # @pytest.mark.add
    @pytest.mark.parametrize("v1, v2, v3", yaml.safe_load(open("../data/add.yml")))
    def test_add(self, v1, v2, v3):
        print(v1, v2, v3)
        try:
            result = self.calc.add(v1, v2)
            assert v3 == pytest.approx(result)
        except TypeError as e:
            result = "TypeError"
            assert v3 == result

    # @pytest.mark.div
    @pytest.mark.parametrize("v1, v2, v3", yaml.safe_load(open("../data/div.yml")))
    def test_div(self, v1, v2, v3):
        # self.calc = Calc()
        try:
            result = self.calc.div(v1, v2)
        except Exception as e:
            result = e.__class__.__name__
            assert v3 == result
        else:
            assert v3 == pytest.approx(result)

    # @pytest.mark.sub
    @pytest.mark.parametrize("v1, v2, v3", yaml.safe_load(open("../data/sub.yml")))
    def test_sub(self, v1, v2, v3):
        try:
            result = self.calc.sub(v1, v2)
        except Exception as e:
            result = e.__class__.__name__
            assert v3 == result
        else:
            assert v3 == pytest.approx(result)

    # @pytest.mark.multi
    @pytest.mark.parametrize("v1, v2, v3", yaml.safe_load(open("../data/multi.yml")))
    def test_multi(self, v1, v2, v3):
        try:
            result = self.calc.multi(v1, v2)
        except Exception as e:
            result = e.__class__.__name__
            assert v3 == result
        else:
            assert v3 == pytest.approx(result)


if __name__ == '__main__':
    pytest.main()
