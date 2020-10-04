<h1> 1288. Remove Covered Intervals --Medium</h1> 
<p>Given a list of intervals, remove all intervals that are covered by another interval in the list.</p>
<p>Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.</p>
<p>After doing so, return the number of remaining intervals.</p>

<pre>
<b>Example 1:</b>
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
<b>Example 2:</b>
Input: intervals = [[1,4],[2,3]]
Output: 1
<b>Example 3:</b>
Input: intervals = [[0,10],[5,12]]
Output: 2
<b>Example 4:</b>
Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2
<b>Example 5:</b>
Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1
</pre>


``` python
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: (x[0], -x[1]))
        j, res = 0, 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                pass
            else:
                res += 1
                j = i
        return res
```