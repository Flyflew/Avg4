from ltp import LTP
import time

start = time.time()  # 紀錄執行時間

ltp = LTP()

segment, hidden = ltp.seg(["這隻程式可以幫我們把網站資料爬下來"])

pos = ltp.pos(hidden)
# ner = ltp.ner(hidden)
# srl = ltp.srl(hidden)
# dep = ltp.dep(hidden)
# sdp = ltp.sdp(hidden)

print(segment)
# print(hidden)
print(pos)


end = time.time()
print(end-start)
