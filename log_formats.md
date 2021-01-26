# 总体格式要求
1. 文件编码为`UTF-8`

## `maoye` 猫爷TRPG导出格式
```
<character> <yyyy>/<mm>/<dd> <hh>:<mm>:<ss>             - infoline
    <msg (characterized by indentation of 4 spaces)>    - msgline
```
在replay中一般仅需要`character`和`msg`两个值，因此`log2rpyscript.py`也会只获取这两个值。

### 需要注意的地方
1. 请将**所有多行信息**和**空行**移除或排成一行，保证**每两行**出现**一组**人物及其对话。
2. 请确保**文件由`infoline`开头，以`msgline`结尾**（而不是空行或infoline）。
3. 人物名字不允许存在类似` 1234/`（空格+四个数字+/）的内容。这是为了让程序能找到人物名称。
