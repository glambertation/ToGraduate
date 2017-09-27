:<<BLOCK
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

For example, assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:
987-123-4567
(123) 456-7890

BLOCK


# 你可以使用 ^ 和 $ 符号强制一个正则表达式分别匹配一行的开始或结束的位置
# \是转义字符 比如 .\ \{ \(
# 使用-e参数，我们可以查找多个模式
# Read from the file file.txt and output all valid phone numbers to stdout.

# v1
cat file.txt | grep -e '\(^[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}$\)' -e '\(^([0-9]\{3\})[ ][0-9]\{3\}-[0-9]\{4\}$\)'

#v2
cat file.txt | grep -e '^\([0-9]\{3\}-\|([0-9]\{3\})[ ]\)[0-9]\{3\}-[0-9]\{4\}$'

#v3
grep -e '^\([0-9]\{3\}-\|([0-9]\{3\})[ ]\)[0-9]\{3\}-[0-9]\{4\}$' file.txt


# $ awk '/re/ ' log.txt //是匹配模式
# awk ()是括号运算 \(\)是匹配的（） 与 grep相反
#v4
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt

# https://coolshell.cn/articles/9104.html
# sed -E 表示正则匹配 -n表示匹配上输出 配合/p (http://www.grymoire.com/Unix/Sed.html#uh-62k)

#v5
sed -n -E '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt



