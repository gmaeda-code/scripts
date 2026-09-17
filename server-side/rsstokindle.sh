#!/bin/bash
# ref
# https://netbuffalo.doorblog.jp/archives/4559916.html
#
#0 7 * * * /path/to/sendtokindle.sh my.recipe > /dev/null 2>&1
#SEND_HOME=$(cd $(dirname $0) && pwd)
#########################################################
# cronの実行環境のデフォルトは"~/"

#mail configuration
source ~/bin/conf.txt

#working_directory
#recipe_dir="/home/mg/.config/calibre/custom_recipes/test-command_1416.recipe"
recipe_dir="/home/mg/.config/calibre/custom_recipes/news_1111.recipe"

output_dir="/home/mg/Downloads"

# file name. ex. RSSFeeds_201308220730
output_file_b="RSS_`date +'%Y-%m-%d_%H-%M'`.mobi"
output_file="RSS_`date +'%Y-%m-%d_%H-%M'`.epub"

# kindle, kindle_dx, kindle_fire, kindle_pw
conv_opts="--output-profile=kindle"


##################### run programs#########################################
echo "starting ebook-convert ..."
#ebook-convert $SEND_HOME/$1 $SEND_HOME/$MOBI $CONV_OPTS
ebook-convert $recipe_dir $output_dir/$output_file_b $conv_opts
ebook-convert $output_dir/$output_file_b $output_dir/$output_file $conv_opts


# send email to kindle
if [ $? -eq 0 -a -f $output_dir/$output_file ];
then
    echo "starting ebook-smtp ..."
    calibre-smtp -a $output_dir/$output_file \
    --relay disroot.org --port 587 -e TLS \
    -u $MAIL_USER -p $MAIL_PASSWD $MAIL_ADDR $KINDLE_ADDR \
    -s 'RSS Feeds to Kindle' ''
    if [ $? -eq 0 ];
        then
        echo "SUCCESS: send to kindle $output_file" >> ~/bin/dbg-msg.txt
        rm -f $output_dir/$output_file_b
        rm -f $output_dir/$output_file
    else
        echo "ERROR: calibre-smtp failed. NAME: $output_file"  >> ~/bin/dbg-msg.txt
    fi
else
    echo "ERROR: ebook-convert failed. NAME: $output_file"  >> ~/bin/dbg-msg.txt
fi

