# Linux Note
这里记录了对于我在Linux世界里一些非常重要但又容易忘记的小问题.

<!-- vim-markdown-toc GFM -->

* [Ubuntu中GVim的配置---`vimrc`说明](#ubuntu中gvim的配置---vimrc说明)
	* [能否用Vim来编辑LaTeX文档, 实现TeX文档的集成写作环境?](#能否用vim来编辑latex文档-实现tex文档的集成写作环境)
	* [如何在退出插入模式后屏蔽中文输入法?](#如何在退出插入模式后屏蔽中文输入法)
	* [在用vim编辑Markdown文档时, 如何实现实时预览?](#在用vim编辑markdown文档时-如何实现实时预览)
* [Mac OS中MacVim的配置---`macvimrc`说明](#mac-os中macvim的配置---macvimrc说明)
	* [如何在退出插入模式后屏蔽中文输入法?](#如何在退出插入模式后屏蔽中文输入法-1)
* [Git的配置](#git的配置)
	* [Git可以使用SSH协议授权, 当你在GitHub和Coding上都有账号时, 如何配置SSH?](#git可以使用ssh协议授权-当你在github和coding上都有账号时-如何配置ssh)
* [Vimperator的配置---`vimperatorrc`说明](#vimperator的配置---vimperatorrc说明)
	* [如何改变难看的配色?](#如何改变难看的配色)

<!-- vim-markdown-toc -->
## Ubuntu中GVim的配置---`vimrc`说明
建议采用Vundle进行Vim插件管理, 非常方便.
### 能否用Vim来编辑LaTeX文档, 实现TeX文档的集成写作环境?
使用插件[`vimtex`](https://github.com/lervag/vimtex/), 在`vimrc`文件中加入

		Plugin 'lervag/vimtex'
		"---------------------
		" set vimtex
		" --------------------
		" Set the viewer method
		let g:vimtex_view_general_viewer = 'zathura'
		let g:vimtex_view_method = 'zathura'
		" Customization of the latexmk compiler
		let g:vimtex_compiler_latexmk = {
		  \ 'backend' : 'jobs',
		  \ 'background' : 1,
		  \ 'build_dir' : '',
		  \ 'callback' : 1,
		  \ 'continuous' : 1,
		  \ 'executable' : 'latexmk',
		  \ 'options' : [
		  \   '-pdf',
		  \   '-verbose',
		  \   '-file-line-error',
		  \   '-xelatex',
		  \   '-synctex=1',
		  \   '-interaction=nonstopmode',
		  \ ],
		  \}

然后在系统中安装好TeXLive就可以实现TeX文档的编辑, 编译, 调试.


### 如何在退出插入模式后屏蔽中文输入法?
在Normal模式下中文输入法简直是噩梦, 若你采用的是小企鹅输入法框架(Fcitx)的话, 最简单有效的屏蔽方式为
使用插件[`fcitx`](https://github.com/vim-scripts/fcitx.vim). 只要在`vimrc`文件中加入

		Plugin 'vim-scripts/fcitx.vim'

就再也不用担心输入法的切换了.


### 在用vim编辑Markdown文档时, 如何实现实时预览?
请使用插件[`markdown-preview`](https://github.com/iamcco/markdown-preview.vim), 只要在`vimrc`文件中加入	

		Plugin 'iamcco/markdown-preview.vim'
		let g:mkdp_path_to_chrome = "firefox"
		let g:mkdp_auto_start = 1

感觉会非常爽.

## Mac OS中MacVim的配置---`macvimrc`说明
### 如何在退出插入模式后屏蔽中文输入法?
对于MacVim最简单有效的屏蔽方式为
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

	**注意:** 两条记录间用空行分隔
	
## Vimperator的配置---`vimperatorrc`说明
### 如何改变难看的配色?
Vimperator是支持使用colorscheme的,具体方法(以使用*indigo colorscheme*为例)
1. 将colorscheme配置文件`indigo.vimp`放置于`~/.vimperator/colors/`文件夹内
2. 在`~/.vimperatorrc`文件中加入`colorscheme indigo`

在[vimperator-colors](https://github.com/vimpr/vimperator-colors)仓库中可以找到很多colorscheme.


