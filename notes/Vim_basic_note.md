# Vim Note

Vim是我最喜欢的编辑器，这里记录了一些Vim的小知识。

## Vim常用操作点滴

1. *normal* 模式下 `x` 删除当前光标下的字符

1. *normal* 模式下 `X` 删除当前光标前一个字符

1. *insert-Normal-mode* 在 insert 模式下执行 normal 模式的命令

    ```vim
    Ctrl-o zz " center your position while tpyping
    Ctrl-o dfx " delete to 'x'
    ```

1. The `~` character can be used to  switch the case of  the character under the
    cursor. Actually, it can act like an operator

    ```vim
    g~w " to switch the case of next word
    g~} " to switch the case of the next paragraph
    g~~ " to switch the case of the entire line
    ```

1. Vim has rot13 encoding built-in with `g?` It acts like an operator

    ```vim
    g?iw " to switch the case of next word
    g?} " to switch the case of the next paragraph
    g?? " to encode the entire line
    ```

## Vim 寄存器

1. `Ctrl-r` vim paste in command mode / search mode

    ```vim
    Ctrl-r " " contents in register noname register
    Ctrl-r a " contents in register a
    Ctrl-r + " system clipboard
    Ctrl-r % " current filename
    Ctrl-r / " last search term
    Ctrl-r Ctr-w " current word
    ```

1. `:put +` 可以将`+`寄存器中的内容置于当前行的下一行

1. `=` 表达示寄存器

    表达式寄存器允许我们做一些运算, 并把运算结果直接插入到文档中

    ```vim
    <C-r>=6*35<CR>
    ```

    利用表达式寄存器与vim脚本插入行号

    ```vim
    :let i=1<Enter>
    gg
    qa
    I<C-r>=i<Enter><C-[>
    :let i+=1<Enter>
    q
    jVG:normal @a<Enter>
    ```

1. 复制一个寄存器到另一个寄存器, 如 register a to register z

    ```vim
    :let @a = @z ` register a to register z
    :let @/ = "" ` 置空查找寄存器
    ```

## Vim的buffer, window与tab

### Buffer(缓冲区)

* `:buffers` 会列出所有被载入到内存的缓冲区的列表

* `:ls` 会列出所有被载入到内存的缓冲区的列表

## Vim标记(mark) 与跳转

1. Vim会自动进行位置标记

    * &apos; 当前文件中上次跳转动作之前的位置
    * `.` 上次修改的地方
    * `^` 上次插入的地方
    * `<` 上次选择区域的起始位置
    * `>` 上次选择区域的结束位置
    * `[` 上次修改或复制的起始位置
    * `]` 上次修改或复制的结束位置

    你可以用 &apos;+ 上述标记进行跳转

1. Vim允许你在文本中放置自定义的标记

1. `ggn` 跳转搜索到文档的第一个匹配 `ggN` 跳转搜索到文档的最后一个匹配

## Vim 调用外部程序

* 利用可视模式选中待计算式, 执行 `:!bc` 调用终端计算器进行计算

