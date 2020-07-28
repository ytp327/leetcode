<h1> 621. Task Scheduler --Medium</h1> 
<p>You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.</p>
<p>However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two <b>same tasks</b>.</p>
<p>You need to return the <b>least</b> number of units of times that the CPU will take to finish all the given tasks.</p>

<pre>
<b>Example 1:</b>
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

<b>Example 2:</b>
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.


<b>Example 3:</b>
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
</pre>



``` python
from collections import *
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count, dupli, maxCount = Counter(tasks), 1, 0
        for x in count.values(): #count duplicate
            if x > maxCount:
                maxCount = x
                dupli = 1
            elif x == maxCount:
                dupli += 1
        return max(len(tasks), (maxCount-1) * (n+1) + dupli)
```