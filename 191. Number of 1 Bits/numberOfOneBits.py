#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

x = 1577962638
print bin(x)

int_length = len(bin(x))
print int_length

output = 0
mask = 1

for i in range(int_length): # 0~31
	
	if (x & (mask<<i)) != 0:
		output += 1
		print "[No Match]!!"
	else:
		print "[Match]!!"
	print "---------------"

# return output
print output
