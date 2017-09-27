# Read from the file words.txt and output the word frequency list to stdout.
:<<BLOCK
Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.
For example, assume that words.txt has the following content:

the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:
the 4
is 3
sunny 2
day 1
BLOCK

# v1

cat words.txt | tr -s ' ' '\n'| sort | uniq -c | sort -r | awk '{ print $2, $1}'

# tr 指令从标准输入设备读取数据，经过字符串转译后，将结果输出到标准输出设备。

