images = [ ['a','b'], ['a','c']]
d = {}
for i in images:
    for j in i:
        if j in d :
            d[j] = d[j] +1
        else:
            d[j] = 1

print (d)
l = []
for i in d.keys():
    l.append( (d[i], i))
print(l)

n = sorted(l, reverse = True)
print(n)
