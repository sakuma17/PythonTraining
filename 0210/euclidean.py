def euclidean(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return euclidean(num2,num1%num2)

print(euclidean(1071,1029))
