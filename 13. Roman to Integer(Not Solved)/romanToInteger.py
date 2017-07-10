#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 罗马数字共有七个，即I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)。按照下面的规则可以表示任意正整数。

x = 'DCXXXII'
result = 0
for a in x:
	print a
	if a == "D":
		result += 100
	elif a == "C":
		result += 50
	elif a == 'X':
		result += 10
	elif a == 'V':
		result += 5
	elif a == "I":
		result += 1

print result
