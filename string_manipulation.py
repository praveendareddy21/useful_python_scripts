

# substitute part of a string in python?
# as string is immutable, can't just do a[7] = 'b'

s ="abcdefghijkl"
s = s[0:-2] + "A" + s[-1:] #replace last but one with A
print(s)   # abcdefghijAl

# General Case substitution

rindex = -2 #Second to the last letter
s = s[0:rindex] + "A" + s[rindex+1:]
print(s)   # abcdefghijAl

