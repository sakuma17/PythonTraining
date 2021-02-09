import codecs
text=input('何を記録しますか?>>')
with open('diary.txt','a','utf-8') as file:
    file.write(text+'\n')
"""
file=open('diary.txt','a')
file.write(text+'\n')
file.close()
"""
