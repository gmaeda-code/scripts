#mullvadのkill switchをufwで追加する｡
#ufwはdefaultでdeny(incoming,outgoingともに)なので､wgのinterface向けにpostupで許可､postdownで取り消す｡
#py,python3で実行

import re,glob,os
#カレントディレクトリのconfファイル一覧を取得
file_list=glob.glob('*.conf')

#confファイル1つごとに作業
for file in file_list:
    #1行ずつ作業｡文字を区分けして配列に入れる
    with open(file,encoding='utf-8') as f:
        lines=[s.strip() for s in f.readlines()]
    #Endpointの行だけ､ip addressとportを取り出すため､細かく区分
    endpoint=lines[9].replace(':',' ').replace('=',' ').split()
    #postupとpostdownを追加
    lines.insert(4, f"PostUp = ufw allow out on {file[:-5]} && ufw allow out to {endpoint[1]} port {endpoint[2]}")
    lines.insert(5, f"PostDown = ufw delete allow out on {file[:-5]} && ufw delete allow out to {endpoint[1]} port {endpoint[2]}")
    #配列を文章にまとめる
    sentence=""
    for l in lines:
        l+="\n"
        sentence+=l
    #書き込み
    file=file.replace(".srt","").split("\\")[-1]
    if(os.path.exists("wg-conf-converted") == False):
        os.mkdir("wg-conf-converted")
    with open (f"./wg-conf-converted/{file}",mode="w",encoding="utf-8") as f:
        f.write(sentence)

