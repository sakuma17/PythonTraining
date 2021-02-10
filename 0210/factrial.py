def factrial(num):
    if num<=1:
        return num
    else:
        return num*factrial(num-1)

print(factrial(int(input('整数>>'))))
