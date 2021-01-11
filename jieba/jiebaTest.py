from sys import flags
import jieba
import jieba.posseg as pseg
import time

# sent = '明明是數字鎖，卻需要畫圖形，滑動解鎖竟然是將手機翻轉90度，圖形鎖則變成射擊到螢幕右上角。'
# wordlist = jieba.cut(sent, cut_all=True)
# print(" | ".join(wordlist))

# wordlist = jieba.cut(sent)
# print(" | ".join(wordlist))

# wordlist = jieba.cut_for_search(sent)
# print(" | ".join(wordlist))

start = time.time()

# words = pseg.cut("這隻程式可以幫我們把網站資料爬下來")  # jieba默认模式

jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持

words = pseg.cut("這隻程式可以幫我們把網站資料爬下來", use_paddle=True)  # paddle模式

for word, flag in words:
    print('%s %s' % (word, flag))

# print(words)
# print(flags)

end = time.time()
print(end-start)
