<h1> 56. Merge Intervals --Medium</h1> 
<p>Given a collection of intervals, merge all overlapping intervals.</p>
<pre><b>Example 1:</b>
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

<b>Example 2:</b>
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.</pre>
``` python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals: return []
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for x in intervals[1:]:
            if x[0] <= res[-1][1]:
                res[-1][1] = max(x[1], res[-1][1])
            else:
                res.append(x)
        return res
```
</br>
<h1>57. Insert Interval --Hard</h1>
<p>Given a set of <i>non-overlapping</i> intervals, insert a new interval into the intervals (merge if necessary).</p>
<p>You may assume that the intervals were initially sorted according to their start times.</p>
<pre><b>Example 1:</b>
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

<b>Example 2:</b>
IInput: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].</pre>
```python
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res, i = [], 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res += [newInterval] + intervals[i:]
        return res
```
<br>
<h1>986. Interval List Intersections --Medium</h1> 
<p>Given two lists of <b>closed</b> intervals, each list of intervals is pairwise disjoint and in sorted order.</p>
<p>Return the intersection of these two interval lists.
(Formally, a closed interval <code>[a, b]</code> (with <code>a <= b</code>) denotes the set of real numbers x with <code>a <= x <= b</code>.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)</p>
<pre><b>Example 1:</b>
<img src="../pic/intervals.png" alt="intervals">
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]</pre>
``` python
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        a, b, res = 0, 0, []
        while a < len(A) and b < len(B):
            res.append([max(A[a][0], B[b][0]), min(A[a][1], B[b][1])])
            if res[-1][1] == A[a][1]:
                a += 1
            else:
                b += 1
            if res[-1][0] > res[-1][1]:
                res.pop()
        return res
```