# Vim Note

Vim是我最喜欢的编辑器，这里记录了一些Vim的小知识。

## Vim替换(substitute)

Vim替换命令的基本语法是

    :[range]s[ubstitute]/{pattern}/{string}/[flags]
    :[range]s[ubstitute]:{pattern}:{string}:[flags]

其中各字段的意思是
* `range` 表示搜索范围, 默认表示当前行. 常用的标识符
    - `number` an absolute line number. `1,10`表示第1行到第10行
    - `.` the current line. `1,.`表示从第一行到当前行,
    - `$` the last line in the file. `.,$`表示从当前行到最后一行
    - `%` the whole file. The same as `1,$`
    - `backquote t` the position of mark `t`
    - `/pattern/` the next line where text *pattern* matches
    - `?pattern?` the previous line where text *pattern* matches
    - `+`, `-` Each may be followed by `+` or `-` and an optional number
      (default 1). `/begin/+,/end/-` 表示从*begin*到*end*之间的所有行,
      但不包含*begin*与*end*所在的行
* `flags` 表示标志位, 常用的包括
    - `g`(global) 修改本行内的所有匹配, 而不仅仅是第一处匹配
    - `c`(confirm) 替换时需要确认, 可以确认和拒绝每一处替换
        + `y` 确认执行该处替换
        + `n` 取消该处替换
        + `a` 执行所有替换且不再询问
        + `q` 退出而不做任何改动
        + `l`(last) 替换完当前匹配点后退出
    - `i` 忽略`pattern`的大小写
    - `I` 不忽略`pattern`的大小写
    - `n` 不让Vim执行替换操作, 而只是统计和显示本次`substitute`命令匹配的个数
    - `&` 用于指示Vim重用上一次`substitute`命令所用过的标志位


## Vim标记(mark)

Vim允许你在文本中放置自定义的标记。
