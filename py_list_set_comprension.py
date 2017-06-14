


ls_comp = [x for x in range(9)]
print(ls_comp)

set_comp = {x for x in range(9)}
print(set_comp)

ls_generate = (x for x in range(9))

for i in range(5):
    print(ls_generate.next())
print(ls_generate)

#print(len(ls_generate)) results in typeerror has generator has no memory, but generates values on fly


for i in ls_generate:
    print(i)