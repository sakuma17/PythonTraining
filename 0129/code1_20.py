price=input('料金を入力>>')
price=int(price)
#まとめて
number=int(input('人数を入力>>'))
payment=int(price/number)
print('お支払いは'+str(payment)+'円です')
