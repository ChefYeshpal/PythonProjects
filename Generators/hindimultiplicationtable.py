

def generate_table(number):
    print(f"Multiplication table for {number}:\n")
    for i in range(1, 21):
        result = number * i
        print(f"{number} x {i} = {result}, {convert_to_hindi(result)}")

def convert_to_hindi(number):
    hindi_numbers = {
        0: "शून्य", 1: "एक", 2: "दो", 3: "तीन", 4: "चार", 5: "पाँच", 6: "छह", 7: "सात",
        8: "आठ", 9: "नौ", 10: "दस", 11: "ग्यारह", 12: "बारह", 13: "तेरह", 14: "चौदह",
        15: "पंद्रह", 16: "सोलह", 17: "सत्रह", 18: "अठारह", 19: "उन्नीस", 20: "बीस"
    }
    return hindi_numbers.get(number, str(number))

if __name__ == "__main__":
    try:
        number = int(input("Enter a number between 2 to 20: "))
        if number < 2 or number > 20:
            raise ValueError("Number must be between 2 to 20")
        
        generate_table(number)
    except ValueError as ve:
        print("Error:", ve)







