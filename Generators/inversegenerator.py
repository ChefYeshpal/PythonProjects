def generate_inverses_table(n=20):
    # Print the header row
    print(f"{'x/y':>5}", end="")  # Top-left corner
    for col in range(1, n + 1):
        print(f"{col:>5}", end="")
    print()
    
    # Generate the table rows
    for row in range(1, n + 1):
        print(f"{row:>5}", end="")  # First column with row numbers
        for col in range(1, n + 1):
            result = row / col
            print(f"{result:>5.2f}", end="")  # Format to 2 decimal places
        print()

if __name__ == "__main__":
    generate_inverses_table()

