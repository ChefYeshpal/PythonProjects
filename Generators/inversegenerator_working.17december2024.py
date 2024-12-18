def generate_inverses_table_with_swapped_axes(n=20):
    def print_horizontal_border(n, corner_left, line, cross, corner_right):
        print(corner_left + (line * 6 + cross) * (n) + line * 6 + corner_right)
    
    # Print the top border
    print_horizontal_border(n, "┌", "─", "┬", "┐")
    
    # Print the header row (row numbers 1-20)
    print(f"│{'y/x':^5} │", end="")
    for row in range(1, n + 1):
        print(f"{row:^5} │", end="")
    print()
    
    # Print the header bottom border
    print_horizontal_border(n, "├", "─", "┼", "┤")
    
    # Generate table rows with swapped axes
    for col in range(1, n + 1):
        print(f"│{col:^5} │", end="")  # Column label
        for row in range(1, n + 1):
            result = col / row
            print(f"{result:^5.2f}│", end="")  # Table cell with 2 decimal places
        print()
        
        # Print row borders
        if col != n:
            print_horizontal_border(n, "├", "─", "┼", "┤")
        else:
            print_horizontal_border(n, "└", "─", "┴", "┘")

if __name__ == "__main__":
    generate_inverses_table_with_swapped_axes()

