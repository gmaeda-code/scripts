#funimation等から入手したsrtファイルを整形し、読める形のtxtファイルに変更する
# 本みたいにしたかったのだったかな?
#py、python3で実行

import re,glob,os
#カレントディレクトリのsrtファイル一覧を取得
#file_list=glob.glob('*.srt')
file_list=glob.glob('**/*.srt',recursive=True)

#srtファイル1つごとに作業
for file in file_list:
    #空白行は除去して配列に入れる（意味あるか？）
    with open(file,encoding='utf-8') as f:
        l_strip=[s.strip() for s in f.readlines()]

    lines=[]
    for l in l_strip:
        if re.search(r"^\d+$",l):   #場面番号は除外
            continue
        elif re.search(r"^\d+:",l): #場面のタイムコードは除外
            continue
        else:
            if l=="":   #空白が含まれるので除外
                continue
            elif re.search(r"^\[[\w\s]*\]$",l): #会話主等[]のみの場合
                l="\n\n"+l+"\n"
            elif re.search(r"^\[\w*\]",l):  ##会話主等[]に文が続く場合
                l=l.split("]")
                l[0]="\n\n"+l[0]+"]"+"\n"
                l[1]=l[1].strip()+" "
                lines.append(l[0])
                lines.append(l[1])
                continue
            elif re.search(r"[\.\?\:]$",l): #文末等では改行
                l=l+"\n"
            else:
                l=l+" "
            lines.append(l)
    #整形した分の配列を平文にする
    sentence=""
    for l in lines:
        sentence+=l
    #書き込み
    file=file.replace(".srt","").split("\\")[-1]
    if(os.path.exists("txt_script") == False):
        os.mkdir("txt_script")
    with open (f"txt_script\\{file}.txt",mode="w",encoding="utf-8") as f:
        f.write(sentence)
