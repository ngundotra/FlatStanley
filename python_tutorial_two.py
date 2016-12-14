# Created by ngundotra 12-13-16
# Python tutorial part 2
#
# Python is known for its flexbile arrays, called lists,
# and its powerful loops

# Here is the most used of arrays:
#	Lists
#		These are indexed from 0. Meaning the first element is 
#		numbered 0, and the last element is numbered n-1. 
#		Where n is the length of the list.
#
#		List elements are accessed using square bracket notation
#		co_presidents[0] = 'Noah'
co_presidents = ['Noah', 'Elina']
print(co_presidents[0] + " is amazing!") # co_presidents[0] is Noah
print(co_presidents[1] + "... yikes––no comment")
# 	Lists can have lists within them
cs_club = ['members', 'vice president', co_presidents]
# '/n' is the ASCII code for a new line. Google ASCII codes for more info
print("/n" + cs_club[0] + " and " + cs_club[1] + " are more amazing!!")
# 	cs_club[2] returns co_presidents, which can then be handled
# 	cs_club[2][0] returns 'Noah'
print(cs_club[2][0] + " is a decent python coder")

# Here is a great way to access lists:
#	for loops
#		These pieces of code will run *for* a specified amount of time.
#		They will repeat the code within the block during that time.
#		Each time they run is called an *iteration*.

print("Here is our first for loop! Printing numbers 0-9")
for i in range(10):
	print(i)

#	What makes Python for loops special is that they can loop through
#	arrays very easily.
print("Here is a more advanced loop")
for name in co_presidents
	print("In CS Club, we have (a) " + name)

# As we go forward this coming semester, we will use more advanced
# versions of these tools
