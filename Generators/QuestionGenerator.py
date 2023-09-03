#the purpose of this program is to increase the basic mathematical calc
#the user will input a value, if the value is incorrect, the program will loop until the user inputs the correct value
#it will generate numbers which will be multiplied/divided/added/subtracted on random
#The maximum number count should be 4

#Date Created: 1 september 2023

#log:
#2023-09-03 13:54:02 : made code simpler, was having isses with realans (solved now)

#to do
#1 make it say "try to do upto 2 decimal places" if usrans is correct but they have not written decimal places
#2


#date last modified: 2023-09-03 13:57:27

######################################################################################


import random

def generate_random_number(minimum, maximum):
    return random.randint(minimum, maximum)

#to generate random values for a b c d
minvalue = 1
maxvalue = 100
a = generate_random_number(minvalue, maxvalue)
b = generate_random_number(minvalue, maxvalue)
c = generate_random_number(minvalue, maxvalue)
d = generate_random_number(minvalue, maxvalue)

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
    
    result = eval(expression)  # Use eval() to compute the result from the expression
    
    return result


result = perform_random_operations(a, b, c, d)
print(result)

#to ask user the question
while True:
    usrans = input("what is your answer? ")

    #to make answer be accepted upto 2 decimal places
    try:
        usrfloat = float(usrans)
        epsilon = 0.01
        if abs(usrfloat - result) < epsilon:
            print("your answer is indeed correct")
            print(result)
            break
        else:
            print("Incorrect value, try again. ")
    except ValueError:
        print("Invalid Input, enter a number: ")



#for correct answer






