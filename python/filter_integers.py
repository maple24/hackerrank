def filter_integers_by_group(group_size: int, data: list) -> list:
    result = []
    current_group = []

    for item in data:
        if isinstance(item, int) and not isinstance(item, bool):
            current_group.append(item)
            if len(current_group) == group_size:
                result.append(current_group)
                current_group = []

    if current_group:
        result.append(current_group)

    return result


group_size = 3
# data = [1, 2, 3, True, "hello", 1]
data = [1, 2, True]
# data = [1, 2, True, 3, 5, 5, "string1", 5.6, 8, 6, 3, 2.1, "string2"]
filtered_data = filter_integers_by_group(group_size, data)
print(filtered_data)  # Output: [[1, 2, 3], [1]]
