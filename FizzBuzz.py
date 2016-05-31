# prints intergers i such that,  1<=i<=100 
# replaces intergers i such that i%3==0 with Fizz and i%5==0 with Buzz
for num in range(1,101):
    if num%3 == 0:
        print '%d%s' % (num,": Fizz")
    elif num%5 == 0:
        print '%d%s' % (num,": Buzz")
    else: print '%d' % num
