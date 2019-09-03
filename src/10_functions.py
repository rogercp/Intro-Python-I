# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def if_true(num):
	if num % 2 == 0:
		return True
	else:
		return False

print(if_true(5))
print(if_true(4))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def if_true_from_keyboard(num):
	if num % 2 == 0:
		print("Even!")
	else:
		print("Odd!")

if_true_from_keyboard(num)


