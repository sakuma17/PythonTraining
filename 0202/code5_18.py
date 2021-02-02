def plus_and_minus(a,b):
    return a+b,a-b #タプルとしてリターン

    # return [a+b,a-b] リストでも行ける

next,prev=plus_and_minus(1978,1)
print(next,prev)
