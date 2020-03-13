arr = [70, 30, 20]
for i, j in enumerate(arr):
    print(i, ':', j)

for i in reversed(arr):
    print(i, end=',')

for n in sorted(arr):
    print(n)

v = dict(enumerate(arr))
print(v)
