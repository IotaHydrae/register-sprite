# **寄存器小精灵**

寄存器小精灵（Register Sprite）基于**python tkinter**编写，具有良好的界面和一些简单的交互功能，它可以轻松实现**10进制**、**16进制**、**8进制**和**2进制**之间的转换，方便用于学习各种嵌入式寄存器的位配置，嵌入式工程师的**必备神器**。
我提供了使用**pyinstaller**构建好的可执行文件，当然你也可以**修改后**构建自己的EXE文件

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
│   ├── __pycache__		<br>
│   │   ├── __init__.cpython-39.pyc		<br>
│   │   ├── _debug.cpython-39.pyc		<br>
│   │   └── _MyColor.cpython-39.pyc		<br>
│   ├── _debug.py		*----------调试库*<br>
│   └── _MyColor.py		*----------样式库*<br>
├── LICENSE		<br>
├── main.py		*----------主程序*<br>
├── README.en.md		<br>
├── README.md		<br>
└── src		*-----------资源目录*<br>

*5 directories, 13 files*

使用到的库
-----
> functools
> time
> tkinter

安装教程
----

* 设备中已有Python环境
  
    > 通过本地python解释器直接运行main.py文件
    >
    > `python main.py `
    
* 设备中未安装Python环境
  
    > 作者提供了位于bin目录下构建好的exe文件，暂时只支持x86平台            
              
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
