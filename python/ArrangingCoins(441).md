<h1> 441. Arranging Coins --Easy</h1> 
<p>You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.</p>
<p>Given <i>n</i>, find the total number of <b>full</b> staircase rows that can be formed.</p>
<p><i>n</i> is a non-negative integer and fits within the range of a 32-bit signed integer.</p>

<pre>
<b>Example 1:</b>
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
Because the 3rd row is incomplete, we return 2.
<b>Example 2:</b>
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.
</pre>



``` python
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l+r)//2
            guess = mid*(mid+1)//2
            if guess == n: return mid
            elif guess < n: l = mid + 1
            else: r = mid - 1
        return l-1
```
