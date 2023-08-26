def insert_c(l: list, cmd: str):
    cmdlist = cmd.split()
    num = int(cmdlist[1])
    index = int(cmdlist[2])
    l.insert(num, index)
    return l


def remove_c(l: list, cmd: str):
    cmdlist = cmd.split()
    l.remove(int(cmdlist[1]))
    return l


def append_c(l: list, cmd: str):
    cmdlist = cmd.split()
    l.append(int(cmdlist[1]))
    return l


def run(l: list, cmd: str):
    c = cmd.split()[0]
    if c == "insert":
        l = insert_c(l, cmd)
        print(l)
    elif c == "remove":
        l = remove_c(l, cmd)
    elif c == "append":
        l = append_c(l, cmd)
    elif c == "print":
        print(l)
    elif c == "sort":
        l.sort()
    elif c == "pop":
        l.pop()
    elif c == "reverse":
        l.reverse()
    return l


if __name__ == "__main__":
    N = int(input())
    mylist = []
    for _ in range(N):
        cmd = input()
        mylist = run(mylist, cmd)
