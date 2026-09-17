#!/usr/bin/bash

####################################
# recursively convert encrypted pdf files to the unencrypted including those in the current directory
####################################

# 実行ファイル場所と同じディレクトリに在る認証情報の取得
source $(dirname $0)/credential.txt

# カレントディレクトリにあるpdfファイルを取得
for org_pdf in *.pdf; do
    #echo "$org_pdf"
    qpdf --password=$KYUYO_PASSWD --decrypt $org_pdf --replace-input 
done

# 年数ごとに分けられたディレクトリ内のpdfをそれぞれ見ていく
for subdir in */; do
    # カレントディレクトリにあるpdfファイルを取得
    for org_pdf in $subdir/*.pdf; do
        qpdf --password=$KYUYO_PASSWD --decrypt $org_pdf --replace-input 
    done
done
