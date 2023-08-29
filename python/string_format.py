def print_formatted(number):
    for i in range(1, number + 1):
        pad = len(bin(number)[2:])
        print(
            f"{i: >{pad}} {oct(i)[2:]: >{pad}} {hex(i)[2:].upper(): >{pad}} {bin(i)[2:]: >{pad}}"
        )


print_formatted(63)
