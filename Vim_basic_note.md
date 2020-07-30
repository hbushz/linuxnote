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

1. `Ctrl-r` vim paste in command mode / search mode

    ```vim
    Ctrl-r " contents in register noname register
    Ctrl-r a contents in register a
    Ctrl-r + system clipboard
    Ctrl-r % current filename
    Ctrl-r / last search term
    ```

## Vim的buffer, window与tab

### Buffer(缓冲区)

* `:buffers` 会列出所有被载入到内存的缓冲区的列表

* `:ls` 会列出所有被载入到内存的缓冲区的列表

## Vim标记(mark) 与跳转

1. Vim允许你在文本中放置自定义的标记。

1. `ggn` 跳转搜索到文档的第一个匹配 `ggN` 跳转搜索到文档的最后一个匹配

## Vim 调用外部程序

* 利用可视模式选中待计算式, 执行 `:!bc` 调用终端计算器进行计算

