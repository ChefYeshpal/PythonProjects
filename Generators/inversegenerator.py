



def print_inverses():
    for i in range(2, 21):
        for j in range(1, 21):
            inverse = round(1 / (j * i), 2)
            print(f"{inverse:<8}", end="")
        print()

if __name__ == "__main__":
    print_inverses()





