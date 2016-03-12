/*
public class Interval {
	int start; 
	int end;
	Interval() { start = 0; end = 0; }
	Interval (int s, int e) { start = s; end = e; }
 } */

 public class Solution {
 	public ArrayList<Interval> insert(ArrayList<Interval> intervals, Interval newInterval) {
 		int start = newInterval.start;
 		int end = newInterval.end;
 		int startIndex = -1, endIndex = -1;
 		int i = 0;

 		for(Interval interval : intervals) {
 			if (start >= interval.start && start <= interval.end)
 				startIndex = i;
 			if (end >= interval.start && end <= interval.end)
 				endIndex = i;
 			++i;
 		}
 		if (startIndex == -1 && endIndex == -1) {
 			startIndex = 0;
 			for (i = 0; i < intervals.size(); ++i)
 				if (start > intervals.get(i).end)
 					startIndex = i+1;

			endIndex = intervals.size()-1;
			for (i = intervals.size()-1; i >= 0; --i)
				if (end < intervals.get(i).start)
					endIndex = i-1;

			for (i = startIndex; i <= endIndex; ++i)
				intervals.remove(startIndex);

			intervals.add(startIndex, newInterval);
			return intervals;
 		}
 		if (startIndex == -1) 
 			for (i = intervals.size()-1; i >= 0; --i)
 				if (start <= intervals.get(i).start)
 					startIndex = i;
 		
 		if (endIndex == -1) 
 			for (i = 0; i < intervals.size(); ++i)
 				if (end >= intervals.get(i).end)
 					endIndex = i;
 		
 		start = Math.min(intervals.get(startIndex).start, start);
 		end = Math.max(intervals.get(endIndex).end, end);
 
 		intervals.get(startIndex).start = start;
 		intervals.get(startIndex).end = end;

 		for (i = startIndex + 1; i <= endIndex; ++i)
 			intervals.remove(startIndex+1);
 		return intervals;

 	}
 }