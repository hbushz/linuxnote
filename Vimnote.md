# Vim Note

Vim是我最喜欢的编辑器，这里记录了一些Vim的小知识。

## Vim替换(substitute)

Vim替换命令的基本语法是

    :[range]s[ubstitute]/{pattern}/{string}/[flags]
    :[range]s[ubstitute]:{pattern}:{string}:[flags]
    :[range]s[ubstitute]={pattern}={string}=[flags]

其中各字段的意思是
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

* `range` 表示搜索范围, 默认表示当前行. 常用的标识符
    - `number` an absolute line number. `1,10`表示第1行到第10行
    - `.` the current line. `1,.`表示从第一行到当前行,
    - `$` the last line in the file. `.,$`表示从当前行到最后一行
    - `%` the whole file. The same as `1,$`
    - `backquote t` the position of mark `t`
    - `/pattern/` the next line where text *pattern* matches
    - `?pattern?` the previous line where text *pattern* matches
    - `\/` the next line where the previously used search pattern matches
    - `\?` the previous line where the previously used search pattern matches
    - `+`, `-` Each may be followed by `+` or `-` and an optional number
      (default 1). `/begin/+,/end/-` 表示从*begin*到*end*之间的所有行,
      但不包含*begin*与*end*所在的行
* `pattern` 搜索字符串, 支持正则表达式, 详述如下
    - Anchors(定界符)
        + `\<` `\>` word boundary symbols. `s:\<vi\>:VIM:g`将单词*vi*替换为*VIM*
        + `^` `$` the beginning and the end of the line anchors.
          `s:^vi\>:VIM:g` 匹配行首的*vi*单词,
          `s:\<vi$:VIM:g` 匹配行尾的*vi*单词,
          `s:^vi$:VIM:g` 匹配行内仅有的*vi*单词.
    - Metacharacters(元字符)  
        The power of regexps is in the use of
        metacharacters. Common Vim metacharacters
        + `.` any character except new line
        + `\s` whitespace character
        + `\S` non-whitespace character
        + `\d` digit
        + `\D` non-digit
        + `\h` head of word character(a, b,..., z, A, B, ..., Z and _ )
        + `\H` non-head of word character
        + `\p` printable character
        + `\P` like `\p`, but excluding digits
        + `\w` word character
        + `\W` non-word character
        + `\a` alphabetic character
        + `\A` non-alphabetic character
        + `\l` lowercase character
        + `\L` non-lowercase character
        + `\u` uppercase character
        + `\U` non-uppercase character
        + `\x` hex digit
        + `\X` non-hex digit
        + `\o` octal digit
        + `\O` non-octal digit
    - Quantifiers(计数符)  
        Using quantifiers you can set how many
        times certain part of you pattern should repeat
        + `\*`      0或更多  尽可能多
        + `\+`      1或更多  尽可能多
        + `\=`      0或1     尽可能多
        + `\?`      0或1     尽可能多
        + `\{n,m}`  n到m     尽可能多
        + `\{n}`    n        准确
        + `\{n,}`   最少n    尽可能多
        + `\{,m}`   0到m     尽可能多
        + `\{}`     0或更多  尽可能多 (与`*`相同)
        + `\{-n,m}` n到m     尽可能少
        + `\{-n}`   n        准确
        + `\{-n,}`  最少n    尽可能少
        + `\{-,m}`  0到m     尽可能少
        + `\{-}`    0或更多  尽可能少
    - Character ranges
        + `[012345]`    匹配[]内指定的任何一个字符之一
        + `[543210]`等价于`[012345]`    与顺序无关
        + `[0-5]`       允许指定一个范围. `[0-5]`等价于`[012345]`
        + `[a-z]`       匹配指定一个小写字母范围
        + `[a-zA-Z]`    匹配所有小写字母与大字母
        + `[-0-9]`      如果想匹配*-*, 需让其在第一位
        + `[^a-z]`      匹配任一个非小写字母
        + `[a^]`        匹配*a*或*^*. 如果*^*不在第一位, 则失去其特殊作用
    - Grouping and Backreference  
        You can group parts of the pattern expression enclosing them with
        `\(` and `\)` and refer to them inside the replacment pattern by
        their special number `\1, \2, ..., \9`. Typeical example is swapping
        first two words of the line
        ```
        s:\(\w\+\)\(\s\+\)\(\w\+\):\3\2\1:g
        ```
        where `\1` holds the first word, `\2` holds any number of spaces or
        tabs in between and `\3` holds the second word. How to decide what
        number holds what pair of `\(\)`? Just count opening `\(` from the
        left. Replacement part of `substitute` command has its own special
        characters. The common characters
        + `&`   the whole matched pattern
        + `\0`  the whole matched pattern
        + `\1`  the matched pattern in the first pair of `\(\)`
        + `\2`  the matched pattern in the second pair of `\(\)`
        + `\9`  the matched pattern in the ninth pair of `\(\)`
        + `~`   the previous substitute string
        + `\L`  the following characters are made lowercase
        + `\U`  the following characters are made uppercase
        + `\e`  end of `\U` and `\L`
        + `\E`  end of `\U` and `\L`
        + `\r`  split line in two at this point
        + `\l`  next character made lowercase
        + `\u`  next character made uppercase

    Now the full  to correct non-capital words at the beginning of the
    sentences looks like
        ```
        s:\([.!?]\)\s\+\([a-z\):\1 \u\2:g
        ```
    - Alternations  
        Using `\|` you can combine several expressions into one which
        matches any of its components. The first one matched will be used
        ```
        s:\(Date:\|Subject:\)\(\s.*\):\1 \u\2:g
        ```
        The thing to remember about Vim alternation that it is not greedy.
        It won't search for the longest possible match, it will use the
        first that matched. That means that the order of the items in the
        alternation is important.
    - Regexp Operator Precedence  
        As in arithmetic expressions, regular expressions are executed in
        a certain order of precedence. Here the table of precedence,
        from highest to lowest
        + `\(\)`                Precedence 1        grouping
        + `\=, \+, *, \{n-m}`   Precedence 2        quantifiers
        + `abc\t\.\w`           Precedence 3        not containing quantifiers or grouping operators
        + `\|`                  Precedence 4        alternation

举例


## Vim全局命令(global command)

全局命令`:g`功能非常强大, 当想要在整个文件中对匹配的行或不匹配的行进行一些
操作时, 应该第一时间想到用这个命令

    :[range]g[lobal][!]/{pattern}/{command}

Execute the Ex command (default `print`) on the lines within `range` where
`pattern` matches. If `pattern` is preceded with a `!` -- only where match
does not occur. 各字段的意思是
* `[range]` 指定文本行范围, 默认文档全部行. 常用的标识符详见`substitute`的
    `[range]`
* `[pattern]` 搜索表达式. 常用的标识符详见`substitute`的`[pattern]`

## Vim标记(mark)

Vim允许你在文本中放置自定义的标记。

## Vim常用操作点滴

normal模式下`x`删除当前光标下的字符
normal模式下`X`删除当前光标前一个字符
