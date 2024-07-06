
def square_numbers(lower, upper):
    squares = {}
    for num in range(lower, upper + 1):
        squares[num] = num ** 2
    return squares

if __name__ == "__main__":
    try:
        lower = int(input("Enter the lower number: "))
        upper = int(input("Enter the upper number: "))
        
        if lower > upper:
            raise ValueError("Lower number cannot be greater than upper number")

        result = square_numbers(lower, upper)
        
        print("Squares of the numbers:")
        for num, square in result.items():
            print(f"{square}")
    except ValueError as ve:
        print("Error:", ve)



