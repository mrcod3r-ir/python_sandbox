# Python has functions for creating, reading, updating, and deleting files.

# Open a file
from typing import Text


myFile = open('myfile.txt','w') # w mean write mode

# Get some info
print('Name: ',myFile.name)
print('Is Closed : ',myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Pyhton')
myFile.write(' and Javascript')
myFile.close()
print('Is Closed : ',myFile.closed)

# Append to file
myFile = open('myfile.txt','a') # a mean append mode
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt','r+') # r mean read mode
text = myFile.read(100)
print(text)