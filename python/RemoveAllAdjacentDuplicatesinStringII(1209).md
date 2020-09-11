<h1> 454. 4Sum II --Medium</h1> 
<p>Given a string <code>s</code>, a <code>k</code> duplicate removal consists of choosing <code>k</code> adjacent and equal letters from <code>s</code> and removing them causing the left and the right side of the deleted substring to concatenate together.</p>

<p>We repeatedly make <code>k</code> duplicate removals on <code>s</code> until we no longer can.</p>

<p>Return the final string after all such duplicate removals have been made.</p>

<p>It is guaranteed that the answer is unique.</p>

<pre>
<b>Example 1:</b>
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

<b>Example 2:</b>
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

<b>Example 3:</b>
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

</pre>


``` python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack[1:])
```