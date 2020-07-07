<h1> 1029. Two City Scheduling --Easy</h1> 
<p>Given a <b>non-empty</b> array of digits representing a non-negative integer, plus one to the integer.</p>
<p>The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.</p>
<p>You may assume the integer does not contain any leading zero, except the number 0 itself.</p>

<pre>
<b>Example 1:</b>
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

<b>Example 2:</b>
Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The array represents the integer 999.
</pre>



``` python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry, i = 1, len(digits)-1
        while carry:
            if i == -1:
                carry, digits = 0, [1]+digits
                break
            carry, digits[i] = divmod(carry+digits[i], 10)
            i -= 1
        return digits
```