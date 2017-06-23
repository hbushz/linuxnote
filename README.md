# Linux Note
这里记录了对于我在Linux世界里一些非常重要但又容易忘记的小问题.

## MacVim的配置---*macvimrc*说明
### 如何在退出插入模式后屏蔽中文输入法?
在Normal模式下中文输入法简直是噩梦, 最简单有效的屏蔽方式为
1. 在`vimrc`文件中加入

		set noimd
		set imi=2
		set ims=2

2. 在MacVim的配置项中（Preferences）中, 取消勾选Draw marked text inline这个Advanced选项

在这种配置下, 在命令模式中, 输入法自动会被禁用, 而进入插入模式后, 可以正常使用输入法.  
ESC退出到命令模式时, 会自动禁用输入法. 但在查找模式中, 会启用输入法.

## Git的配置
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

	**注意**两条记录间用空行分隔
	




