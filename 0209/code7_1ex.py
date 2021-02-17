import codecs

"""
file=codecs.open('diary.txt','a','utf-8')
text='こんにちは'
file.write(text)
file.close()
"""

text=input('書き込む内容>>')
with codecs.open('diary.txt','a','utf-8') as file:
    file.write(text+'\n')
