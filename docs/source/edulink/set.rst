=========
配置 EduLink
=========

本文档将把 ``config.ini`` （ **配置文件** ）填写完整

.. admonition:: 阅读本文档前

    本文档仅用于教育目的， **部分名词可能使用不当** 。
    
    我们可能使用了 **涉嫌版权** 的图片。
    如果有图片 **涉嫌侵权** ，我们会尽早替换。

电脑打开 **任意浏览器（如Chrome、Edge等）**，打开本文档后， `点我进入 百度智能云登录 网页<https://login.bce.baidu.com/?redirect=https%3A%2F%2Fconsole.bce.baidu.com%2Fai-engine%2Fold%2F#/ai/speech/app/list>`_ 。

.. image:: https://img.picui.cn/free/2025/05/25/683306c01d2f5.png
    :align: center
    :alt: 百度智能云登录页面

登录后，将自动跳转至 **语音生成应用列表 网页** ，单击 **创建应用** 按钮。

.. image:: https://img.picui.cn/free/2025/05/25/68330744cf0b6.png
    :align: center
    :alt: 语音生成应用列表 网页 及 创建应用 按钮位置
    
进入 **创建新应用 网页** ，填写所有带 **红色*号** 的内容：

*应用名称* ：填什么都可以

.. image:: https://img.picui.cn/free/2025/05/25/68330aac64244.png
    :align: center
    :alt: 应用名称 填写示例

*接口选择* ：默认即可

.. image:: https://img.picui.cn/free/2025/05/25/68330bbcd36ba.png
    :align: center
    :alt: 接口选择 填写示例

*语音包名* ：默认即可

.. image:: https://img.picui.cn/free/2025/05/25/68330bd16258a.png
    :align: center
    :alt: 语音包名 填写示例

*应用归属* ：选择 *个人*

.. image:: https://img.picui.cn/free/2025/05/25/68330c63332f9.png
    :align: center
    :alt: 应用归属 填写示例

*应用描述* ：填什么都可以

.. image:: https://img.picui.cn/free/2025/05/25/68330c8c2d7d6.png
    :align: center
    :alt: 应用描述 填写示例

最后单击 **立即创建** 即可成功创建。

.. image:: https://img.picui.cn/free/2025/05/25/68330e1cd8aa5.png
    :align: center
    :alt: 立即创建 按钮位置

显示 **创建完毕** 后，单击 **查看应用详情**

.. image:: https://img.picui.cn/free/2025/05/25/68330e6757bea.png
    :align: center
    :alt: 创建完毕 页面 及 查看应用详情 按钮位置

进入 **应用详情 页面** 后，复制 **API Key** 和 **Secret Key** 。

.. image:: https://img.picui.cn/free/2025/05/25/6833100d14590.png
    :align: center
    :alt: 应用详情 页面 及 API Key 和 Secret Key 显示位置

在 浏览器地址栏 输入 `10.1.2.3:8888/edit/EduLink/config.ini<http://10.1.2.3:8888/edit/EduLink/config.ini>`_ ，进入 **配置文件编辑页面** 。

在 **下图红框所标注的位置** 分别填入 **API Key** 和 **Secret Key** ：

.. image:: https://img.picui.cn/free/2025/05/25/683312d38ed88.png
    :align: center
    :alt: 将 API Key 和 Secret Key 填入 配置文件

**键盘按下 Ctrl+S 保存**

**不要关闭此标签页，备用**

`点我 进入 高德开放平台登录 网页<https://lbs.amap.com/?ref=https://console.amap.com/dev/index>`_

登录后，单击 **创建新应用**

.. image:: https://img.picui.cn/free/2025/05/25/683316654add5.png
    :align: center
    :alt: 创建新应用 按钮位置

进入 **新建应用 页面** ，填写所有带 **红色*号** 的内容：

*应用名称* ：填什么都可以

*应用类型* ：推荐 *教育*

填写完毕后，单击 **新建** 。

.. image:: https://img.picui.cn/free/2025/05/25/68331756affbd.png
    :align: center
    :alt: 高德 创建新应用 样例示范 及 新建 按钮位置

新建完毕后，单击 **添加Key** 。

.. image:: https://img.picui.cn/free/2025/05/25/683317f16bb3e.png
    :align: center
    :alt: 添加Key 按钮位置

进入 **添加Key 页面** ，填写所有带 **红色*号** 的内容：

*Key名称* ：填什么都可以

*服务平台* ：选择 *Web服务*

**勾选 阅读并同意 高德地图开放平台服务协议 和 高德地图开放平台隐私权政策**

填写完毕后，单击 **提交** 。

.. image:: https://img.picui.cn/free/2025/05/25/683319a810e94.png
    :align: center
    :alt: 高德 添加Key 示范样例 及 提交 按钮位置

之后再下图红框范围内复制 **Key** ：

.. image:: https://img.picui.cn/free/2025/05/25/68331a8321812.png
    :align: center
    :alt: Key 位置

回到 `配置文件编辑页面<http://10.1.2.3:8888/edit/EduLink/config.ini>`_ 。

这次将 **下图红框所标注的位置** 填入您刚刚复制的内容。

.. image:: https://img.picui.cn/free/2025/05/25/68331b922d297.png
    :align: center
    :alt: 将 Key 填入 配置文件

将 **下图红框所标注的位置** 填入以下内容。

.. image:: https://img.picui.cn/free/2025/05/25/68331edeb3521.png
    :align: center
    :alt: 将 EasyIoT信息 填入 配置文件

.. code-block::

    3Q_H7J1Hg

.. code-block::

    _O64nJ1Hg

.. code-block::

    ld6V7J1HRz

.. caution::

    这是一个公开的设备，仅用于测试，因此可能无法正常使用。

    如果您真的要使用，请 `联系我们<mailto:18149721348@163.com>` ，我们将会为您新建一个设备。

**键盘按下 Ctrl+S 保存**

现在回到 **行空板**，长按 **Home 键** 进入 主菜单。

使用 **A键 B键 上下调整 Home键 选中** 以选择 **2-切换运行程序**

.. image:: https://img.picui.cn/free/2025/05/25/683320db952a2.png
    :align: center
    :alt: 2-切换运行程序

分别使用 **A键 B键 上下调整 Home键 选中** 选择以下选项： **root/ →  EduLink/ → EduLink.py**

.. image:: https://img.picui.cn/free/2025/05/25/6833213c00758.png
    :align: center
    :alt: EduLink.py

首次运行需先行安装字体，可能需要5~10秒左右。

现在程序应当开始运作了，如下图：

.. image:: https://img.picui.cn/free/2025/05/25/683322b365352.png
    :align: center
    :alt: EduLink 运作时

恭喜！您完成了 EduLink 安装配置教程 的所有章节！

现在是时候看看 :doc:`如何安装并使用 班讯<../classages/index>` 来向 EduLink 发送消息了。
