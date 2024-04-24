# Function

# Create function
def sayHello(name='sam'):
    print(f'hello {name}')

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

# print(getSum(3, 4))

# num = getSum(3, 4)
# print(num)

# A lambda

getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 3))