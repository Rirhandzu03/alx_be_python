
size = int(input("Enter the size of the pattern"))

if size > 0:
    row =0

    while row < size:
        for x in range(size):
            print("*", end="")
        print()
        row += 1

else:
    print("Pleas enter a positive interger. ")

    