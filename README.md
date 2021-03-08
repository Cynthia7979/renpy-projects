# Cynthia7979的Ren'Py Projects
本repo将实现：
* 自动将[猫爷TRPG](https://maoyetrpg.com)的导出log转为`.rpy`脚本，其中包括：
    * 人物立绘自动切换
    * 骰子音效
    * 自动播放
    * **不包括：** 人物语音、背景音乐、背景转换、条件跳转、和所有没有列出来的东西
* 将`.rpy`脚本转为含有朗读者标签的朗读女文件。

参考：[【教程】如何使用Renpy制作跑团视频](https://blog.maddestroyer.xyz/2020/06/12/renpy/)

本repo使用了fstring等特性，**仅适用于Python 3**。

> 如果对实现方法不满意，请考虑自己调整样式。如果需要帮助或有其他建议，请
>[创建一个Issue](https://github.com/Cynthia7979/renpy-projects/issues/new/choose)。

## Log转Ren'Py使用方法
1. 在Ren'Py中创建一个新的工程，不要做什么改动
2. 将log复制到`log.txt`中，参考`log_formats.md`调整格式
3. 运行`log2rpyscript.y`
4. 将本文件夹中的：
    * `script.rpy`
    * `screen.rpy`
    * `gui.rpy`
    * `msyhl.ttc`
    * `roll.mp3`
    * `success.mp3`
    * `fail.mp3`
    * `bigsuccess.mp3`
    * `bigfail.mp3`

    复制到`game`文件夹中，覆盖原有的文件
5. 将你要用的所有角色立绘命名成角色的*全名*，然后复制到`images`文件夹中
6. 在Ren'Py中运行你创建的工程

生成好的Ren'Py游戏会打开自动播放并隐藏游戏内菜单，可以直接用OBS或其他录屏软件录制后剪辑。
然而，如果需要*背景转换*等操作的话，请**手动修改**Ren'Py脚本。**进一步的自定义请查看[文档](https://www.renpy.cn/doc/index.html)。**

需要注意的是，本程序**不会**自动封装人物语音，只有骰子和成功/失败音效，需要后期剪辑时手动添加语音（使用[朗读女](http://www.443w.com/tts)
或其它软件）。

程序同时会自动生成一个`朗读女.txt`，其中包括带标签的人物台词，使用方法参考[这篇教程](http://www.443w.com/tts/?post=26)
（标签名使用人物名字）。

**命令行语法：**

```*\renpy-projects> log2rpyscript.py <log_file>```

## Ren'Py转朗读女使用方法
如果你喜欢手动编写Ren'Py脚本，或者希望根据更改后的脚本生成语音文件，那么可以直接使用`renpy2langdunv`将Ren'Py脚本转换为带标签的`txt`文件。

**注意！** 这会覆盖`log2renpy`生成的朗读女文件。

步骤：
1. 将`script.rpy`复制到本文件夹
2. 运行`renpy2langdunv.py`
3. 使用朗读女打开生成的`朗读女.txt`，设定好朗读者后生成语音文件。使用方法参考[这篇教程](http://www.443w.com/tts/?post=26)

`renpy2langdunv.py`会跳过包含"SAN CHECK"，"1d100"，"检定"等关键词的台词。可以在`should_pass()`中修改关键词列表。

**命令行语法：**

```*\renpy-projects> renpy2langdunv.py <rpy_script> <output_file>```

## 软件下载
| 名称 | 下载链接 |
| --- | ------- |
| Ren'Py | https://www.renpy.org |
| Python 3 | https://www.python.org/downloads/release/python-391/ |
| OBS（录屏） | https://obsproject.com |
| 朗读女 | http://www.443w.com/tts/ |

## 素材来源
* [roll.mp3](http://www.sucaitianxia.net/yinxiaosucai/tiyu/200708/1546.html)
* `success.mp3`, `fail.mp3`, `bigfail.mp3`, `bigsuccess.mp3 ` - [爱给网](http://www.aigei.com)，使用了格式工厂进行转换
