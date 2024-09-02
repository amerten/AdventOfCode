def decrypt(c, n):
    if c == '-':
        return ' '
    for _ in range(n):
        if c == 'z':
            c = 'a'
        else:
            c = chr(ord(c) + 1)
    return c


for line in open(0).read().splitlines():
    code, id = line[:-11], int(line[-10:-7])
    decrypted_code = "".join([decrypt(c, id) for c in code])
    if 'northpole object storage' == decrypted_code:
        print(id)
        break