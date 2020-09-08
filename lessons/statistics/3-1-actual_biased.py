#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:24:45 2020

@author: andrew


ThinkStats2 Chapter 3 Exercise 1   

Something like the class size paradox appears if you survey children and ask 
how many children are in their family. Families with many children are more 
likely to appear in your sample, and families with no children have no chance 
to be in the sample.

Use the NSFG respondent variable NUMKDHH to construct the actual distribution 
for the number of children under 18 in the household.

Now compute the biased distribution we would see if we surveyed the children 
and asked them how many children under 18 (including themselves) are in their 
household.

Plot the actual and biased distributions, and compute their means. As a 
starting place, you can use chap03ex.ipynb. 


"""



import nsfg
import thinkplot
import thinkstats2


def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


#read resp file
resp = nsfg.ReadFemResp()

#actual distribution
actual_hh = resp.numkdhh
actual_pmf = thinkstats2.Pmf(actual_hh, label='Actual Distribution')

#
bias_pmf = BiasPmf(actual_pmf, 'Biased Distribution')

thinkplot.PrePlot(2)
thinkplot.Pmfs([actual_pmf, bias_pmf])
thinkplot.Config(xlabel='Class size', ylabel='PMF')

print('Actual distribution mean: {}'.format(actual_pmf.Mean()))
print('Biased distribution mean: {}'.format(bias_pmf.Mean()))