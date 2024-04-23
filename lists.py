# List

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apells', 'Oranges', 'Grapes', 'Pears']

# Use a Constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a Value
print(fruits[1])

# Get lenght
print(len(fruits))

# Append to list
fruits.append('Manggos')

# Remove from list
fruits.remove('Grapes')

# insert into position
fruits.insert(2, 'Duren')

# Change value
fruits[0] = 'Semangka'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)