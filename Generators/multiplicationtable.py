



def print_multiplication_table(number):
    for i in range(1, 21):
        result = number * i
        print(result)

if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        print_multiplication_table(number)
    except ValueError:
        print("Please enter a valid number.")




