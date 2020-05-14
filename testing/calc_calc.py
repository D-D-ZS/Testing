#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/14 11:17  
# Author  : DanDan Zhao 
# File    : calc_calc.py  
# 

import pytest
import yaml
from src.calc import Calc


@pytest.fixture()
def init_calc():
    return Calc


class CalcCalc:
    # def setup(self):
    #     self.calc = Calc()
    #     pass

    # @pytest.mark.add
    @pytest.mark.parametrize("v1, v2, v3", yaml.safe_load(open("../data/add.yml")))
    def calc_add(self, v1, v2, v3, init_calc):
        calc = init_calc()
        print(v1, v2, v3)
        try:
            result = calc.add(v1, v2)
            assert v3 == pytest.approx(result)
        except TypeError as e:
            result = "TypeError"
            assert v3 == result

    # @pytest.mark.div
    @pytest.mark.parametrize("v1, v2, v3", yaml.safe_load(open("../data/div.yml")))
    def calc_div(self, v1, v2, v3, init_calc):
        # self.calc = Calc()
        calc = init_calc()
        try:
            result = calc.div(v1, v2)
        except Exception as e:
            result = e.__class__.__name__
            assert v3 == result
        else:
            assert v3 == pytest.approx(result)

    # @pytest.mark.sub
    @pytest.mark.parametrize("v1, v2, v3", yaml.safe_load(open("../data/sub.yml")))
    def calc_sub(self, v1, v2, v3, init_calc):
        calc = init_calc()
        try:
            result = calc.sub(v1, v2)
        except Exception as e:
            result = e.__class__.__name__
            assert v3 == result
        else:
            assert v3 == pytest.approx(result)

    # @pytest.mark.multi
    @pytest.mark.parametrize("v1, v2, v3", yaml.safe_load(open("../data/multi.yml")))
    def calc_multi(self, v1, v2, v3, init_calc):
        calc = init_calc()
        try:
            result = calc.multi(v1, v2)
        except Exception as e:
            result = e.__class__.__name__
            assert v3 == result
        else:
            assert v3 == pytest.approx(result)


if __name__ == '__main__':
    pytest.main("-v")
