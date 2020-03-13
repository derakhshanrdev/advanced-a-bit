lst = [11, 20, 35, 66]
a, b, c, d = lst
print(a, b, c, d, sep='-')  # sep function without loop use for stop row

student = ['Tom', 80, 90, 64, 32, 20]
name, *marks, age = student
print(*marks)

y = (1, 'two', 3, ('five', 'six', 'seven'))
a, *b, (*c, d) = y
print(b)
print(c)


