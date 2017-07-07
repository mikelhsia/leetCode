#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

# x = 1577962638
x = 0
print bin(x)
y = 10
# y = 1727613287
print bin(y)

int_length = max(len(bin(x)), len(bin(y)))
print int_length

output = 0
mask = 1

for i in range(int_length): # 0~31
	a = x & (mask<<i)
	b = y & (mask<<i)
	print "a = ", bin(a)
	print "b = ", bin(b)
	if a != b:
		output += 1
		print "[No Match]!!"
	else:
		print "[Match]!!"
	print "---------------"

# return output
print output
