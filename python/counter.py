"""
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
"""
from collections import Counter

number_of_shoes = 5
list_of_sizes = [1, 2, 3, 4, 5]
number_of_customers = 3
counter_of_sizes = Counter(list_of_sizes)
total = 0
for i in range(number_of_customers):
    order = list(map(int, input().split()))
    order_size = order[0]
    order_price = order[1]
    if order_size in counter_of_sizes and counter_of_sizes[order_size] > 0:
        total += order_price
        counter_of_sizes[order_size] -= 1
print(total)
