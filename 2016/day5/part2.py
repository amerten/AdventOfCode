import hashlib

password = {}
index = 0
id = open(0).read().rstrip()
while len(password) < 8:
    md5 = str(hashlib.md5((id + str(index)).encode()).hexdigest())
    if md5[:5] == "00000":
        i, val = md5[5], md5[6]
        if i.isdigit() and 0 <= int(i) < 8 and int(i) not in password:
            password[int(i)] = val
    index += 1
print("".join([v for _,v in sorted(password.items())]))