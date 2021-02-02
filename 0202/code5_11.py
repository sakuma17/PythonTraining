def calc_average(scores):
    avg=sum(scores)/len(scores)
    print('平均点は{}点です'.format(avg))
calc_average([10,20,30])
calc_average((10,20,30))
calc_average(range(10,31,10))
calc_average({10,20,30})

print()

def plus(x,y):
    answer=x+y
    return answer

ans=plus(100,200)
print(ans)
