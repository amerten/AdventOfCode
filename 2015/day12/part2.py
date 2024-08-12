import json


def my_sum(j):
    if type(j) == dict:
        if "red" in j.keys() or "red" in j.values():
            return 0
        t = 0
        for k in j:
            t += my_sum(j[k])
        return t
    elif type(j) == list:
        return sum(map(my_sum, j))
    elif type(j) == int:
        return int(j)
    else:
        return 0


print(my_sum(json.loads(open(0).read().strip())))
