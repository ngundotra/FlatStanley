# Created by ngundotra 12-13-16
# Python tutorial part 1
#
#
# Python is a popular programming language that powers tomorrow's tech
# and is focused on readability and ease of usage.

# Variables
# They come in many types:

#	Boolean (True, False)
is_noah_a_gangster = True
#	Integers (1,-2, 21069)
favorite_number = 97
#	Floats (2.5, -1.2714)
pi = 3.141519
#	Strings ("Hello", "World!", "asdf")
co_presidents = "Noah, Elina"

# Math
# In python 3.5, we do not have to worry about converting between
# integer and float data types. Python handles all the technicalities
# for us.

#	Addition / Subtraction
# 	favoriteNumber now equals 69
favorite_number = favorite_number - 28

# 	Mulitplication / Division
# 	This will output "favoriteNumber is 6.9"
#	str(number) turns the data into a string which Python can print
print("favorite_number is " + str(favorite_number * 0.1))

#	Exponents
#	there are multiple ways to handle exponents, but here is easiest
print("12 squared is " + str(12**2))

# 	Logarithms, Trig functions (radians), and more
#	To handle these, you must learn to use *libraries*
#	These are just folders of code you can reference

# 	this allows us to use both CODE + VARIABLES from Python's math library
# 	we will write our own libraries in the future
import math
# this will print 1.0
print("Take the natural log of e " + str(math.log(math.e)))
# this will print 0.5
print("Take the tangent of " + str(math.tan(math.pi/4)))
# this will print 24
print("Take factorial of 4!: " + str(math.factorial(4)))



