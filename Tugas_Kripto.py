s = [x for x in range(256)]

k = 'saputra1'
p = '2072'

k = [ord(x) for x in k]


j = 0
for i in range(len(k)):
    j = (j + s[i] + k[i % len(k)]) % 256
    s[i], s[j] = s[j], s[i]


i, j = 0, 0
ks = []
for i in range(len(p)):
    i = (i+1) % 256
    j = (j+s[i]) % 256
    s[i], s[j] = s[j], s[i]
    t = (s[i]+s[j]) % 256
    keys = (s[t])
    ks.append(keys)
print("keystream:")
print(ks)

chip = []
for i in range(len(p)):
    c = ((ks[i]) ^ ord(p[i]))
    chip.append(c)
print("hasil XOR (desimal chiperteks):")
print(chip)
print("chiperteks:")
for x in chip:
    print(chr(x), end='')