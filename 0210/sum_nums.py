def sum_nums(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum

def sum_nums2(num):
    return sum(range(1,num+1))

def sum_nums3(num):
    nums=[i for i in range(1,num+1)]
    return sum(nums)

def sum_nums4(num):
    if num<=1:
        return num
    else:
        return num+sum_nums4(num-1)

#sum=sum_nums(int(input('正の整数を入力>>')))
#sum=sum_nums2(int(input('正の整数を入力>>')))
#sum=sum_nums3(int(input('正の整数を入力>>')))
sum=sum_nums4(int(input('正の整数を入力>>')))
print(sum)
