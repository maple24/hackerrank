# records = [
#     {
#         "name": "chi",
#         "score": 20.0
#     },
#     {
#         "name": "beta",
#         "score": 50.0
#     },
#     {
#         "name": "alpha",
#         "score": 50.0
#     },
#     {
#         "name": "gamma",
#         "score": 60.0
#     },
# ]
# grades = [20.0, 50.0, 50.0, 60.0]
if __name__ == "__main__":
    records = []
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append({"name": name, "score": score})
        grades.append(score)
    grades = list(set(grades))
    grades.sort()
    second_lowest = grades[1]
    out = []
    for r in records:
        if r.get("score") == second_lowest:
            out.append(r.get("name"))
    out.sort()
    [print(n) for n in out]
