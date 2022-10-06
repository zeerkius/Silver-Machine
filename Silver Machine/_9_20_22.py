def primecounter(x):
 n = x - 1
 xeros = 0
 for i in range(x-2):
    if x % n == 0:
       xeros += 1
    elif x % n != 0:
       xeros = xeros
    n -= 1
 if xeros == 0:
        print("Prime " + str(x))
 if xeros != 0:
     print("Not Prime " + str(x))
 if x == 1:
     quit()
 primecounter(x-1)
#
testnumber = int(input("How many numbers would you like to test?"))
primecounter(testnumber)
