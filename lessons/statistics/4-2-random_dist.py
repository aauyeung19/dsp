#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:38:51 2020

@author: andrew
"""
import sys
sys.path.insert(0, '/home/andrew/metis_prework/ThinkStats2/code')

import thinkplot
import thinkstats2


from random import random

random_list = [random() for each in range(1000)]

pmf = thinkstats2.Pmf(random_list, label='random Pmf')

cdf = thinkstats2.Cdf(random_list, label='random Cdf')

thinkplot.Pmf(pmf, label='random Pmf')
thinkplot.Cdf(cdf, label='random cdf')

