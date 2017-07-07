#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Question: Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
          Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

Example: 
Given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

''' Worked, but took too much time since Big O is n^3
class solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
 		:rtype: List[List[int]]
		"""
		nums.sort()
		list = [] 
		for i in range(0, len(nums)):
			for j in range(i+1, len(nums)):
				for k in range(j+1, len(nums)):
					if ((nums[i] + nums[j] + nums[k]) == 0):
						potential_result = [nums[i], nums[j], nums[k]];
						if len(list) == 0:
							list.append(potential_result)
						else:
							hit = False;
							for x in list:
								if (cmp(x, potential_result) == 0):
									hit = True
									break
							if (hit == False):
								list.append(potential_result)


		return list
'''
''' Still doesn't work. Too many exception to handle
'''
# nums = [-4,-8,7,13,10,1,-14,-13,0,8,6,-13,-5,-4,-12,2,-11,7,-5,0,-9,-14,-8,-9,2,-7,-13,-3,13,9,-14,-6,8,1,14,-5,-13,8,-10,-5,1,11,-11,3,14,-8,-10,-12,6,-8,-5,13,-15,2,11,-5,10,6,-1,1,0,0,2,-7,8,-6,3,3,-13,8,5,-5,-3,9,5,-4,-14,11,-8,7,10,-6,-3,11,12,-14,-9,-1,7,5,-15,14,12,-5,-8,-2,4,2,-14,-2,-12,6,8,0,0,-2,3,-7,-14,2,7,12,12,12,0,9,13,-2,-15,-3,10,-14,-4,7,-12,3,-10]
# nums = [-1,0,1,2,-1,-4]
nums = [7,5,-8,-6,-13,7,10,1,1,-4,-14,0,-1,-10,1,-13,-4,6,-11,8,-6,0,0,-5,0,11,-9,8,2,-6,4,-14,6,4,-5,0,-12,12,-13,5,-6,10,-10,0,7,-2,-5,-12,12,-9,12,-9,6,-11,1,14,8,-1,7,-13,8,-11,-11,0,0,-1,-15,3,-11,9,-7,-10,4,-2,5,-4,12,7,-8,9,14,-11,7,5,-15,-15,-4,0,0,-11,3,-15,-15,7,0,0,13,-7,-12,9,9,-3,14,-1,2,5,2,-9,-3,1,7,-12,-3,-1,1,-2,0,12,5,7,8,-7,7,8,7,-15]

import sys

alist = [] 
nums.sort()

print nums

dictionary = {}

if (len(nums) < 3):
	sys.exit()

for x in nums:
	index = str(x);
	if (not dictionary.has_key(index)):
		dictionary[index] = x;

for i in range(0, len(nums)):
	print "nums[%d] = %d" % (i, nums[i])
	for j in range(i+1, len(nums)):
		print "+---nums[%d] = %d" % (j, nums[j])
		answer = -(nums[i]+nums[j])

		if (dictionary.has_key(str(answer))):
			if (nums.count(dictionary[str(answer)]) == 1 and (dictionary[str(answer)] == nums[i] or dictionary[str(answer)] == nums[j])):
				continue
			if (nums.count(dictionary[str(answer)]) == 2 and (dictionary[str(answer)] == nums[i] and dictionary[str(answer)] == nums[j])):
				continue
			potential_result = [nums[i],nums[j],answer]
			potential_result.sort()
			if len(alist) == 0:
				alist.append(potential_result)
				print "!Action: Insert ", potential_result
			else:
				hit = False;
				for x in alist:
					if (cmp(x, potential_result) == 0):
						hit = True
						break
				if (hit == False):
					alist.append(potential_result)
					print "!Action: Insert ", potential_result
# return alist

print alist

# nums = [-4,-8,7,13,10,1,-14,-13,0,8,6,-13,-5,-4,-12,2,-11,7,-5,0,-9,-14,-8,-9,2,-7,-13,-3,13,9,-14,-6,8,1,14,-5,-13,8,-10,-5,1,11,-11,3,14,-8,-10,-12,6,-8,-5,13,-15,2,11,-5,10,6,-1,1,0,0,2,-7,8,-6,3,3,-13,8,5,-5,-3,9,5,-4,-14,11,-8,7,10,-6,-3,11,12,-14,-9,-1,7,5,-15,14,12,-5,-8,-2,4,2,-14,-2,-12,6,8,0,0,-2,3,-7,-14,2,7,12,12,12,0,9,13,-2,-15,-3,10,-14,-4,7,-12,3,-10]
nums = [-1,0,1,2,-1,-4]

import sys

alist = [] 
nums.sort()

for x in iter(nums):
	print x