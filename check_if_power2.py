"""
Bitwise manipulation to check if a number is a power of 2
ex: 8,16, 1024 etc


"""

inp = 16

def isPowOf2(inp) :   # uses left shift  to iterate, then AND's with inp   O(n)  n - bits in inp
#     1010   inp

#     0001   tmp
#     0010   tmp
#     0100   tmp
 	tmp = 1
	count = 0

	while(tmp <= inp):
	    ou = inp & tmp   #  if inp has bit 1 at tmp position, ou = 1

 	    print(str(tmp) +" " +str(ou))
	    if(ou != 0):
	    	count= count+1
	    tmp = tmp << 1
	if (count ==1 ):
		return True
	else:
		return False





def isPowerof2(inp) :   #much efficient  O(1)
#   1000    (8)   &   0111 (7)    == 0
 	if(inp == 1):
		return True
	elif(inp & (inp-1) == 0) :
		return True
	else:
		return False


print(isPowOf2(inp))
print(isPowerof2(inp))

"""
Theory regarding x and x-1
 (x-1) will have all the bits same as x, except for the rightmost 1 in x 
 and all the bits to the right of the rightmost 1. 

Let, x = 4 = (100)2
x - 1 = 3 = (011)2
Let, x = 6 = (110)2 
x - 1 = 5 = (101)2

By AND x and x-1, right most set bit in x is cleared. 
This is used in isPower2  as power of 2 has only one bit set, so  AND with (x-1) will result in 0.

This can be used for counting set bits in a number, by simply counting how many right most set bits can be cleared.


"""

def countSetBits(inp):
	count = 0
	while(inp):
		inp = inp & inp-1
		count = count+1
	return count

print("countSetBits(6) : "+ str(countSetBits(6)))
print("countSetBits(7) : "+ str(countSetBits(7)))
print("countSetBits(8) : "+ str(countSetBits(8)))
