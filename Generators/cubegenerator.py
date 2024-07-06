

def cube_numbers(start, end):
    for i in range(start, end + 1):
        print(f"{i**3}")

if __name__ == "__main__":
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    cube_numbers(start, end)





