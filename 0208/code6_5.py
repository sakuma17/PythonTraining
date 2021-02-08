class Hero:
    name='松田'
    hp=100
    def sleep(self,hours):
        print('{}は{}時間寝た!'.format(self.name,hours))
        self.hp+=hours

print('スッキリファンタジーXII ～金色の理想郷～')
h=Hero()
n=int((input('何時間寝ますか?>>')))
h.sleep(n)
print('{}の現在のHPは{}です'.format(h.name,h.hp))
