# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
    	if new_interval is None:
    		return None
    	
    	new_start = new_interval[0]
    	new_end = new_interval[1]

    	start_interval
    	end_interval

    	for i in xrange(len(intervals)):
    		
    		start = intervals[i[0]]
    		end = interval[i[1]]

    		# fits inside existing intervals
    		if new_start >= start and new_start <= end:
    			start_interval = i
    		
    		if new_end >= start and new_end <= end:
    			end_interval = i

    		# in between, make previous interval
    		if start_interval is None and new_start < start:
    			intervals[i-1[1]] = new_start
    			start_interval = i-1

    		if end_interval is None and new_end < start:
    			intervals[i-1[1]] = new_end
    			end_interval = i-1
    	# merge
    	if end_interval-start_interval > 0:
    		intervals = self.merge(intervals, start_interval, end_interval)
    def merge(self, intervals, start_interval, end_interval):
    	for i in xrange(start_interval, end_interval+1):
    		intervals.remove(i)
    	intervals.insert(i, [start_interval, end_interval])
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
"""