import hashlib

input = ""
i = 1
while True:
    h = hashlib.md5((input + str(i)).encode()).hexdigest()
    if len(h) > 5 and h[:5] == "00000":
        print(i)
        break
    i += 1
