```shell script
         ____            _     _              ____             _ _
        |  _ \ ___  __ _(_)___| |_ ___ _ __  / ___| _ __  _ __(_) |_ ___
        | |_) / _ \/ _` | / __| __/ _ \ '__| \___ \| '_ \| '__| | __/ _ \
        |  _ <  __/ (_| | \__ \ ||  __/ |     ___) | |_) | |  | | ||  __/
        |_| \_\___|\__, |_|___/\__\___|_|    |____/| .__/|_|  |_|\__\___|
                   |___/                           |_|
```
# **寄存器小精灵**

寄存器小精灵（Register Sprite）基于**python tkinter**编写，具有良好的界面和一些简单的交互功能，它可以轻松实现**10进制**、**16进制**、**8进制**和**2进制**之间的转换，可视化配置各种芯片的寄存器，嵌入式工程师的**必备神器**。
我提供了使用**pyinstaller**构建好的可执行文件，当然你也可以**修改后**构建自己的EXE文件。

> 如果你有更好的构建方法，欢迎指教！

安装教程
----

* 设备中已有Python环境
  
    > 通过本地python解释器直接运行main.py文件
    >
    > `python main.py `
    
* 设备中未安装Python环境
  
    > 作者提供了位于bin目录下构建好的exe文件

保持更新
----
```shell script
git pull origin
```

预览图
---
![avatar](http://ngrok.huazheng.club/wp-content/uploads/2020/11/my_pic1.png)
---
![avatar](http://ngrok.huazheng.club/wp-content/uploads/2020/11/my_pic2.png)
---
![avatar](http://ngrok.huazheng.club/wp-content/uploads/2020/11/my_pic3.png)

注意事项
----
> 1. 程序中存在debug函数，禁用后会提升程序运行效率
>
> 2. 程序首次运行会在根目录下生成配置文件，移动配置文件位置会导致保存的设置失效
>
> 3. 部分Linux发行版会出现中文编码问题，请尝试修改地区设置和安装中文字库，若上述方法依旧无法启动，尝试修改程序中文显示内容为英文。

软件架构
----
* Python 3.9 tkinter
  
  > 详情见文档目录

目录结构及说明
----
├── bin		*----------可执行文件* <br>
│   └── register_sprite_v1.1_win64_exe.7z		<br>
├── doc		*----------软件文档目录* <br>
│   ├── 更详细的软件结构说明.txt		<br>
│   └── 更新日志.txt		<br>
├── lib		*----------库文件*<br>
│   ├── __init__.py		<br>
│   ├── _debug.py		*----------调试库*<br>
│   └── _color_operations.py		*----------样式库*<br>
│   └── _file_operations.py		*----------文件操作库*<br>
├── LICENSE		*----------许可证信息<br>
├── main.py		*----------主程序*<br>
├── README.en.md		<br>
├── README.md		<br>
├── user-config.ini	  *----------用户配置文件*	<br>├── run.bat	  *----------batch启动文件	<br>
└── src		*-----------资源目录*<br>

*5 directories, 13 files*

使用到的库
-----
```python
# main.py
import ctypes
import os
from tkinter import *
import tkinter as tk

# _debug.py
import time
from functools import wraps

# _file_operations.py
import configparser

# _color_operations.py
import tkinter as tk
from tkinter import Tk, Label, Button, Toplevel
```


​    
使用说明
----                
* > 软件使用了可视化的操作界面，如果需要更详细的了解使用方法，请查看doc目录下相关文档

加入我们
----
* > 将你的信息发送到我的邮箱（h1657802074@gmail.com），我会亲自查看每一封邮件
  >
  > 你的每一份贡献都是对这个项目极大的帮助

参与贡献
----
@[hz2](https://gitee.com/JensenHua/)
