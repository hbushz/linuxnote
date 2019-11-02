# Python Note

这里记录了Python使用中一些非常重要但又容易忘记的小问题.

## Python包管理工具pip

---

### 常用命令

1. 搜索包: `pip search 关键字`

1. 安装包: `pip install 包名`

2. 安装本地的安装包: `pip install 目录|文件名`

3. 安装包到用户目录: `pip install 包名 --user`

4. 下载包但不安装: `pip install 包名 -d 目录`

1. 查看已安装包的详情: `pip show 包名`

2. 显示已安装包的目录: `pip show -f 包名`

1. 查看过期的包: `pip list --outdated`

2. 查询可升级的包: `pip list -o`

3. 升级包: `pip install 包名 --upgrade`

4. 升级pip包自身: `pip install pip --upgrade`

1. 卸载包: `pip uninstall 包名`

1. 打包: `pip wheel 包名`

### 配置镜像源

* [中科大镜像](https://mirrors.ustc.edu.cn/pypi/)

* [清华镜像](https://pypi.tuna.tsinghua.edu.cn/simple)

1. 临时使用

    ```bash
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
    ```

1. 设为默认

    修改`pip.conf`的配置文件

    ```python
    [global]
    index-url = https://mirrors.ustc.edu.cn/pypi/web/simple
    format = columns
    ```

## Python与系统交互

---

### Python调用Shell Scripts

* 通过`subprocess`模块实现

    ```python
    import subprocess

    res = subprocess.check_output(["lsmod"])
    for line in res.splitlines():
        print(line.decode("utf_8"))
    ```

## Pandas

---

### The difference bewteen `loc` and `iloc` of Pandas

Here's a recap of the two methods:

* `loc` gets rows (or columns) with particular labels from the index.

* `iloc` gets rows (or columns) at particular positions in the index (so it only takes integers).
