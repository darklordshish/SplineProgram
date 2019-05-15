#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:34:35 2017

@author: semion
"""
import numpy as np


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
