# Vim Note

Vim是我最喜欢的编辑器，这里记录了一些Vim的小知识。

## Vim替换(substitute)

Vim替换命令的基本语法是

    :[range]s[ubstitute]/{pattern}/{string}/[flags]

其中各字段的意思是
* `range` 表示搜索范围, 默认表示当前行. `1,10`表示第1行到第10行, `1,.`表示
从第一行到当前行, `.,$`表示从当前行到最后一行, `%`表示所有行(`1,$`)
* `flags` 表示标志位, 常用的包括
    - `g`
    - `c`
    - `n`
    - `e`


## Vim标记(mark)

Vim允许你在文本中放置自定义的标记。
