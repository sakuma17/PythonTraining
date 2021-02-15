print('しりとりスタート!'),print('しりとり')

word_set=set()
count=0
word='しりとり'
while True:
    count+=1
    print(f'{count}ターン目です。')
    last_char=word[len(word)-1:]
    word=input(f'[{last_char}]で始まる平仮名を入れてください:')
    if word[len(word)-1:]=='ん':
        print('これは[ん]で終わる単語です。あなたの負けです。')
        break
    if word[0:1]!=last_char:
        print('最初の文字が間違っています。あなたの負けです。')
        break
    if word in word_set:
        print('この単語は既に使われています。あなたの負けです。')
        break
    else:
        word_set.add(word)
