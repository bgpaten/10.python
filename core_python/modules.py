# Modules adalah serangakaian fungsi yang akan digunakan di aplikasi

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# import custom module
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()
# print(timestamp)

c = CamelCase()
# print(c.hump('hello there world'))

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')

