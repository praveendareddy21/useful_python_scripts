""" 
Python has mulitple inheritance similar to C++ 
while Java  has single inheritance with single tree structure, all objects has object as superclass )

mro- method resolution order followed by python

General rule : Python normally uses a dept-first order when searching inheriting classes
 But when two classes inherit from the same class, Python removes the first mention of that class from mro.

"""
class A(object):
    def dothis(self):
        print('I am from A class')

class B(A):
    pass

class C(object):
    def dothis(self):
        print('I am from C class')

class D(B, C):
    pass

d_instance= D()
d_instance.dothis()
print(D.mro())