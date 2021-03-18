# Arch Linux相关

## Archlinux 包管理器`pacman`的使用说明

1. 源的选择
    * pacman-mirrors 寻找最快镜像源

            sudo pacman-mirrors -c China -m rank -i

    * 其中参数`-c` 指定国家, `-m` 指定排序方式, `-i` 采用交互选择方式

1. 同步与升级
    * 安装和升级软件包前，先让本地的包数据库和远程的软件仓库同步是个好习惯。

                pacman -Syy

    * 也可以使用一句命令同时进行同步软件库并更新系统到最新状态

                pacman -Syyu

1. 安装软件包
    * 安装或者升级单个软件包，或者一列软件包（包含依赖包），使用如下命令：

            　　pacman -S package_name1 package_name2

    * 有时候在不同的软件仓库中，一个软件包有多个版本（比如extra和testing）。你可以选择一个来安装：

            　　pacman -S extra/package_name
            　　pacman -S testing/package_name

    * 你也可以在一个命令里同步包数据库并且安装一个软件包：

            　　pacman -Sy package_name

    * 安装一个本地包（不从源里）：

            　　pacman -U /path/to/package/package_name-version.pkg.tar.gz
                pacman -U http://www.example.com/repo/example.pkg.tar.xz

    * 下载包而不安装它：

            　　pacman -Sw package_name

    * 强制覆盖冲突的软件包：

            　　pacman -Sw package_name

1. 卸载软件包
    * 删除单个软件包，保留其全部已经安装的依赖关系

            　　pacman -R package_name

    * 删除指定软件包，及其所有没有被其他已安装软件包使用的依赖关系：

            　　pacman -Rs package_name

1. 包数据库查询
    * 可以使用 -Q 标志搜索和查询本地包数据库。详情参见

            　　pacman -Q --help
            　　pacman -Qi package_name     #显示查找的包信息
            　　pacman -Ql package_name     #显示查找的包的安装
            　　pacman -Qo /path/to/file    #查找某个文件被那个包占用

    * 可以使用 -F 标志搜索和查询本地包数据库。详情参见

            　　pacman -Fy package_name

    * 可以使用-S 标志搜索和查询远程同步的包数据库。详情参见

                pacman -Ss package_name

1. 完全清理包缓存目录(`/var/cache/pacman/pkg`)：

        　　pacman -Scc

1. Note

Q: Whenever I try to install/uninstall a package pacman takes around 5~10 seconds
for "fixing hard coded icons" post transaction hook.

A: The package is hardcoder-fixer. Remove if you wish as it is non-critical.

1. 查看package依赖

        　　pactree -Scc

## ArchlinuxCN 镜像使用帮助

Arch Linux 中文社区仓库 是由 Arch Linux 中文社区驱动的非官方用户仓库。
包含中文用户常用软件、工具、字体/美化包等。

* [官方仓库](http://repo.archlinuxcn.org)

* [清华镜像](https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/)

使用方法：在 `/etc/pacman.conf` 文件末尾添加以下两行：

          [archlinuxcn]
          Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch

之后安装 archlinuxcn-keyring 包导入 GPG key:

          sudo pacman -Syy && sudo pacman -S archlinuxcn-keyring

## Mathematica 11.3 conflicts with system libraries

The Mathematica package includes a number of it's own libraries,
located in InstallPath/SystemFiles/Libraries/Linux-x86-64.
They may lead to some compatibility issues and fallback to the system
versions of some of these libraries may be necessary.

Symbol lookup error: /usr/lib/libfontconfig.so.1: undefined symbol:
FT_Done_MM_Var
Force Mathematica to use the system version of the freetype library.

         cd <INSTALL_DIR>/SystemFiles/Libraries/Linux-x86-64
         mv libfreetype.so.6 libfreetype.so.6.old

Mathematica/11.3/SystemFiles/Libraries/Linux-x86-64/libz.so.1: version
'ZLIB_1.2.9' not found (required by /usr/lib/libpng16.so.16)
Force Mathematica to use the system version of the zlib library.

         cd <INSTALL_DIR>/SystemFiles/Libraries/Linux-x86-64
         mv libz.so.1 libz.so.1.old

## Matlab Hidpi

MathWorks suggested the following procedure, which works well for me (R2017b).
Quoting from their email:
Tuning a high-DPI Linux system requires two steps

1. Setting the MATLAB scale factor
2. Calibrating the system's DPI

The MATLAB scale factor affects MATLAB desktop and the size/position of
windows. The system DPI determines the scale and font size of axes and labels.
To set the MATLAB scale factor, please use the following MATLAB commands:

        >> s = settings;s.matlab.desktop.DisplayScaleFactor
        >> s.matlab.desktop.DisplayScaleFactor.PersonalValue = 1.5

To calibrate the system DPI to match the scale facto, please use the following
terminal commands :

        % xdpyinfo | grep resolution
        resolution:    96x96 dots per inch
        % xrandr --dpi 144

The DPI value chosen should be the resolution found with xdpyinfo multiplied by
the MATLAB scale factor that was set. In the example, 96 × 1.5 = 144.

MATLAB must be restarted after Step 2.

我自己只设置了第一步, Matlab就显示比较正常了.

## NetworkManager(无线网络相关)

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
            nmcli device wifi connect SSID-Name password wireless-password
            # where `SSID-Name` is 无线路由名称，`wireless-password` 是无线密码

## Arch Linux中`autojump`的安装小记

When you install `autojump`, you should do this post-installation instructions.

If you use bash try doing this command in terminal:

    echo "source /usr/share/autojump/autojump.bash" >> ~/.bashrc

zsh users:

    echo "source /usr/share/autojump/autojump.zsh" >> ~/.zshrc

## Custom sddm DPI

In order to set custom DPI for high resolution screens you should configure Xorg
yourself. An easy way is to pass an additional argument to Xorg.

Edit `/etc/sddm.conf`, go to the X11 section and change ServerArguments like this:

    ServerArguments=-nolisten tcp -dpi 192

to set DPI to 192.(高DPI可以有效解决4K显示屏下sddm字体较小的问题)

