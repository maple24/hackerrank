def door_mat(row, col) -> str:
    for r in range(row):
        if r == (row - 1) / 2:
            center = "WELCOME"
        else:
            if r > row / 2:
                r = row - r - 1
            center = (2 * r + 1) * (".|.")
        lpad = rpad = int((col - len(center)) / 2) * "-"
        res = lpad + center + rpad
        print(res)


if __name__ == "__main__":
    row, col = input().split()
    door_mat(int(row), int(col))
