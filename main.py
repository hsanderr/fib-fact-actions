"""
Henrique Sander Lourenco
10802705
"""

# Factorial function (recursive)
def fact(x):
    return x * fact(x - 1) if x > 1 else 1

# Return term of index x of Fibonacci sequence
def fib(x):
    return fib(x - 1) + fib(x - 2) if x > 1 else 1 if x == 1 else 0

# Function to remove new line characters and spaces from list
def isNumber(listItem):
    return True if (listItem != '\n') and (listItem != ' ') else False

# Function to select only numbers which indexes are even
def indexIsEven(listItem):
    return True if (listItem[0] % 2 == 0) else False

# Function to select only numbers which indexes are odd
def indexIsOdd(listItem):
    return True if (listItem[0] % 2 != 0) else False


def test_answer(input, fibonacci, factorial):
    assert fib(input) == fibonacci and fact(input) == factorial

# Read input file
with open('input.dat', 'r') as inputFile:
    inputData = list(inputFile.read())

firstNumber = True
for character in inputData:
    if(isNumber(character)):














# Remove spaces and new line characters from inputData and transform result into a list
filteredInputData = list(filter(isNumber, inputData))

# Cast filteredInputData elements to int type, enumerate result and transform it into a list
numberInputData =  list(enumerate(map(int, filteredInputData)))

# Get numbers which index in enumeration is even, we want to get Fibonacci term with this numbers
evenIndexData = [data[1] for data in list(filter(indexIsEven, numberInputData))]

# Get numbers which index in enumeration is odd, we want to get the factorial of this numbers
oddIndexData = [data[1] for data in list(filter(indexIsOdd, numberInputData))]

# Get Fibonacci terms and transform result into a list
fibonacci = list(map(fib, evenIndexData))

# Get factorial of the numbers and transform result into a list
factorial = list(map(fact, oddIndexData))

# Create output data
outputLines = ["Linha {}:\tfib({}) = {}\tfact({}) = {}\n".format(i, evenIndexData[i], fibonacci[i], oddIndexData[i], factorial[i]) for i in range(len(fibonacci))]
outputData = ''.join(outputLines)

# Write output file
with open('output.dat', 'w') as outputFile:
    outputFile.write(outputData)