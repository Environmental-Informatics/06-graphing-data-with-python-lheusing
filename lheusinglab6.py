#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:14:37 2020

@author: lheusing
"""

import numpy as np
import matplotlib.pyplot as plt

import os

for file in os.listdir('./'):
    if file.endswith(".txt"):
        print(file)
        print(" \n")



inname = input('enter file name to use \nthe file must be in the same directory \npossible files are listed above')

outname = input('enter name to save pdf as ')

data = np.genfromtxt(inname, names=True)


plt.subplot(3,1,1) #plot 1 mena max and min
plt.plot(data['Year'], data['Mean'], color = 'k',label='mean')
plt.plot(data['Year'], data['Max'], color = 'r',label = 'max')
plt.plot(data['Year'], data['Min'], color = 'b', label = 'min')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.5), shadow=True, ncol=3)
plt.xlabel('Year')
plt.ylabel('Streamflow(cfs)')
 
plt.subplot(3,1,2)#middle subplot tqmean in symbols
plt.plot(data['Year'],data['Tqmean']*100, 'r^')
plt.xlabel('Year')
plt.ylabel('Tqmean (%)')

plt.subplot(3,1,3)#lower sublpot of RB index as boxplot
plt.bar(data['Year'],data['RBindex'])
plt.xlabel('Year')
plt.ylabel('R-B index (ratio)')

plt.tight_layout() #fix overlap
plt.savefig(outname +'.pdf')