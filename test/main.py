import jieba
import os
import jieba.analyse


f = open('C:/Users/黃智遠/Desktop/test/main1/◎徐志摩 一條金色的光痕.txt','r', encoding='utf-8')
words = f.read()
words = jieba.posseg.cut(words)
for word, flag in words:
    f = open('C:/Users/黃智遠/Desktop/test/2.txt', 'wt', encoding='utf-8')
    print(f'{word} {flag}')
    f.write(f'{word} {flag} \n')
f.close()


