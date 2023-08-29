"""
The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet.
d = defaultdict(str)
print(d["p"])
>>> the default value would be an empty srting
"""
from collections import defaultdict

d = defaultdict(list)
