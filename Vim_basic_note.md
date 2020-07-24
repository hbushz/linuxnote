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

## Vim的buffer, window与tab

### Buffer(缓冲区)

* `ls` 会列出所有被载入到内存的缓冲区的列表

## Vim标记(mark)

Vim允许你在文本中放置自定义的标记。

