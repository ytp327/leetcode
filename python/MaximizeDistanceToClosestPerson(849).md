<h1> 849. Maximize Distance to Closest Person --Medium</h1> 
<p>You are given an array representing a row of <code>seats</code> where seats[i] = 1 represents a person sitting in the i<sup>th</sup> seat, and seats[i] = 0 represents that the i<sup>th</sup> seat is empty (0-indexed).</p>
<p>There is at least one empty seat, and at least one person sitting.</p>
<p>Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. </p>
<p>Return that maximum distance to the closest person.</p>
<img src = "../pic/personDistance.jpg" >

<pre>
<b>Example1:</b>
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
<b>Example2:</b>
Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
<b>Example3:</b>
Input: seats = [0,1]
Output: 1
</pre>

``` python
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        pre, res = None, 0
        for i, x in enumerate(seats):
            if x:
                if pre == None:
                    res = i
                else:
                    res = max(res, (i-pre)//2)
                pre = i
        # can we take the last seat
        if not seats[-1]:
            res = max(res, len(seats)-1-pre)
        return res
```