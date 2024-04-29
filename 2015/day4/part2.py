import hashlib

input = ""
i = 1
while True:
    h = hashlib.md5((input + str(i)).encode()).hexdigest()
    if len(h) > 6 and h[:6] == "000000":
        print(i)
        break
    i += 1
