# Dictionary

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Smith',
    'age': 20
}

# Use constructor
# person2 = dict(first_name='Haryati', last_name='Astuti')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '0813-6334-2584'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get lenght
print(len(person2))

# List of dict
people = [
    {'name': 'Ahyar', 'age': 19},
    {'name': 'Haryati', 'age': 20}
]

print(people[1]['name'])