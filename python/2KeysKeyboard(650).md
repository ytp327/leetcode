<h1> 650. 2 Keys Keyboard --Medium</h1> 
<p>Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:
1.<code>Copy All</code>: You can copy all the characters present on the notepad (partial copy is not allowed).
2.<code>Paste</code>: You can paste the characters which are copied last time.</p>
<p>Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.</p>

<pre>
<b>Example 1:</b>
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
</pre>

<p>Approach 1 (DP, O(n<sup>2</sup>)):</p>
``` python
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        dp[1] = 0
        for i in range(2, n+1):
            for j in range(i//2, 1, -1):
                if not i%j:
                    dp[i] = dp[j] + i // j
                    break
        return dp[-1]
```
<p>Approach 2 (Math, O(n)):</p>
``` python
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, d = 0, 2
        while n > 1:
        	while not n % d:
        		res += d
        		n /= d
        	d += 1
        return res
```