#!~/anaconda2/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import numpy as np
import pandas as pd

data_text = ['# I am happy #',
			 '# happy is an emotion #',
			 '# I am not happy #',
			 '# Our work suggests that neuroevolution approaches can be competitive #',
			 '# In particular, note that the submarine in Seaquest correctly learns to go up when its oxygen reaches low levels #']
print data_text
#### matrix M * M ####
#P(wi|wi_1) = count(wi, wi_1)/ count(wi_1)
all_words = set()
for each_sent in data_text:
	each_sent_list = each_sent.split(' ')
	for word in each_sent_list:
		if word in all_words: continue
		all_words.add(word)
print all_words
print len(all_words)

#### 计算概率矩阵 #####

for word1 in all_words:
	for word2 in all_words:
		count_join = sum([i.count(word2 +' '+ word1) for i in data_text])
		count_sing = sum([i.count(word2) for i in data_text])
		P = float(count_join)/float(count_sing)
		if float(P) == 0.0: continue
		print 'P('+word1+'|'+word2+') = ' +str(P)

