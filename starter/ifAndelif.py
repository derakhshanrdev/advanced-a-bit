number = int(input('type a number : '))

if number % 2 == 0:
    if number % 3 == 0:
        print('The number is divisible by 2 and 3!')
    else:
        print('The number is divisible by 2 only!')
elif number % (3 and 5) == 0:
    print('The number id divisible by 3 and 5!')
elif number % 5 == 0:
    print('The number is divisible by 5!')
