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

# Read input file
with open('test_wrong.data', 'r') as inputFile:
    lines = inputFile.readlines()

firstNumber = []
secondNumber = []
thirdNumber = []
for line in lines:
    if ((len(line) > 1) and line != lines[0]):
        splitted = line.split(' ')
        firstNumber.append(int(splitted[0]))
        secondNumber.append(int(splitted[1]))
        thirdNumber.append(int(splitted[2].split('\n')[0]))

def testAnswers():
    for i in range(len(firstNumber)):
        assert fib(firstNumber[i]) == thirdNumber[i] \
            and fact(firstNumber[i]) == secondNumber[i]