"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

with open('foo.txt', 'r') as f:
	contents = f.read()
	print(contents)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('bar.txt', 'w') as new_file:
	new_file.write("this\nis my\nnew file")
new_file.close()

with open('bar.txt', 'r') as new_file:
	contents = new_file.read()
	print(contents)
new_file.close()


