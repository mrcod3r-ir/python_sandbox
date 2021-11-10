# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules

""" import datetime
today = datetime.date.today() """

""" from datetime import date
today = date.today()

print(today) """

""" import time
print(time.time()) """

""" from time import time
timestamp = time()
print(timestamp) """


# Pip modules

# in cmd type pip install moduleName for installing
# in cmd type pip freeze for showing global modules

""" import camelcase
print(camelcase.CamelCase().hump('hello there world')) """

# Import custom module
import validator
from validator import validate_email

email = 'test@test.com'

if(validate_email(email)):
  print('Email is valid')
else:
  print('Email in bad')