name='松田'
def change_name():
    global name #宣言と代入は別々に
    name='浅木'
    print(name)

def hello():
    """
    hello()内でしか使えない
    def change_name():
        name='浅木'
        print(name)
    """
    print('こんにちは'+name+'さん')

change_name()
hello()
