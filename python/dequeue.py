from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    action = input().split()
    method = getattr(deque, action[0])
    params = action[1] if len(action) > 1 else None
    if params:
        method(d, params)
    else:
        method(d)
print(" ".join(d))
