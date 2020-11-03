# abc 110 c - String Transformation
# ref https://img.atcoder.jp/abc110/editorial.pdf
from collections import Counter
s = input()
t = input()
sd = {}
td = {}
for i in range(len(s)):
    if s[i] not in sd:
        sd[s[i]] = t[i]
    if t[i] not in td:
        td[t[i]] = s[i]
    if sd[s[i]] != t[i] or td[t[i]] != s[i]:
        print('No')
        exit()
print('Yes')

'''note
i番目の文字を見る。i番目の文字に対応する変換先が決まっていなかったら、
それを辞書に入れていく。
それができないとき、つまりすでに別の文字で埋まっているときに、
変換が出来ないということになる。
'''