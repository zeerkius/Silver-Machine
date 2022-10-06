def prime(x):
    n = 1
    zeroc = 0
    for i in range(x-2):
        n += 1
        if x % n == 0:
            zeroc += 1
        if x % n != 0:
            print("False")
    if zeroc > 0:
        print("Not Prime")
        return "Not Prime"
    if zeroc == 0:
        print("Prime")
        return "Prime"
prime(5)
#make a prime number generator