"""
A CLOSURE is a function object that remembers values in enclosing scopes 
regardless of whether those scopes are still present in memory.


or wiki

In programming languages, closures (also lexical closures or function closures) are techniques for
implementing lexically scoped name binding in languages with first-class functions. 
Operationally, a closure is a record storing a function[a] together with an environment:[1] a mapping associating each free variable of the function (variables that are used locally, 
ut defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.[b] 

A closure  unlike a plain functionallows the function to access those captured variables through 
the closure's copies of their values or references, even when the function is invoked outside their scope

"""



def generate_power_func(n):
    print "id(n): %X" % id(n)
    def nth_power(x):
        return x**n
    print "id(nth_power): %X" % id(nth_power)
    return nth_power


def startAt(x):
	def incrementBy(y):
		return x + y   ## accessing x even though not in its local scope
	return incrementBy

closure_with_x_as_5 = startAt(5)
closure_with_x_as_1 = startAt(1)

print(closure_with_x_as_5(2))
print("closure content1 : " + str(closure_with_x_as_5.__closure__[0].cell_contents)) 
print("closure content2 : " + str(closure_with_x_as_1.__closure__[0].cell_contents)) 
## here, we see that closure returned by startAt has stored the value of x, outside of startAt's lexical scope



# not working, TODO fix this
def n_value_incrementer(init_val, n_val):
	n = n_val
	i = init_val
	def incrementer():
		i = 0
		i = i + n_val  
		return i
	return incrementer

_2_val_incr = n_value_incrementer(0, 2)

for i in range(5):
	print(_2_val_incr())


"""
python's decorator's are example of closures

"""

def decorate(f):
    def wrapped_function():
        print("Function is being called")
        f()
        print("Function call is finished")
    return wrapped_function

@decorate
def my_function():
    print("Hello world")

my_function()