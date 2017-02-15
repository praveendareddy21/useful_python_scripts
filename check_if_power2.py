"""
Bitwise manipulation to check if a number is a power of 2
ex: 8,16, 1024 etc


"""

inp = 17

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
	if(inp == 1):
		return True
	elif(inp & (inp-1) == 0) :
		return True
	else:
		return False


print(isPowOf2(inp))
print(isPowerof2(inp))