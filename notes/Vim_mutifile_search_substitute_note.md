# Vim pattern search

Vim是我最喜欢的编辑器，这里记录了Vim的多文件查找与替换

## 批量文件查找

1. 多文件查找命令`vimgrep`  

* 比如在当前目录下查找带有*abc*字符的后缀为txt的文件，不包括子目录

    ```vim
    :vimgrep /abc/ ./*.txt
    ```

* 如果包含子目录，命令如下：

    ```vim
    :vimgrep /abc/ ./**/*.txt
    ```

* vimgrep 支持正则， 所以注意正则的关键符号， 必要的时候需要转义，转义符`\`


## 批量文件替换

1. 批量文件替换

* 前提熟悉vim的替换命令

    ```vim
    :%s/abc/123/g
    ```

  将当前文件所有匹配的abc字符替换成123，如果没有"g"选项，则替换当前位置。

* 熟悉替换命令行后，接下来说批量替换的步骤：

1. 打开所有需要操作的文件

    ```vim
    :args ./**/*.txt
    ```

2. 对所有打开的文件执行替换并更新到文件

    ```vim
    :argdo %s/abc/123/ge | update
    ```
