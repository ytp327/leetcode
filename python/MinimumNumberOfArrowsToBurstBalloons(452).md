<h1> 452. Minimum Number of Arrows to Burst Balloons --Medium</h1> 
<p>There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.</p>
<p>An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.</p>
<p>Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.</p>

<pre>
<b>Example 1:</b>
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
<b>Example 2:</b>
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
<b>Example 3:</b>
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
<b>Example 4:</b>
Input: points = [[1,2]]
Output: 1
<b>Example 5:</b>
Input: points = [[2,3],[2,3]]
Output: 1
</pre>


``` python
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[1])
        res, end = 0, -float('inf')
        for point in points:
            if point[0] > end:
                res += 1
                end = point[1]
        return res
```