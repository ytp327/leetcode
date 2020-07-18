<h1> 65. Valid Number --Hard</h1> 
<p>Validate if a given string can be interpreted as a decimal number.</p>
<p><b>Note:</b> It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:
<ul><li>Numbers 0-9</li>
<li>Exponent - "e"</li>
<li>Positive/negative sign - "+"/"-"</li>
<li>Decimal point - "."</li></ul>
Of course, the context of these characters also matters in the input.</p>

<pre>
<b>Examples:</b>
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
</pre>

Regular expression is really important in interviews and solving this kind problems.
We need to match the whole string, so in the pattern we start with <code>^</code> (beginning symbol of the string) and end with <code>$</code> (ending symbol of the string). <code>\s*</code> matches zero or more spaces. <code>[\+|\-]?</code> matches nothing or one <code>-</code> or one <code>+</code>. A=<code>\.\d+</code> matches decimal point with digits like <code>.121</code>. And B=<code> \d+(\.\d*)?</code> matches integer or integer following decimal point following digits. We should only pick one of A and B to match the string so use (A|B) to wrap them. The string may also follow by exponential form. We use <code>(e[\+|\-]?\d+)?</code> to match exponential form.
```python
import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return re.match(r'^\s*[\+|\-]?(\.\d+|\d+(\.\d*)?)(e[\+|\-]?\d+)?\s*$', s)
```