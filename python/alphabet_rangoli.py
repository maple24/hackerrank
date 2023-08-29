def print_rangoli(size):
    import string

    # Create a string of lowercase letters
    letters = string.ascii_lowercase

    # Create the lines of the rangoli
    lines = []
    for i in range(size):
        pattern = "-".join(letters[size - 1 : i : -1] + letters[i:size])
        lines.append(pattern.center(4 * size - 3, "-"))

    # Print the rangoli
    print("\n".join(lines[::-1] + lines[1:]))


# Replace 'N' with the desired size
N = int(input("Enter the size of the rangoli: "))
print_rangoli(N)
