for num in range(1,101):
    if num%3 == 0:
        print '%d%s' % (num,": Fizz")
    elif num%5 == 0:
        print '%d%s' % (num,": Buzz")
    else: print '%d' % num
