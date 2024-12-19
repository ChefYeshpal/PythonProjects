def generate_inverses_table_with_swapped_axes(n=20):
    def print_horizontal_border(n, corner_left, line, cross, corner_right):
        print(corner_left + (line * 8 + cross) * n + line * 8 + corner_right)
    
    # Print the top border
    print_horizontal_border(n, "+", "-", "-", "+")
    
    # Print the header row (column numbers 1-20)
    print(f"│{'y/x':^8}│", end="")
    for col in range(1, n + 1):
        print(f"{col:^8}│", end="")
    print()
    
    # Print the header bottom border
    print_horizontal_border(n, "+", "-", "-", "+")
    
    # Generate table rows for y/x
    for row in range(1, n + 1):
        print(f"│{row:^8}│", end="")  # Row label
        for col in range(1, n + 1):
            result = row / col  # Swapped to y / x
            print(f"{result:^8.3f}│", end="")  # Fixed-width format for each cell
        print()
        
        # Print row borders
        if row != n:
            print_horizontal_border(n, "+", "-", "-", "+")
        else:
            print_horizontal_border(n, "+", "-", "-", "+")

if __name__ == "__main__":
    generate_inverses_table_with_swapped_axes()

