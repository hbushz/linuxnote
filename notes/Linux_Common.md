# Linux common note

## Linux中的fcitx设置

当安装好`fcitx`程序以后, 如果无法在`WPS`这种类型的程序中启用输入法,
则需要配置文件`~/.xprofile`, 在其中加入

    export XIM="fcitx"
    export XIM_PROGRAM="fcitx"
    export XMODIFIERS="@im=fcitx"
    export GTK_IM_MODULE="fcitx"
    export QT_IM_MODULE="fcitx"

## Linux中TeXLive的安装小记

1. 首先在CTAN国内的镜像上下载TeXLive光盘镜像文件`texlive2018.iso`，推荐

    * [清华大学开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)

    * [中国科学技术大学开源镜像站](http://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/)

2. 为了使用图形化安装界面，需要安装`perl`的`tk`组件
        sudo pacman -S perl-tk

3. 加载镜像文件

        sudo mount -o loop texlive2018.iso /mnt
        sudo mount -t iso9660 -o ro,loop,noauto /your/texlive.iso /mnt

4. 启动图形安装界面

        sudo /mnt/install-tl -gui

5. 安装选项基本都是默认，只有最后两项

    * 一定要创建指向系统目录的符号链接，选择默认路径即可

    * 自动更新选项选择**否**

6. 点击`安装TeX Live`，进行安装。安装持续时间大约10多分钟，直到出现`完成`按扭，点击完成。 然后卸载镜像文件

        sudo umount /mnt

7. 配置合适的CTAN源可以加快宏包更新的网速，以清华源为例

        sudo tlmgr option repository https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/tlnet

   之后可以利用tlmgr进行网络更新。临时切换源

        sudo tlmgr update --self --all --repository https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/tlnet

   CTAN 上的包更新很频繁，所以即便是最新版的texlive2018， 其中也有大量的宏包需要更新（可能包括tlmgr程序本身）

        sudo tlmgr update --self --all

   临时切换更新源

        sudo tlmgr update --self --all --repository https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/tlnet

8. 删除老版本的`TeX Live`

If you installed `TeX Live` using `install-tl`:

        sudo tlmgr remove --all.

## Linux 与 Windows 双系统设置

### Linux 与 Windows 的时间差校正

Linux和Windows默认的时间管理方式不同，所以双系统发生时间错乱是正常的。
> Linux默认时间是把BIOS时间当成GMT+0时间，也就是世界标准时，而我国在东八区(GMT+8)，
> 所以如果你的Linux位置是中国的话你系统显示的时间就是BIOS时间+8小时。
> 假如现在是早上8点，那么你Linux会显示8点，这时BIOS中的时间是0点。
> 而当你切换到Windows系统时就会发生时间错乱，因为Windows会认为BIOS时间就是你的本地时间，
> 结果就是Windows显示时间为0点……而假如你在Windows下同步时间，恢复显示为8点，
> 这时BIOS时间也会被Windows改写成8点，再次进入Ubuntu时显示时间又变成了8+8=16点……

解决的办法有两个:

* 一个是让Windows使用Linux的时间管理方式， 就是启用UTC(世界协调时)。

    > 在Windows下启用UTC。打开运行窗口(快捷键Win+R)，然后输入regedit启动注册表编辑器，
    > 并找到一下目录位置：
    >
    >     HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Control/TimeZoneInformation/
    >
    > 添加一项类型为`REG_DWORD`的键值，命名为`RealTimeIsUniversal`，值为1。
    > 然后重启后时间即回复正常。

* 另一个就是让Linux按照Windows的方式管理时间， 就是让Linux禁用(世界协调时)。

    > 按Ctrl+Alt+T调出终端，输入：
    >
    >     sudo timedatectl set-local-rtc true
    >

这样就可以解决Windows与Linux双系统时间同步问题了。

### Ubuntu 与 Windows 的默认启动项

当我们安装windows和ubuntu双系统以后，默认启动变成ubuntu了，这对于使用ubuntu作为系统的
童鞋来说没什么，但对那些经常要进windows的童鞋，每次开机都得按几次向下的箭头，再敲回车，
非常不方便，有没有方法，让电脑开机时默认启动windows呢？

打开ubuntu系统以后，我们打开超级终端，输入以下命令

    sudo gedit /etc/default/grub

显示如下

    # If you change this file, run 'update-grub' afterwards to update
    # /boot/grub/grub.cfg.
    # For full documentation of the options in this file, see:
    #   info -f grub -n 'Simple configuration'

    GRUB_DEFAULT=0
    #GRUB_HIDDEN_TIMEOUT=0
    GRUB_HIDDEN_TIMEOUT_QUIET=true
    GRUB_TIMEOUT=10
    GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
    GRUB_CMDLINE_LINUX="locale=zh_CN"


`GRUB_DEFAULT`代表的就是启动项的顺序，从数字0开始，依次代表如下启动项
（这是在我的电脑上，不同的ubuntu版本和windows系统可能会有一些不同）：

    Ubuntu
    Advanced options for Ubuntu
    Memory test (memtest86+)
    Memory test (memtest86+, serial console 115200)
    Windows 8 (loader) (on /dev/sda1)

windows排第四位（注意，顺序是从0开始计的），所以，把`GRUB_DEFAULT`的值修改为4，
然后别忘了运行命令：

    sudo update-grub

重启电脑，默认启动的系统就换到windows了。

## 如何将`visudo`编辑器从`nano`更改为`vim`?

**问题描述:**
在Debain系统中, 当我使用visudo时，它总是用nano编辑器打开它。
如何将编辑器更改为vim？

**最佳方法:**
键入以下命令

    sudo update-alternatives --config editor

## 如何改变时区

We can change timezone in two ways

1. Using `/etc/localtime`

2. Using `timedatectl` command

### Method 1 (Traditional method)

* Check the current time zone using the `date` command
* The `/usr/share/zoneinfo/` directory contains all the timezones. Beneath that
    you can find some directories specific to country or zone. Find the file
    you want. For example:

        /usr/share/zoneinfo/Asia/Shanghai

* Check the current symbolic link `/etc/localtime` using the following command

        ls -al /etc/localtime

* Create a new link with the desired timezone. For example:

        ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

### Method 2 (Novel method)

* Using the `timedatectl` command to list all time zone

        timedatectl list-timezones

*  the `grep` command to filter the output. For example

        timedatectl list-timezones | grep -i shanghai

* Set the timezone using the following command

        timedatectl set-timezone Asia/Shanghai

## Monitoring CPUTemperature

    watch -n 2 sensors

* where `watch` guarantees that the reading will be updated every 2 seconds

* where `sensors` sensors is used to show the current readings of all sensor chips

## MPV Player使用与配置

mpv 是著名开源项目 MPlayer 的分支, 因其对最新软硬件平台, 视频标准以及各种高画质选项的
支持而广受好评.

### 使用说明

1. mpv 在播放界面上提供了一些简单的控制功能。在视频画面上移动鼠标会在界面底部显示
   浮动控制栏。 底部最左边的三个按钮分别是播放/暂停、跳转前后章节。
   进度条右边的几个按钮分别是切换音轨、切换字幕、调节音量和全屏/窗口显示。
   鼠标左键点击音轨和字幕按钮可以直接切换音轨或字幕， `Shift + 左键`则可以
   显示当前已加载的音轨或字幕列表。

2. 常用快捷键

    * `→` 前进 5 秒
    * `←` 后退 5 秒
    * `↑` 前进 1 分钟
    * `↓` 后退 1 分钟
    * `PageUp` 跳转到下一章节
    * `PageDown` 跳转到前一章节
    * `Space` 播放/暂停
    * `9` 降低音量
    * `0` 提高音量
    * `j` 切换字幕
    * `#` 切换音轨
    * `f` 切换全屏/窗口显示
    * `s` 截图
    * `i` 可以显示当前正在播放的文件的媒体信息以及解码、渲染的相关数据。 `Shift + i`
        则可以让这些信息保持显示或清除，显示时点击 `1` 和 `2` 可以分别显示信息的第一、二页

### 配置说明

1. 创建配置文件

    * Linux与macOS系统的配置文件为`~/.config/mpv/mpv.conf`(如果没有就创建一个)
    * Windows 在mpv的解压目录下新建一个名为`portable_config`的新文件夹，例如
        `C:\mpv\portable_config`，将配置文件命名为 `mpv.conf`
        保存在该文件夹内（注意使用记事本的话，保存文件时“保存类型”要选择“所有文件
        (*.*)”，否则文件名会被加上 `.txt` 扩展名，变成 `mpv.conf.txt`）。

2. 配置命令

    * mpv的默认渲染设置非常保守。如果你的显卡性能不是太差（近几年的集成显卡一般都已足够）
      建议启用一套预设的高质量渲染设置，方法是在 mpv.conf 中写上这么一行：

            profile=gpu-hq

      注意，使用高质量渲染设置可能会大大降低笔记本的电池续航时间，在近些年的高分辨率
      屏幕上（例如“Retina显示屏”的 MacBook）尤其明显。

    * mpv默认不对视频进行色彩管理。即使你没有使用校色仪对屏幕进行过校色，
        对于原生色域接近某一标准色域（如sRGB 或 DCI-P3 D65）的屏幕来说，开启色彩管理
        仍然可以获得更准确的颜色，因此，我建议始终将色彩管理开启：

            icc-profile-auto

    * 设置将字幕渲染到视频源分辨率并随视频一起缩放并进行色彩管理，
      这样可以保证字幕的分辨率与画面始终一致（避免“画面模糊字幕高清”的情况），
      并保证字幕中“屏幕字”的颜色与画面一致：

            blend-subtitles=video

    * 如果你有中高端独立显卡，想进一步提高画面拉伸质量，可以将画面拉伸算法更改为
      EWA Lanczos（即madVR 中所谓 Jinc）：

            scale=ewa_lanczossharp

    * 在很多时候，我们的显示器刷新率不是片源帧率的整数倍（例如显示器刷新率通常为
      60 Hz而动画通常为 23.976 fps），此时在默认设置下会因每一帧实际在屏幕上的呈现
      时间不均等而造成卡顿感（俗称 3:2 pull down judder）。
      因此，建议启用 interpolation 来消除这个问题（此功能非常类似于 madVR 中
      的 smooth motion）：

            video-sync=display-resample
            interpolation
            tscale=oversample

    以上是我认为具有普适性的一些选项。其他可以定制的地方还有很多，具体可以参考官方
    的文档对于上百个设置的解释说明。此外，mpv提供了第三方用户脚本支持，可以实现更多
    的功能（例如设置 profile 针对不同片源类型进行不同的处理），以及第三方 user shader
    来实现更多的画面处理（例如NNEDI3、RAVU 等等）。

    相比在图形界面中用鼠标勾勾点点，手写配置文件的方式固然不太符合普通用户的习惯，
    但是“一旦接受了这种设定”，你会逐渐体会到命令行的便利与灵活。

## KDE 文件管理器Dolphin的使用说明

### 快捷键说明

* `F1` 打开帮助

* `F2` 重命名选中文件或文件夹

* `F3` 打开/关闭拆分视图

    - `Ctrl+1` Icon

    - `Ctrl+2` Compact

    - `Ctrl+3` Details

* `F4` 打开/关闭终端面板

* `F5` 刷新

* `F6` 切换导航栏样式

* `F7` 打开/关闭侧边导航窗格

* `F8` 显示/隐藏隐藏文件文件夹

* `F9` 打开/关闭侧边栏

* `F10` 新建文件夹

* `F11` 显示文件文件夹详细信息


## Vimperator的配置---`vimperatorrc`说明

The vimperator is out date now.

### 如何改变难看的配色

Vimperator是支持使用colorscheme的,具体方法(以使用*indigo colorscheme*为例)

1. 将colorscheme配置文件`indigo.vimp`放置于`~/.vimperator/colors/`文件夹内

2. 在`~/.vimperatorrc`文件中加入`colorscheme indigo`

在[vimperator-colors](https://github.com/vimpr/vimperator-colors)仓库中可以找到很多colorscheme.

