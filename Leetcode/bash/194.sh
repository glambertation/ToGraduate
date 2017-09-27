:BLOCK

Given a text file file.txt, transpose its content.

You may assume that each row has the same number of columns and each field is separated by the ' ' character.

For example, if file.txt has the following content:

name age
alice 21
ryan 30
Output the following:

name alice ryan
age 21 30

BLOCK

# v1
# wc -w 按照word统计
# seq 1 10 
# cut -df d分隔符 f区域
# but 超时了
col=`head -n1 194file.txt | wc -w`

for i in `seq 1 $col`
do
    echo `cut -d ' ' -f$i 194file.txt`
    echo "hell"
done
