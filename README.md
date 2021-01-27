# Cynthia7979的Ren'Py Projects
本repo将实现：
* 自动将猫爷TRPG的导出log转为`.rpy`脚本，其中包括：
    * 人物立绘自动切换（双人对话时自动暗化另一方立绘）
    * 骰子音效
    * 自动播放
    * **不包括：** 人物语音、背景音乐、背景转换、条件跳转、和所有没有列出来的东西

参考：[【教程】如何使用Renpy制作跑团视频](https://blog.maddestroyer.xyz/2020/06/12/renpy/)

本repo使用了fstring等特性，**仅适用于Python 3**。

## Log转Ren'Py使用方法
1. 在Ren'Py中创建一个新的工程，不要做什么改动
2. 将log复制到`log.txt`中，参考`log_formats.md`调整格式
3. （TODO）
4. 将生成的`script.rpy`和一开始就有的`screen.rpy`，`gui.rpy`, 以及`msyhl.ttc`复制到`game`文件夹中，覆盖原有的文件
5. 将你要用的所有角色立绘命名成角色的*全名*，然后复制到`images`文件夹中

生成好的Ren'Py游戏会打开自动播放并隐藏游戏内菜单，可以直接用OBS或其他录屏软件录制后剪辑。

然而，如果需要背景转换等操作的话，请手动修改Ren'Py脚本

需要注意的是，本程序**不会**自动封装人物语音，只有骰子和成功/失败音效，后期剪辑时请注意这一点

## 素材来源
* [roll.mp3](http://www.sucaitianxia.net/yinxiaosucai/tiyu/200708/1546.html)
* `success.mp3`, `fail.mp3`, `bigfail.mp3` - [爱给网](http://www.aigei.com)
