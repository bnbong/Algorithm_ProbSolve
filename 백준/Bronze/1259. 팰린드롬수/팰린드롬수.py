while True:
    number = str(input())
    if number == '0':
        break

    r_number = number[::-1]
    if r_number == number:
        print('yes')
    else:
        print('no')
