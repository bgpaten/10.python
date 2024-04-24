# JSON

import json

# Sample JSON
userJSON = '{"first_name": "Haryati", "last_name": "Astuti", "age": 20}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

# dict to JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)