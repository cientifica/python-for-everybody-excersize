# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:46:49 2022

@author: Lindean
"""

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From': continue
    print(words[1])
    count+=1
print("count",count)