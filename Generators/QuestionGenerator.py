#the purpose of this program is to increase the basic mathematical calc
#the user will input a value, if the value is incorrect, the program will loop until the user inputs the correct value
#it will generate numbers which will be multiplied/divided/added/subtracted on random
#The maximum number count should be 4
#Date Created: 1 september 2023
#date last modified:

######################################################################################


import random

def generate_random_number(minimum, maximum):
    return random.randint(minimum, maximum)

#for value a
min_value = 1
max_value = 100
a = generate_random_number(min_value, max_value)
def generate_random_number(minimum, maximum):
    return random.randint(minimum, maximum)

#for value b
min_value = 1
max_value = 100
b = generate_random_number(min_value, max_value)
def generate_random_number(minimum, maximum):
    return random.randint(minimum, maximum)

#for value c
min_value = 1
max_value = 100
c = generate_random_number(min_value, max_value)
def generate_random_number(minimum, maximum):
    return random.randint(minimum, maximum)

#for value d
min_value = 1
max_value = 100
d = generate_random_number(min_value, max_value)


#for generating symbols of + - * / between the operations


def perform_random_operations(a, b, c, d):
    operations = ['+', '-', '*', '/']

    a_operation = random.choice(operations)
    b_operation = random.choice(operations)
    c_operation = random.choice(operations)
    d_operation = random.choice(operations)

    # Display the operations as a mathematical expression
    expression = f"{a} {a_operation} {b} {b_operation} {c} {c_operation} {d}"
    print(f"Performing operations: {expression}")
    
    realans = eval(expression)  # Use eval() to compute the result from the expression
    
    return result


result = str(perform_random_operations(a, b, c, d))
print(result)


while True:
    usrans = input("what is your answer? ")

    #to make answer be accepted upto 2 decimal places
    try:
        usra = float(usrans)
        if round(usra, 2) == result:
            print("your answer is indeed correct (" + {result} + ")")
            break
        else:
            print("Incorrect value, try again: ")
    except ValueError:
        print("Invalid Input, enter a number: ")



#for correct answer






