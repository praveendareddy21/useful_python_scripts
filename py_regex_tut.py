import re


str = 'an example word:cat!! word:cat'
match = re.search(r'word:\w\w\w', str)
print (match)
if match:
	print ('found' + match.group() )## 'found word:cat'
else:
	print ('did not find')

"""
Special Char with special Meaning
.   - matches any single character except newline '\n' 

^   - start of string

$   - end of string

* -  0 or more occurances of pattern to left
+  - 1 or more occurances of pattern to left

+ and * are greedy, they tried to use up as much as of string as possible,

For non-greedy behavior, use extension to regular expression where you add a ? at the end, such as .*? or .+?, changing them to be non-greedy. 


? - match 0 or 1 occurrences of the pattern to its left



{
[ ]  - Square brackets can be used to indicate a set of chars, so [abc] matches 'a' or 'b' or 'c'.

\ -  inhibit the "specialness" of a character.  \. matches a period

|
( )



"""