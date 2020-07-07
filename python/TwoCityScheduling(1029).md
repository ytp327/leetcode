<h1> 1029. Two City Scheduling --Easy</h1> 
<p>There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].</p>
<p>Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.</p>

<pre>
<b>Example 1:</b>
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
</pre>



``` python
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key = lambda x: x[0]-x[1])
        return sum(x[0] for x in costs[:len(costs)//2])\
            + sum(x[1] for x in costs[len(costs)//2:])
```
