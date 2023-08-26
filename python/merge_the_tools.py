def merge_the_tools(string, k):
    # your code goes here
    n = int(len(string) / k)
    for i in range(n):
        substring = string[i * k : (i + 1) * k]
        u = ""
        for s in substring:
            if s not in u:
                u += s
        print(u)


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
