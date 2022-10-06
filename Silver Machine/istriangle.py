def istriangle(a,b,c):
    true = 0
    if a + b > c:
        true += 1
    if b + c > a:
        true += 1
    if c + a > b:
        true +=1
    if true == 3:
        return True

input1 = int(input("firstnumber"))
input2 = int(input("secondnumber"))
input3 = int(input("thirdnumber"))
istriangle(input1,input2,input3)