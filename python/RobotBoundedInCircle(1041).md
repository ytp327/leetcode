<h1> 1041. Robot Bounded In Circle --Medium</h1> 
<p>On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:</p>
<p>"G": go straight 1 unit;<br>
"L": turn 90 degrees to the left;<br>
"R": turn 90 degress to the right.</p>
<p>The robot performs the instructions given in order, and repeats them forever.</p>
<p>Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.</p>

<pre>
<b>Example 1:</b>
Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
<b>Example 2:</b>
Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
<b>Example 3:</b>
Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
</pre>


``` python
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        # up [0, 1], left [-1, 0], down [0, -1], right [1, 0]
        for ins in instructions:
            if ins == 'G': x, y = x + dx, y + dy
            elif ins == 'L': dx, dy = -dy, dx
            elif ins == 'R': dx, dy = dy, -dx
        if [x, y] == [0, 0] or [dx, dy] != [0, 1]: return True
        return False
```