# Linux Note

这里记录了对于我在Linux世界里一些非常重要但又容易忘记的小问题.


## Arch Linux相关

### Archlinux 包管理器`pacman`的使用说明

1.  同步与升级
* 安装和升级软件包前，先让本地的包数据库和远程的软件仓库同步是个好习惯。 

        pacman -Syy
    
* 也可以使用一句命令同时进行同步软件库并更新系统到最新状态 

        pacman -Syyu


2.  安装软件包
* 安装或者升级单个软件包，或者一列软件包（包含依赖包），使用如下命令： 

        　　pacman -S package_name1 package_name2

* 有时候在不同的软件仓库中，一个软件包有多个版本（比如extra和testing）。你可以选择一个来安装：

        　　pacman -S extra/package_name
        　　pacman -S testing/package_name

* 你也可以在一个命令里同步包数据库并且安装一个软件包：

        　　pacman -Sy package_name

* 安装一个本地包（不从源里）： 

        　　pacman -U /path/to/package/package_name-version.pkg.tar.gz 

3. 卸载软件包
* 删除单个软件包，保留其全部已经安装的依赖关系 

        　　pacman -R package_name

* 删除指定软件包，及其所有没有被其他已安装软件包使用的依赖关系： 

        　　pacman -Rs package_name

4. 包数据库查询
* 可以使用 -Q 标志搜索和查询本地包数据库。详情参见

        　　pacman -Q --help
        　　pacman -Qi package_name     #显示查找的包信息
        　　pacman -Ql package_name     #显示查找的包的安装
* 可以使用-S 标志搜索和查询远程同步的包数据库。详情参见

            pacman -Ss package_name

5. 完全清理包缓存目录(`/var/cache/pacman/pkg`)：

        　　pacman -Scc　　　　

7. 下载包而不安装它：

        　　pacman -Sw package_name

### ArchlinuxCN 镜像使用帮助

Arch Linux 中文社区仓库 是由 Arch Linux 中文社区驱动的非官方用户仓库。
包含中文用户常用软件、工具、字体/美化包等。
+ [官方仓库](http://repo.archlinuxcn.org)
+ [清华镜像](https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/)

使用方法：在 `/etc/pacman.conf` 文件末尾添加以下两行：

          [archlinuxcn]
          Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch

之后安装 archlinuxcn-keyring 包导入 GPG key:

          sudo pacman -Syy && sudo pacman -S archlinuxcn-keyring

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

### NetworkManager(无线网络相关)

1. Start NetworkManager:

        systemctl start NetworkManager

2. Make it auto-start on boot:

        systemctl enable NetworkManager

3. Use command-line tool `nmcli` to connect to a wireless network:
    * check the radio is enabled

            nmcli radio

    * show wifi device

            nmcli device

    * To actually connect to a wireless AP:

            nmcli device wifi rescan
            nmcli device wifi list
            nmcli device wifi connect SSID-Name password wireless-password # where `SSID-Name` is 无线路由名称，`wireless-password` 是无线密码。

### Arch Linux中`autojump`的安装小记

When you install `autojump`, you should do this post-installation instructions.

If you use bash try doing this command in terminal:

    echo "source /usr/share/autojump/autojump.bash" >> ~/.bashrc

zsh users:

    echo "source /usr/share/autojump/autojump.zsh" >> ~/.zshrc

### Custom sddm DPI

In order to set custom DPI for high resolution screens you should configure Xorg
yourself. An easy way is to pass an additional argument to Xorg.

Edit `/etc/sddm.conf`, go to the X11 section and change ServerArguments like this:

    ServerArguments=-nolisten tcp -dpi 192

to set DPI to 192.(高DPI可以有效解决4K显示屏下sddm字体较小的问题)

## Linux中TeXLive的安装小记

1. 首先在CTAN国内的镜像上下载TeXLive光盘镜像文件`texlive2018.iso`，推荐：
    * [清华大学开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)
    * [中国科学技术大学开源镜像站](http://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/)
2. 为了使用图形化安装界面，需要安装`perl`的`tk`组件
        sudo pacman -S perl-tk
3. 加载镜像文件
        sudo mount -o loop texlive2018.iso /mnt
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
<!-- vim-markdown-toc GFM -->

<!-- vim-markdown-toc -->
