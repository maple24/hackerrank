a = "23hello    23world    lol    2g"
import re


def solve(s: str):
    words = re.split(r"(\W+)", s)
    result = []

    for word in words:
        if word:
            restored_word = word.capitalize()
        result.append(restored_word)

    return "".join(result)


print(solve(a))
