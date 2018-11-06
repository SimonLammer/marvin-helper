# marvin-helper

In my CS studies, we were to work with a turing-ish machine called "marvin", which accepted rules in the form of `(<f|g><f|g><f|g>,<state>,<value>)->(<new-value>,<movement>,<new-state>)`.

For example: `(ffg,white,0)->(1,move forward,blue)` would mean that if the robot encounters a "ffg" while in the "white" state and on a field with value "0" it will change the field value to "1", switch it's state to "blue" and move a field forward.

The problem with this notation is that I found myself often having to copy rules (i.e. when I wanted the same rule for "fff" and "ffg"), this script lets me (among other things) input the rule with "ff?" and will output both rules.

## Usage:

Run the script with `python3 main.py <file>`.
It will read all lines of the file and print all rules that the lines evaluate to.

### Examples

`(fg?,,0)->(0,nach vorn,grün)`:
```
(fgf,,0)->(0,nach vorn,grün)
(fgg,,0)->(0,nach vorn,grün)
```

`(fgf,[blau,grün],0)->(0,nach vorn,grün)`:
```
(fgf,blau,0)->(0,nach vorn,grün)
(fgf,grün,0)->(0,nach vorn,grün)
```

`(fgf,,[0,1])->(2,nach vorn,grün)`:
```
(fgf,,0)->(2,nach vorn,grün)
(fgf,,1)->(2,nach vorn,grün)
```
**With the last two examples, the current state can be refered to using '%':**

`(fgf,[blau,grün],0)->(0,nach vorn,%)`:
```
(fgf,blau,0)->(0,nach vorn,blau)
(fgf,grün,0)->(0,nach vorn,grün)
```

`(fgf,,[0,1])->(%,nach vorn,grün)`:
```
(fgf,,0)->(0,nach vorn,grün)
(fgf,,1)->(1,nach vorn,grün)
```

**Multiple of these methods can be combined:**

`(f??,[grün,blau],[0,1,2])->(%,nach vorn,rot)`:
```
(fff,grün,0)->(0,nach vorn,rot)
(fff,grün,1)->(1,nach vorn,rot)
(fff,grün,2)->(2,nach vorn,rot)
(fff,blau,0)->(0,nach vorn,rot)
(fff,blau,1)->(1,nach vorn,rot)
(fff,blau,2)->(2,nach vorn,rot)
(ffg,grün,0)->(0,nach vorn,rot)
(ffg,grün,1)->(1,nach vorn,rot)
(ffg,grün,2)->(2,nach vorn,rot)
(ffg,blau,0)->(0,nach vorn,rot)
(ffg,blau,1)->(1,nach vorn,rot)
(ffg,blau,2)->(2,nach vorn,rot)
(fgf,grün,0)->(0,nach vorn,rot)
(fgf,grün,1)->(1,nach vorn,rot)
(fgf,grün,2)->(2,nach vorn,rot)
(fgf,blau,0)->(0,nach vorn,rot)
(fgf,blau,1)->(1,nach vorn,rot)
(fgf,blau,2)->(2,nach vorn,rot)
(fgg,grün,0)->(0,nach vorn,rot)
(fgg,grün,1)->(1,nach vorn,rot)
(fgg,grün,2)->(2,nach vorn,rot)
(fgg,blau,0)->(0,nach vorn,rot)
(fgg,blau,1)->(1,nach vorn,rot)
(fgg,blau,2)->(2,nach vorn,rot)

```

