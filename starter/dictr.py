dct = {}
print(dct)
dct[1] = 'ali'  # output: {1: 'ali'}
print(dct)
dct[2] = 24
print(dct)  # output: {1: 'ali', 2: 24}
h = dct.keys()
print(h)  # output: dict_keys([1, 2])
dct = {1: 'ali', 2: 24, 3: '54'}
print(dct)
print(dct.fromkeys('a', 's'))
print(dct)