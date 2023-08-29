from collections import Counter

n = int(input())
words = [input() for _ in range(n)]
counter_of_words = Counter(words)
print(len(counter_of_words))
print(" ".join(map(str, counter_of_words.values())))
