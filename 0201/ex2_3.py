setA={'カメラ','散歩','ゲーム','映画','料理'}
setB={'料理','映画','手芸','ショッピング','昼寝'}
input('心の準備ができたらEnterキーを押してください')
result=(len(setA&setB)/len(setA|setB))*100
print('二人の相性は',result,'%です')
