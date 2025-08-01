#alcの拡張検索の文字を削除、ankiアプリで貼り付けるときに使用

import re,pyperclip

orgclip=pyperclip.paste()
newclip = re.sub(r"拡張検索|【\w*】\r\n","",orgclip)
pyperclip.copy(newclip)