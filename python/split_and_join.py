def split_and_join(line):
    # write your code here
    newline = line.split(" ")
    return "-".join(newline)


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
