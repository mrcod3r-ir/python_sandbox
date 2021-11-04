# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}

# Use constructor
person2 = dict(first_name='Sara',last_name='Williams')

""" print(person2,type(person)) """

# Get value
""" print(person['first_name'])
print(person.get('last_name')) """

# Add key/value
person['phone'] = '555-652-1234'

# Get dict keys
""" print(person.keys()) """

# Get dict items
""" print(person.items()) """

# Copy dict
person3 = person.copy()
person3['city'] = 'Boston'

# Remove item
del(person3['age'])
person3.pop('last_name')

# Clear
person3.clear()

# Get length
""" print(len(person)) """

# List of dict
people = [
  {'name':'Martina','age':30},
  {'name':'Kevin','age':25}
]

print(people[1]['name'])


""" print(person3) """