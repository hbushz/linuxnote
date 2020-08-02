# Vim pattern search substitute and global Note

Vim是我最喜欢的编辑器，这里记录了Vim的正则表达式查找替换与全局命令

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
    - \`t the position of mark `t`
    - `/pattern/` the next line where text *pattern* matches
    - `?pattern?` the previous line where text *pattern* matches
    - `\/` the next line where the previously used search pattern matches
    - `\?` the previous line where the previously used search pattern matches
    - `+`, `-` Each may be followed by `+` or `-` and an optional number
      (default 1). `/begin/+,/end/-` 表示从*begin*到*end*之间的所有行,
      但不包含*begin*与*end*所在的行

* `pattern` 搜索字符串, 支持正则表达式, 详述如下
    - 搜索模式
        + `\M` nomagic模式 字符倾向于表示字符本身, 仅`^`与`$`具有特殊含义
        + `\m` magic模式(缺省) 自动为一些字符赋予特殊含义, 例如: `.`, `*`, `[]`.
        但`+`, `?`, `()`, `{}`还需要转义才具有特殊含义
        + `\v` very magic模式 所有ASCII字符中, 除了数字(0-9), 大小写字母(A-Za-z),
        和下划线(_)外, 都有特殊含义. 适用于大量使用正则表达式的情况
        + `\V` very nomagic模式. 大多数字符都表示自身, 只有反斜杠`\`和表示模式起止
        的分隔符`/`或`?`. 适用于完全不正则表达式的原文搜索

        **注意事项**
        + 由于反斜杠`\`肩负转义序列开始的特殊使命, 上面四种情况下`\`字符本身均需要
        转义`\\`
        + 字母, 数字, 下划线开始的字符序列总表示字符本身;
        而由`\`开始后接字母, 数字, 下划线字符序列, 不管该转义序列有无特殊含义
        (如\d表示数字0-9，\y则仅表示字符y) 在4种选项下均具有相同的写法,
        也始终和正则表达式保持一致
        + 除字母, 数字, 下划线和空格以外的字符（假设其为`$`）则因选项而异:
        若某选项下默认它具有特殊含义, 则`$`直接表示特殊含义,`\$`表示`$`字符本身;
        若某选项下默认它没有特殊含义，则`$`表示`$`字符本身, `\$`表示特殊含义
        (也是`$`在正则表达式中的含义). 当`$`在正则表达式中尚未拥有特殊含义时,
        则所谓特殊含义也因此而变为字符本身
        + 如果某字符用于模式的分隔符(搜索分隔符有`/`和`?`两种，:s :g :v命令则可
        自定义除`\`, `"`, `|`之外的其他单个字符作为模式分隔符，默认为`/`）
        则不管它在*VIM*正则表达式中是否拥有特殊含义, 都无法再用该字符表示正则特殊含义,
        因为它的第一特殊含义已变为更为优先的模式分隔符, 跟在`\`后则表示该字符本身
        (总得让每个选项下每个字符本身能得以表达)。例如: 以`?`开始的搜索,
        `\?`表示问号本身, 再出现直接的`?`表示搜索模式结束, `?`在正测表达式里表示0次
        或1次的量词已无从表达. 使用`/`则不会出现这个问题, 因为正则表达式中`/`的特殊
        含义也是分隔符, 因此推荐总是使用/作为模式分隔符. 只在不想用正则的情况下,
        待匹配模式中常出现`/`字符本身时, 才推荐换用其他分隔符
        + 当使用具有正则表达式意义的元字符括号时, 在需要转义的选项下, 开始括号
        `(`, `[`, `{`必须前加`\`, 而在结束括号中`)`必须前加`\`, `]`必须前不加`\`
        (因为`\]`专门在字符组中表示`]`字符), 而`}`则可在前面加或不加`\`
    - Anchors(定界符)
        + `\<` `\>` word boundary symbols. `s:\<vi\>:VIM:g`将单词*vi*替换为*VIM*
        + `^` `$` the beginning and the end of the line anchors.
          `s:^vi\>:VIM:g` 匹配行首的*vi*单词,
          `s:\<vi$:VIM:g` 匹配行尾的*vi*单词,
          `s:^vi$:VIM:g` 匹配行内仅有的*vi*单词.
        + `\zs` 用来标识匹配的开始
        + `\ze` 用来界定匹配的结束
    - Metacharacters(元字符)
        The power of regexps is in the use of
        metacharacters. Common Vim metacharacters
        + `.` any character except new line
        + `\s` whitespace character
        + `\S` non-whitespace character
        + `\_s` whitespace or a linebreak.
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
        s:\([.!?]\)\s\+\([a-z]\):\1 \u\2:g
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
    :[range]g[lobal][!]/pattern1/,/pattern2/{command}

The global commands work by first scaning through the `range` of the lines
and marking each line where a match occurs. In a second scan the `command`
is executed for each marked line with its line number prepended. If a line
is changed or deleted its mark disappears.

Execute the Ex command (default `print`) on the lines within `range` where
`pattern` matches. If `pattern` is preceded with a `!` -- only where match
does not occur. 各字段的意思是
* `[range]` 指定文本行范围, 默认文档全部行. 常用的标识符详见`substitute`的
    `[range]`
* `[pattern]` 搜索表达式. 常用的标识符详见`substitute`的`[pattern]`
* `[command]` Ex command  
    Ex commands are all commands you are entering on
    the Vim command line like
    - `:co[py]`         复制
    - `:t`              等价于`:copy`
    - `:m[ove]`         移动
    - `:d[elete]`       删除
    - `:w[rite]`        写入
    - `:s[ubstitute]`   替换

    Non-Ex commands (normal mode commands) can be alse executed via
    ```
    :normal non-ex command
    ```

### Examples

* `:g/test/d`   删除所有带*test*的行
* `:g!/test/d`  保留所有带*test*的行
* `:g/^$/d`     删除所有空行
* `:g/^/m 0`    反转文件中的每一行
* `:g/^/m 0`    反转文件中的每一行
* `:g/^/y A`    将所有行复制到寄存器*A*
* `:g/hello/,/world/d`   删除*hello*到*world*之间的行(含)

