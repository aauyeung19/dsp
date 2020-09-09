#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:56:14 2020


@author: andrew


Exercise: In the BRFSS (see Section 5.4), the distribution of heights is 
roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and 
µ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” 
(see http://bluemancasting.com). What percentage of the U.S. male population 
is in this range? Hint: use scipy.stats.norm.cdf.

1 in - 2.54 cm

"""

import scipy.stats

mu = 178
sigma = 7.7

dist = scipy.stats.norm(loc=mu, scale=sigma)

low = 177.8 #low limit
high = 185.42 #top limit

ans = dist.cdf(high)-dist.cdf(low)
ans = ans*100
ans = int(ans)

print('Roughly {}% of the U.S. male population would qualify to be in the Blue Man Group'.format(ans))