# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:30:15 2016

@author: semion
"""
import numpy as np


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


class Parameter():
    """
    """
    def __init__(self, num=100):
        self.num = num
        self.Min = 0
        self.Max = 1
        self.diskrete = False
        self.param_greed = np.linspace(self.Min, self.Max, self.num)

    def ChangeAll(self, num=100, Min=0, Max=1, Disktete=False):
        self.num = num
        self.Min = Min
        self.Max = Max
        self.diskrete = Disktete
        self.param_greed = np.linspace(Min, Max, num)

    def ChangeNum(self, num=100):
        self.num = num
        self.param_greed = np.linspace(self.Min, self.Max, num)

    def ChangeMin(self, Min=0):
        self.Min = Min
        self.param_greed = np.linspace(Min, self.Max, self.num)

    def ChangeMax(self, Max=1):
        self.Max = Max
        self.param_greed = np.linspace(self.Min, Max, self.num)


class Result():
    """
    """
    def __init__(self, num=100):
        self.num = num
        self.min = None
        self.max = None
        self.meaning = []

    def Update(self, Num=100, Meaning=[]):
        self.num = Num
        if Meaning:
            self.min = np.min(Meaning)
            self.max = np.max(Meaning)
            self.meaning = Meaning


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
