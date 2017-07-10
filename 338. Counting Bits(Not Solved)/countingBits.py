#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

num = 7
alist = [0] * (num + 1)


for x in range(1,num + 1):
	print x
	print '**'
	if int(math.log(x,2)) == math.log(x,2):
		alist[x] = 1
	else:
		while (x / 2) >= 1:
			print x
			x = x/2 + x%2
	print '*************'

print alist
