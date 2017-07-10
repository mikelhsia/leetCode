#!/usr/bin/python
# -*- coding: UTF-8 -*-
g = [10,9,8,7]
s = [5,6,7,8]
output = 0
length = len(s)

g.sort()
s.sort()
print g
print s

child_index = 0

for x in s:
	if ((len(s) == 0) or (len(g) == 0)):
		continue
	if (g[child_index] <= x):
		output += 1
		g.remove(g[child_index])

# return output
print output