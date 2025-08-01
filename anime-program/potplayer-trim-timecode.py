#potplayerの拡張、複数字幕をコピーしたときの処理を記載

import re,pyperclip

#orgclip='00:00:38  "Heaven does not create one person above or below another."'.split()
orgclip=pyperclip.paste().split()

newclip=[]
for w in orgclip:
    if re.search(r"^\d+:",w):
        continue;
    elif re.search(r"^\[[\w\s]*\]$",w): 
        continue;
    newclip.append(w)

newstr=" ".join(newclip)
pyperclip.copy(newstr)

