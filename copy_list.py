animals = ['tiger', 'lion', 'bird']
am = animals.copy()
for a in animals[:]:
    if len(a) > 3:
        animals.append(a)

print(animals)