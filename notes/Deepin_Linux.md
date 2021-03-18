# Deepin Linux 相关

## Remap `CapsLock` as `Ctrl`

我先后尝试了两种方法

* 利用`setxkbmap`

    1. 临时更改 终端输入以下命令

        `setxkbmap -layout us -option ctrl:nocaps`

    1. 永久更改 修改配置文件 `/etc/default/keyboard` 修改 `XKBOPTIONS`的值

        ```bash
        XKBMODEL="pc105"
        XKBLAYOUT="cn"
        XKBVARIANT=""
        XKBOPTIONS="ctrl:nocaps"
        # XKBOPTIONS="ctrl:swapcaps"    # 交换 Ctrl 与 CapsLock
        ```

* 利用`Xmodmap`

    1. 临时更改 在终端执行命令

        `xmodmap ~/.Xmodmap`

    1. 永久更改
    编辑文件 `~/.xinitrc` 内容如下 `[ -f ~/.Xmodmap ] && xmodmap ~/.Xmodmap`
    (对于 *Deepin V20* 经测试该方法会受到系统锁屏程序的影响而失效)

    1. 这里文件 `~/.Xmodmap` 内容如下

        ```bash
        remove Lock = Caps_Lock
        keycode 0x42 = Control_L
        add Control = Control_L
        ```

        若交换 CapsLock 与 CtrlR, 则需要配置文件为

        ```bash
        !
        ! Swap Caps_Lock and Control_R
        !
        remove Lock = Caps_Lock
        remove Control = Control_R
        keysym Control_R = Caps_Lock
        keysym Caps_Lock = Control_R
        add Lock = Caps_Lock
        add Control = Control_R
        ```

