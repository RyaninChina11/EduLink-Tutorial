=========
安装 EduLink
=========

使用 **Git** 以安装 EduLink
=========

.. admonition:: 阅读本文档前

    本文档仅用于教育目的， **部分名词可能使用不当** 。
    
    我们可能使用了 **涉嫌版权** 的图片。
    如果有图片 **涉嫌侵权** ，我们会尽早替换。

电脑打开 **任意浏览器（如Chrome、Edge等）**，输入网址 `10.1.2.3:8888 <10.1.2.3:8888>`_ ,进入 **行空板Jupyter服务页面**

.. image:: https://img.picui.cn/free/2025/05/25/68325d8309160.png
    :align: center
    :alt: 行空板Jupyter服务页面

单击靠右的 **新建** 按钮，在下拉菜单中选择 **终端** 。

.. image:: https://img.picui.cn/free/2025/05/25/68325e3e6b57c.png
    :align: center
    :alt: 新建 菜单

此时将进入 **终端页面** ，即 **Linux中的命令行界面** 。

.. image:: https://img.picui.cn/free/2025/05/25/68325eb4445ba.png
    :align: center
    :alt: 新建 菜单

输入以下命令，以检查 Git 的版本号：

.. code-block:: sh

   git --version

应返回Git 版本号，例如：

.. code-block:: sh

    git version 2.20.1

.. note::

    在 终端页面 中，粘贴文本需使用 Ctrl+Shift+V (Windows) 。

    其他操作系统浏览器的粘贴方式还未经测试。

.. admonition:: 版本号不一样？

    没关系，本文档仅需使用 ``git init`` 和 ``git clone`` 命令，

    查看 Git 版本号仅仅是为了验证 **Git 是否安装** ， **与版本无关**。

    如果返回的是 ``bash: git：未找到命令``，那么您需要运行以下命令来安装 Git ：

    .. code-block:: sh

        sudo apt-get install git

    这一步通常不需要，因为 行空板 似乎自带 Git 。


输入以下命令，以创建一个新的 Git 仓库：

.. code-block:: sh

    git init

应返回以下内容：

.. code-block:: sh

    已初始化空的 Git 仓库于 /root/.git/

输入以下命令， Git 就会将远程 EdLink 的 Github 仓库克隆到本地：

.. code-block:: sh

    git clone https://www.github.com/RyaninChina11/EduLink.git/

等待大约一分钟，即可完成。完成后终端应显示：

.. code-block:: sh

    正克隆到 'EduLink'...
    remote: Enumerating objects: 97, done.
    remote: Counting objects: 100% (97/97), done.
    remote: Compressing objects: 100% (93/93), done.
    remote: Total 97 (delta 49), reused 6 (delta 0), pack-reused 0 (from 0)
    展开对象中: 100% (97/97), 完成.

.. admonition:: 报错了？

    这可能是因为 Github 被墙了，即网络问题。

    多运行几次可能会解决这个问题。

.. admonition:: [后续问题] 消息没有声音？ 或 消息音量太响？

    使用以下命令

    .. code-block:: sh

        alsamixer

    即可进入 行空板 自带的音量调整器

    按下 `F6` ，显示以下内容：

    .. code-block:: sh

        ┌────── Sound Card ───────┐

        │-  (default)             │

        │0  Loopback              │

        │1  rockchip,rk3308-acodec│

        │2  这个名字可能不一样      │

        │   enter device name...  │

        └─────────────────────────┘ 

    按 方向键（↑和↓）以选择2（这个名字可能不一样）后按回车

    即可再次使用 方向键（↑和↓）以调整音量

    调整完毕后按 `Esc` 退出

完成！接下来该 :doc:`配置 EduLink<set>` 了。    
