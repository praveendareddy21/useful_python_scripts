

"""
1. How to set a bit in the number ‘num’ :
First we left shift ‘1’ to n position via (1<<n)
Then, use ‘OR’ operator to set bit at that position.
’OR’ operator is used because it will set the bit even if the bit is unset previously in binary representation of number ‘num’.

"""
num = 5
print(bin(num))
pos = 2
print("setting 2nd bit from right")
print(bin(num | (1 <<1) ))
print("-----------------")


"""
2. How to unset/clear a bit at n’th position in the number ‘num’ :

Suppose we want to unset a bit at nth position in number ‘num’ then we have to do this with the help of ‘AND’ (&) operator.

First we left shift ‘1’ to n position via (1<<n) than we use bitwise NOT operator ‘~’ to unset this shifted ‘1’.
Now after clearing this left shifted ‘1’ i.e making it to ‘0’ we will ‘AND'(&) with the number ‘num’ that will unset bit at nth position position.

"""

num = 7
print(bin(num))
pos = 2
print("unsetting 2nd bit from right")
print(bin(num & ~(1 <<1) ))
print("-----------------")


"""
Toggle bit at a position

1^1 = 0
0^1 = 1 XOR with 1 will flip that bit

"""

num = 7
print(bin(num))
pos = 2
print("toggling 2nd bit from right")
print(bin(num ^ (1 <<1) ))
print("-----------------")


"""
4. Checking if bit at nth position is set or unset:
Left shift ‘1’ to given position and then ‘AND'(‘&’).

"""

num = 7
print(bin(num))
pos = 2
print("toggling 2nd bit from right")
print(num & (1 <<1) > 0)
print("-----------------")

"""
Inverting bits, bitwise operator ~
"""
num = 7
print(bin(num))

print("Inverting all bits")
print(bin(~num))
print("-----------------")

"""
2's complement, invert all bits, add 1

 used for substraction as
 a - b   ====  a + 2's complement of b

"""

num = 7
print(bin(num))

print("2's complement")
print(bin((~num) + 1))
print(~num + 1)
print("subtraction from 8")
print(8 + ~num + 1)

print("-----------------")

"""
Stripping off the lowest set bit :
In many situations we want to strip off the lowest set bit 
for example in Binary Indexed tree data structure, counting number of set bit in a number.
"""
num = 6
print(bin(num))
print("Stripping off the lowest set bit")
print(bin(num & num -1 ))
print("-----------------")
