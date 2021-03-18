# Vim config file

Vim是我最喜欢的编辑器，这里记录了vim配置的配置文件

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

### 在用vim编辑Markdown文档时, 如何实现实时预览

请使用插件[`markdown-preview`](https://github.com/iamcco/markdown-preview.vim), 只要在`vimrc`文件中加入

        Plugin 'iamcco/markdown-preview.vim'
        let g:mkdp_auto_start = 1

感觉会非常爽.

## Mac OS中MacVim的配置---`macvimrc`说明

