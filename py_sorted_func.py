"""
sorted(iterable[, cmp[, key[, reverse]]])
Return a new sorted list from the items in iterable.

The optional arguments cmp, key, and reverse 

cmp specifies a custom comparison function of two arguments (iterable elements) which should return a negative, zero or positive number 
depending on whether the first argument is considered smaller than, equal to, or larger than the second argument:
 cmp=lambda x,y: cmp(x.lower(), y.lower()). The default value is None.

key specifies a function of one argument that is used to extract a comparison key from each list element: key=str.lower. 
The default value is None (compare the elements directly).

reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

In general, the key and reverse conversion processes are much faster than specifying an equivalent cmp function. 
This is because cmp is called multiple times for each list element while key and reverse touch each element only once.
 Use functools.cmp_to_key() to convert an old-style cmp function to a key function.

The built-in sorted() function is guaranteed to be stable. 
A sort is stable if it guarantees not to change the relative order of elements that compare equal 
this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).


### works on any iterable, general purpose use

"""
a = [5, 2, 3, 1, 4]  # list
b = sorted(a)
print(b)


student_tuples = [    # sorting tuple objects, with third elem as key
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])


Names  =  ["A12312", "C121", "B0" , "A421"]  # sort w.r.t  first alphabet only

s_names  = sorted(Names, key = lambda name: ord(name[0]))
print(s_names)

cas_ins = sorted("This is a test string from Andrew".split(), key=str.lower) # case insensitive sort
print(cas_ins)

# default order is ascending, for descending set reverse == True

reverse_names  = sorted(Names, key = lambda name: ord(name[0]) , reverse=True )
print(reverse_names)






from operator import itemgetter, attrgetter


sorted(student_tuples, key=itemgetter(2))
#sorted(student_tuples, key=attrgetter('age'))


#multiple sort usage example
sorted(student_tuples, key=itemgetter(1,2))



### sort is guaranteed to be stable

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
data_sorted = sorted(data, key=itemgetter(0))
print(data_sorted)

## sorting on multiple keys
s = sorted(student_tuples, key=itemgetter(1))     # sort on secondary key
data_sorted = sorted(s, key=itemgetter(2), reverse=True)       # now sort on primary key, descending
print(data_sorted)
