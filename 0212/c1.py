class GameCharacter:
    #self部分は任意だが慣習的にselfが用いられている
    def __init__(self,job,life):
        self.job=job
        self.life=life
    def info(self):
        print(self.job)
        print(self.life)

warrior=GameCharacter('戦士',100)
#ctrl+vでビジュアルモード→jで移動→shift+i→#
#まとめてコメントアウト(文頭に#を挿入)できる
#print(warrior.job)
#print(warrior.life)
warrior.info()
