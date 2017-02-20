"""
https://leetcode.com/problems/counting-bits/

Given a non negative integer number num.
 For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation 
 and return them as an array.

"""
num = 1
maxn = 10
ans =[0]
while(num <= maxn):
	ans.append(ans[num & num-1] + 1)
	num = num+1
print(ans)
