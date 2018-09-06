#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:32:17 2017

@author: semion
"""
# import numpy as np
from Parameter.py import Parameter
from Result.py import Result


class Function(object):
    """
    """
    def __init__(self, func=False, num=100, func_data={'number_of_param': 2,
                                                       'numder_of_res': 1,
                                                       'discription': None}):
        self.num = num
        if func:
            self.f = func
        else:
            self.f = lambda x, y: x + y
        self.function_data = func_data


class Model():
    """
    """
    def __init__(self, *args, **kwards):
        self.num = 100
        self.Function = Function()
        self.Parameters = [Parameter() for x in range(
                           self.Function.function_data['number_of_param'])]
        self.Results = [Result() for x in range(
                        self.Function.function_data['numder_of_res'])]
        self.num = 100

        self.greed = [self.Parameters[0].param_greed,
                      self.Parameters[1].param_greed]

        self.Results[0].meaning = self.Function.f(self.greed[0], self.greed[1])
