# Git Note

这里记录了我在 Git 使用中一些非常重要但又容易忘记的小问题.

## Git的配置

### Git全局用户与邮箱设置

        git config --global user.name "Your Name"
        git config --global user.email "email@example.com"

### Git访问GitHub特别慢, 如何配置socks5代理
GitHub提供两种clone方式

* Clone with HTTPS: `git clone https://github.com/xxx/xxx.git`
* Clone with SSH: `git clone git@github.com/xxx/xxx.git`

下面的设置仅对第1种方法有效

设置全局代理

        git config --global http.proxy 'socks5://127.0.0.1:1080'
        git config --global https.proxy 'socks5://127.0.0.1:1080'

可以只对github进行全局代理设置，对国内的仓库不影响

        git config --global http.https://github.com.proxy 'socks5://127.0.0.1:1080'
        git config --global https.https://github.com.proxy 'socks5://127.0.0.1:1080'

同时，如果在输入这条命令之前，已经输入全局代理的话，可以输入进行取消

        git config --global --unset http.proxy
        git config --global --unset https.proxy

注：除了用代理外，以下设置可能有效

        git config --global http.postBuffer 524288000

此外, terminal中设置临时代理

        export ALL_PROXY=socks5://127.0.0.1:1080

或者添加别名

        alias proxy="export ALL_PROXY=socks5://127.0.0.1:1080"

### Git可以使用SSH协议授权, 当你在GitHub和Coding上都有账号时, 如何配置SSH?

假设已经有一个Coding的密钥(文件名默认为`id_rsa`与`id_rsa.pub`)，需要需要添加Github的密钥

1. 生成指定名字的密钥

        ssh-keygen -t rsa -C "YOUREMAIL@163.COM" -f ~/.ssh/github

    这可以生成名为`github`和`github.pub`的密钥文件

2. 修改`~/.ssh/config`文件(如果该文件不存在就自己新建一个), 添加以下代码

        Host github.com www.github.com
        IdentityFile ~/.ssh/github

        Host coding.net www.coding.net
        IdentityFile ~/.ssh/id_rsa

    **注意:** 两条记录间用空行分隔


## Git 使用

1. `git checkout .` 撤消某文件夹内的所有更改

