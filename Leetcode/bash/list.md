* file edit
    * cat
    * sort
        * -r 倒序
    * uniq
    * tr
        * -s 缩减连续重复的字符成指定的单个字符
        * tr ' ' '\n' 把‘’ 替换成 \n 
    * awk
    * tail
        * -f 从尾部读
        * -n + 行数 读第x行 
    * head
        * -n 从头输入第n行
    * sed
* 正则匹配
    * grep
        * -e 多个任务匹配
    * awk
        * '{ print $1, $2}'
        * 内建函数
            * NF 已读行数
            * FNR 行数
    * sed
        * -n 只输出匹配的结果
        * -E 正则匹配
* 逻辑运算
    * le 小于等于; eq 等于
    * 变量 cnt=0 没有空格
    * let
* 流程逻辑
    * while ;do ;done
    * if ;then; if
* IO
    * stdin < file.txt
    * stdout > out.txt 
* pipe
    * |

