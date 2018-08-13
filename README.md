# Linux Note
这里记录了对于我在Linux世界里一些非常重要但又容易忘记的小问题.

<!-- vim-markdown-toc GFM -->

* [Arch Linux相关配置](#arch-linux相关配置)
    - [Mathematica 11.3 conflicts with system libraries](#mathematica-113-conflicts-with-system-libraries)
* [Linux中TeXLive的安装小记](#linux中texlive的安装小记)
* [Linux中GVim的配置---`vimrc`说明](#linux中gvim的配置---vimrc说明)
    - [能否用Vim来编辑LaTeX文档, 实现TeX文档的集成写作环境?](#能否用vim来编辑latex文档-实现tex文档的集成写作环境)
    - [如何在退出插入模式后屏蔽中文输入法?](#如何在退出插入模式后屏蔽中文输入法)
    - [在用vim编辑Markdown文档时, 如何实现实时预览?](#在用vim编辑markdown文档时-如何实现实时预览)
* [Git的配置](#git的配置)
    - [Git访问GitHub特别慢, 如何配置socks5代理?](#git访问github特别慢-如何配置socks5代理)
    - [Git可以使用SSH协议授权, 当你在GitHub和Coding上都有账号时, 如何配置SSH?](#git可以使用ssh协议授权-当你在github和coding上都有账号时-如何配置ssh)
* [Vimperator的配置---`vimperatorrc`说明](#vimperator的配置---vimperatorrc说明)
    - [如何改变难看的配色?](#如何改变难看的配色)
* [Mac OS中MacVim的配置---`macvimrc`说明](#mac-os中macvim的配置---macvimrc说明)
    - [如何在退出插入模式后屏蔽中文输入法?](#如何在退出插入模式后屏蔽中文输入法-1)

<!-- vim-markdown-toc -->

## Arch Linux相关配置
### Mathematica 11.3 conflicts with system libraries
The Mathematica package includes a number of it's own libraries,
located in InstallPath/SystemFiles/Libraries/Linux-x86-64.
They may lead to some compatibility issues and fallback to the system
versions of some of these libraries may be necessary.

Symbol lookup error: /usr/lib/libfontconfig.so.1: undefined symbol: FT_Done_MM_Var
Force Mathematica to use the system version of the freetype library.

        $ cd <INSTALL_DIR>/SystemFiles/Libraries/Linux-x86-64
        $ mv libfreetype.so.6 libfreetype.so.6.old

Mathematica/11.3/SystemFiles/Libraries/Linux-x86-64/libz.so.1: version 'ZLIB_1.2.9' not found (required by /usr/lib/libpng16.so.16)
Force Mathematica to use the system version of the zlib library.

        $ cd <INSTALL_DIR>/SystemFiles/Libraries/Linux-x86-64
        $ mv libz.so.1 libz.so.1.old

## Linux中TeXLive的安装小记
1. 首先在CTAN国内的镜像上下载TeXLive光盘镜像文件`texlive2018.iso`，推荐：
    * [清华大学开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)
    * [中国科学技术大学开源镜像站](http://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/)
2. 为了使用图形化安装界面，需要安装`perl`的`tk`组件
        sudo pacman -S perl-tk
3. 加载镜像文件
        sudo mount -o loop texlive2017.iso /mnt
4. 启动图形安装界面
        sudo /mnt/install-tl -gui
5. 安装选项基本都是默认，只有最后两项
    * 一定要创建指向系统目录的符号链接，选择默认路径即可
    * 自动更新选项选择**否**
6. 点击`安装TeX Live`，进行安装。安装持续时间大约10多分钟，直到出现`完成`按扭，点击完成。
   然后卸载镜像文件
        sudo umount /mnt
7. 配置合适的CTAN源可以加快宏包更新的网速，以中科大的源为例：
        sudo tlmgr option repository http://mirrors.ustc.edu.cn/CTAN/systems/texlive/tlnet
   之后可以利用tlmgr进行网络更新。CTAN 上的包更新很频繁，所以即便是最新版的texlive2018，
   其中也有大量的宏包需要更新（可能包括tlmgr程序本身）
        sudo tlmgr update --self --all
## Linux中GVim的配置---`vimrc`说明
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
        let g:mkdp_auto_start = 1

感觉会非常爽.

## Git的配置
### Git访问GitHub特别慢, 如何配置socks5代理?
可以只对github进行全局代理设置，对国内的仓库不影响

        git config --global http.https://github.com.proxy socks5://127.0.0.1:1086
        git config --global https.https://github.com.proxy socks5://127.0.0.1:1086

同时，如果在输入这条命令之前，已经输入全局代理的话，可以输入进行取消

        git config --global --unset http.proxy
        git config --global --unset https.proxy

注：除了用代理外，以下设置可能有效

        git config --global http.postBuffer 524288000

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


