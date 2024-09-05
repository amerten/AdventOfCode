import hashlib

password = ""
index = 0
id = open(0).read().rstrip()
while len(password) < 8:
    md5 = str(hashlib.md5((id + str(index)).encode()).hexdigest())
    if md5[:5] == "00000":
        password += md5[5]
    index += 1
print(password)