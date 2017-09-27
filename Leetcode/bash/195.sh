:BLOCK

How would you print just the 10th line of a file?

For example, assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:
Line 10

BLOCK

# awk FNR : 各文件分别计数的行号 NR 已经读出的记录数，就是行号，从1开始
# v1
awk 'NR == 10' 195file.txt

# v2
awk 'FNR == 10 {print }'  195file.txt

# sed 10p 打印第十行
# v3
sed -n 10p 195file.txt


# -n Number 从 Number 行位置读取指定文件
# head -1 打印一行 -10 打印10行
# v4
tail -n+10 195file.txt | head -1

# v5
cnt=0
while read line && [ $cnt -le 10 ]; do
    let 'cnt = cnt + 1'
    if [ $cnt -eq 10 ]; then
        echo $line
        exit 0
    fi
done < 195file.txt
