# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate
# print('Hello, I am '+name+' and my age is '+str(age))

# String Formatting

# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name,age=age))

# F-String (3.6+)
# print(f'My name is {name} and I am {age}')

# String Methods
s = 'Hello World'

# Capitalize string
""" print(s.capitalize()) """

# Make all upper or lower case
""" print(s.upper())
print(s.lower()) """

# Swap case
""" print(s.swapcase()) """

# Get length
""" print(len(s)) """

# Replace
""" print(s.replace('Hello','every on in')) """

# Count
sub = 'l'
""" print(s.count(sub)) """

# Start with && End with
""" print(s.startswith('Hello'))
print(s.endswith('ld')) """

# Split
""" print(s.split()) """

# Find Position
""" print(s.find('W')) """

# ss all alphanumeric
""" print(s.isalnum()) """

# is all alphabetic
""" print(s.isalpha()) """

# is all numeric
""" print(s.isnumeric()) """