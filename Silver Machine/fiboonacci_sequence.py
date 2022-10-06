def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        print(c)
        a += b
        c = a + b
        print(c)
        b += a

#returns the parameter*2 of fibonacci numbers   
fibonacci(4)

