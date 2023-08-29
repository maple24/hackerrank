import textwrap


def wrap(string: str, max_width: int) -> list:
    # res = textwrap.wrap(string, max_width)
    res = []
    substring = ""
    for i, s in enumerate(string):
        substring += s
        if len(substring) == max_width:
            res.append(substring)
            substring = ""
    if substring:
        res.append(substring)
    return "\n".join(res)


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
