#!/usr/bin/env python
# -*- coding: utf-8 -*-
# type hints 类型提示


class Calc:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def div(a: int, b: int) -> float:
        return a / b

    @staticmethod
    def sub(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def multi(a: int, b: int) -> int:
        return a * b
