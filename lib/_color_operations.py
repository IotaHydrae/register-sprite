# RegisterSprite  Copyright (C) 2020  jessenhua (h1657802074@gmail.com)

# This file is part of RegisterSprite
#   ____ ____  _      __     _______  ___
#  / ___|  _ \| |     \ \   / /___ / / _ \
# | |  _| |_) | |      \ \ / /  |_ \| | | |
# | |_| |  __/| |___    \ V /  ___) | |_| |
#  \____|_|   |_____|    \_/  |____(_)___/
#
# RegisterSprite is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
    @file: _color_operations.py
    @author: hz
    @version:
    @date: 21-10-2020
    @brief: Color lib for tkinter widgets
'''
'''
    @attention:  Color initials capitalized 
'''
colors = '''#FFB6C1 LightPink 浅粉红
#FFC0CB Pink 粉红
#DC143C Crimson 深红/猩红
#FFF0F5 LavenderBlush 淡紫红
#DB7093 PaleVioletRed 弱紫罗兰红
#FF69B4 HotPink 热情的粉红
#FF1493 DeepPink 深粉红
#C71585 MediumVioletRed 中紫罗兰红
#DA70D6 Orchid 暗紫色/兰花紫
#D8BFD8 Thistle 蓟色
#DDA0DD Plum 洋李色/李子紫
#EE82EE Violet 紫罗兰
#FF00FF Magenta 洋红/玫瑰红
#FF00FF Fuchsia 紫红/灯笼海棠
#8B008B DarkMagenta 深洋红
#800080 Purple 紫色
#BA55D3 MediumOrchid 中兰花紫
#9400D3 DarkViolet 暗紫罗兰
#9932CC DarkOrchid 暗兰花紫
#4B0082 Indigo 靛青/紫兰色
#8A2BE2 BlueViolet 蓝紫罗兰
#9370DB MediumPurple 中紫色
#7B68EE MediumSlateBlue 中暗蓝色/中板岩蓝
#6A5ACD SlateBlue 石蓝色/板岩蓝
#483D8B DarkSlateBlue 暗灰蓝色/暗板岩蓝
#E6E6FA Lavender 淡紫色/熏衣草淡紫
#F8F8FF GhostWhite 幽灵白
#0000FF Blue 纯蓝
#0000CD MediumBlue 中蓝色
#191970 MidnightBlue 午夜蓝
#00008B DarkBlue 暗蓝色
#000080 Navy 海军蓝
#4169E1 RoyalBlue 皇家蓝/宝蓝
#6495ED CornflowerBlue 矢车菊蓝
#B0C4DE LightSteelBlue 亮钢蓝
#778899 LightSlateGray 亮蓝灰/亮石板灰
#708090 SlateGray 灰石色/石板灰
#1E90FF DodgerBlue 闪兰色/道奇蓝
#F0F8FF AliceBlue 爱丽丝蓝
#4682B4 SteelBlue 钢蓝/铁青
#87CEFA LightSkyBlue 亮天蓝色
#87CEEB SkyBlue 天蓝色
#00BFFF DeepSkyBlue 深天蓝
#ADD8E6 LightBlue 亮蓝
#B0E0E6 PowderBlue 粉蓝色/火药青
#5F9EA0 CadetBlue 军兰色/军服蓝
#F0FFFF Azure 蔚蓝色
#E0FFFF LightCyan 淡青色
#AFEEEE PaleTurquoise 弱绿宝石
#00FFFF Cyan 青色
#00FFFF Aqua 浅绿色/水色
#00CED1 DarkTurquoise 暗绿宝石
#2F4F4F DarkSlateGray 暗瓦灰色/暗石板灰
#008B8B DarkCyan 暗青色
#008080 Teal 水鸭色
#48D1CC MediumTurquoise 中绿宝石
#20B2AA LightSeaGreen 浅海洋绿
#40E0D0 Turquoise 绿宝石
#7FFFD4 Aquamarine 宝石碧绿
#66CDAA MediumAquamarine 中宝石碧绿
#00FA9A MediumSpringGreen 中春绿色
#F5FFFA MintCream 薄荷奶油
#00FF7F SpringGreen 春绿色
#3CB371 MediumSeaGreen 中海洋绿
#2E8B57 SeaGreen 海洋绿
#F0FFF0 Honeydew 蜜色/蜜瓜色
#90EE90 LightGreen 淡绿色
#98FB98 PaleGreen 弱绿色
#8FBC8F DarkSeaGreen 暗海洋绿
#32CD32 LimeGreen 闪光深绿
#00FF00 Lime 闪光绿
#228B22 ForestGreen 森林绿
#008000 Green 纯绿
#006400 DarkGreen 暗绿色
#7FFF00 Chartreuse 黄绿色/查特酒绿
#7CFC00 LawnGreen 草绿色/草坪绿
#ADFF2F GreenYellow 绿黄色
#556B2F DarkOliveGreen 暗橄榄绿
#9ACD32 YellowGreen 黄绿色
#6B8E23 OliveDrab 橄榄褐色
#F5F5DC Beige 米色/灰棕色
#FAFAD2 LightGoldenrodYellow 亮菊黄
#FFFFF0 Ivory 象牙色
#FFFFE0 LightYellow 浅黄色
#FFFF00 Yellow 纯黄
#808000 Olive 橄榄
#BDB76B DarkKhaki 暗黄褐色/深卡叽布
#FFFACD LemonChiffon 柠檬绸
#EEE8AA PaleGoldenrod 灰菊黄/苍麒麟色
#F0E68C Khaki 黄褐色/卡叽布
#FFD700 Gold 金色
#FFF8DC Cornsilk 玉米丝色
#DAA520 Goldenrod 金菊黄
#B8860B DarkGoldenrod 暗金菊黄
#FFFAF0 FloralWhite 花的白色
#FDF5E6 OldLace 老花色/旧蕾丝
#F5DEB3 Wheat 浅黄色/小麦色
#FFE4B5 Moccasin 鹿皮色/鹿皮靴
#FFA500 Orange 橙色
#FFEFD5 PapayaWhip 番木色/番木瓜
#FFEBCD BlanchedAlmond 白杏色
#FFDEAD NavajoWhite 纳瓦白/土著白
#FAEBD7 AntiqueWhite 古董白
#D2B48C Tan 茶色
#DEB887 BurlyWood 硬木色
#FFE4C4 Bisque 陶坯黄
#FF8C00 DarkOrange 深橙色
#FAF0E6 Linen 亚麻布
#CD853F Peru 秘鲁色
#FFDAB9 PeachPuff 桃肉色
#F4A460 SandyBrown 沙棕色
#D2691E Chocolate 巧克力色
#8B4513 SaddleBrown 重褐色/马鞍棕色
#FFF5EE Seashell 海贝壳
#A0522D Sienna 黄土赭色
#FFA07A LightSalmon 浅鲑鱼肉色
#FF7F50 Coral 珊瑚
#FF4500 OrangeRed 橙红色
#E9967A DarkSalmon 深鲜肉/鲑鱼色
#FF6347 Tomato 番茄红
#FFE4E1 MistyRose 浅玫瑰色/薄雾玫瑰
#FA8072 Salmon 鲜肉/鲑鱼色
#FFFAFA Snow 雪白色
#F08080 LightCoral 淡珊瑚色
#BC8F8F RosyBrown 玫瑰棕色
#CD5C5C IndianRed 印度红
#FF0000 Red 纯红
#A52A2A Brown 棕色
#B22222 FireBrick 火砖色/耐火砖
#8B0000 DarkRed 深红色
#800000 Maroon 栗色
#FFFFFF White 纯白
#F5F5F5 WhiteSmoke 白烟
#DCDCDC Gainsboro 淡灰色
#D3D3D3 LightGrey 浅灰色
#C0C0C0 Silver 银灰色
#A9A9A9 DarkGray 深灰色
#808080 Gray 灰色
#696969 DimGray 暗淡灰
#000000 Black 纯黑'''

# import **************************************************
import tkinter as tk
from tkinter import Label, Button, Toplevel


def ColorInit():
    """
    初始话颜色列表，将字符串处理为列表
    :return: 颜色列表
    """
    color_list = colors.split('\n')
    return color_list


def ShowColors():
    '''
        返回支持的颜色
    :return:
    '''
    color_list = ColorInit()

    for color in color_list:
        color_info_list = color.split(' ')
        print(color_info_list[1], end=' ')
        print(color_info_list[2])

    choice = input("是否要输出到文件中?")
    if choice == 'yes':
        try:
            file = open('../colors.txt', 'w', encoding='utf-8')
            for color in color_list:
                file.write(color)
                file.write('\n')
            file.close()
            print('已输出到程序根目录下')
        except:
            print('ERROR when creating output file.')
            print('trying create to current dir')
            file = open('colors.txt', 'w', encoding='utf-8')

            for color in color_list:
                file.writelines(color)
            file.close()
            print('已输出到当前目录下')
    else:
        pass


def GetColor(color_in):
    '''
        返回16进制的颜色值
    :param color_in: 颜色参数，见上部列表16进制颜色值后
    :return: selected color
    '''
    color_list = ColorInit()
    for color in color_list:
        more_info_list = color.split(' ')
        # print(more_info_list)
        if (color_in == more_info_list[1]) or (color_in == more_info_list[2]):
            # print(more_info_list[0])
            return more_info_list[0]


SEPARATOR = "===="
# 显示方式
DISPLAY_START_DEFALUT = "\033[0m"
DISPLAY_START_HIGHLIGHT = "\033[1m"
DISPLAY_START_UNDERLINE = "\033[4m"
DISPLAY_START_REVERSE = "\033[7m"

# 前景色
FOREGROUND_START_BLACK = "\033[30m"
FOREGROUND_START_RED = "\033[31m"
FOREGROUND_START_GREEN = "\033[32m"
FOREGROUND_START_YELLOW = "\033[33m"
FOREGROUND_START_BLUE = "\033[34m"
FOREGROUND_START_PLUM = "\033[35m"
FOREGROUND_START_CYAN = "\033[36m"
FOREGROUND_START_WHITE = "\033[37m"

# 背景色
BACKGROUND_START_BLACK = "\033[40m"
BACKGROUND_START_RED = "\033[41m"
BACKGROUND_START_GREEN = "\033[42m"
BACKGROUND_START_YELLOW = "\033[43m"
BACKGROUND_START_BLUE = "\033[44m"
BACKGROUND_START_PLUM = "\033[45m"
BACKGROUND_START_CYAN = "\033[46m"
BACKGROUND_START_WHITE = "\033[47m"
# 结束标志
END_ALL = "\033[0m"


class FontStyle(object):
    def __init__(self):
        pass

    # color_font("Hello World", 7, 32, 44)
    def __render_font(self, text, command):
        # print(command)
        # print(hex(command))
        display_type = command >> 8
        foreground_color = (command & 0xf0) >> 4
        background_color = (command & 0xf)
        # print(display_type, foreground_color, background_color)

        style_start = f"\033[{display_type};3{foreground_color};4{background_color}m"
        style_end = "\033[0m"

        return f"{style_start}{text}{style_end}"

    def color_font(self, text, display_type=None, foreground_color=None, backgroud_color=None):
        """
        改变打印到终端的文本样式
        :param text: 输入的字符串
        :param display_type: 显示方式   -----0: 默认值 1：高亮加粗 4：下划线 7：反显
        :param foreground_color: 前景色 ----30：黑色 31：红色 32：绿色 33：黄色 34：蓝色： 35：梅色 36：青色 37：白色
        :param backgroud_color: 背景色  ----40：黑色 41：红色 42：绿色 44：黄色 44：蓝色： 45：梅色 46：青色 47：白色
        :return: 修改样式后的字符串
        """
        SUPPORT_DISPLAY_TYPE = [0, 1, 4, 7, None]
        SUPPORT_FOREGROUD_COLOR = [30, 31, 32, 33, 34, 35, 36, 37, None]
        SUPPORT_BACKGROUD_COLOR = [40, 41, 42, 43, 44, 45, 46, 47, None]
        error_msg_head = "[   \033[31m WRONG\033[0m  ] "

        tip_display_type = f"0: 默认值 {DISPLAY_START_HIGHLIGHT}1：高亮加粗{END_ALL} {DISPLAY_START_UNDERLINE}4：下划线{END_ALL} {DISPLAY_START_REVERSE}7：反显{END_ALL}"
        tip_foregroud_color = f"{FOREGROUND_START_BLACK}30：黑色{END_ALL} 31：红色 32：绿色 33：黄色 34：蓝色： 35：梅色 36：青色 37：白色"
        tip_backgroud_color = f"40：黑色 41：红色 42：绿色 44：黄色 44：蓝色： 45：梅色 46：青色 47：白色"

        #
        flag_display = True if display_type in SUPPORT_DISPLAY_TYPE else False
        flag_foreground = True if foreground_color in SUPPORT_FOREGROUD_COLOR else False
        flag_background = True if backgroud_color in SUPPORT_BACKGROUD_COLOR else False

        print(
            error_msg_head + f"SUPPORT_DISPLAY_TYPE: {SUPPORT_DISPLAY_TYPE}{SEPARATOR}" + tip_display_type) \
            if not flag_display else None
        print(
            error_msg_head + f"SUPPORT_FOREGROUD_COLOR: {SUPPORT_FOREGROUD_COLOR}{SEPARATOR}" + tip_foregroud_color) \
            if not flag_foreground else None
        print(
            error_msg_head + f"SUPPORT_BACKGROUD_COLOR: {SUPPORT_BACKGROUD_COLOR}{SEPARATOR}" + tip_backgroud_color) \
            if not flag_background else None

        # color_font("Hello World", 7, 32, 44)

        if flag_display and flag_foreground and flag_background:
            command1 = display_type << 8 if display_type != None else 0x0E << 8
            command2 = (foreground_color % 30) << 4 if foreground_color != None else 0x0C << 4
            command3 = (backgroud_color % 40) if backgroud_color != None else 0x0A
            command = command1 | command2 | command3
            return self.__render_font(text, command)
        else:
            return self.__render_font("TRY AGAIN PLEASE", 0)


# import **************************************************
import random


# from lib import _debug

class ColorChoiceFrame(Toplevel):
    '''
        @file: _color_operations.py
        @author: hz
        @version:
        @date: 2020-10-22
        @brief: 样式色彩相关操作

    '''

    # @_debug.printk()
    def __init__(self, master=None):
        super().__init__(master)
        # 设置窗口大小不可更改
        self.resizable(0, 0)
        # 获取master
        self.master = master
        self.title("色彩选择窗口")
        # 生成1~140之间20个不重复的随机数
        self.random_color_list = random.sample(range(1, 140), 20)
        # 全部颜色的列表，总数140
        self.color_list = ColorInit()

        # 颜色选定按钮列表
        self.btn_list = []
        # 选中的颜色值
        self.current_btn_value = ''
        # 要返回给主窗口的list
        self.color_data_list = []

        # UI初始化函数
        self.setupUI()

    # @_debug.printk()
    def setupUI(self):
        # row1 色彩组
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        self.create_obj_group(row1, 0, 5)

        # row2 色彩组
        row2 = tk.Frame(self)
        row2.pack(fill="x")
        self.create_obj_group(row2, 5, 10)

        # row3 色彩组
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        self.create_obj_group(row3, 10, 15)

        # row4 色彩组
        row4 = tk.Frame(self)
        row4.pack(fill="x")
        self.create_obj_group(row4, 15, 20)

        # row5 底部功能区
        row5 = tk.Frame(self)
        row5.pack(fill="x")

        # 关闭按钮
        close = Button(row5,
                       text="关闭",
                       bg='#ffffff',
                       width=5)
        close.config(command=self.destroy_command)
        close.pack(side=tk.RIGHT)
        # 确定按钮
        determine = Button(row5,
                           text="确定",
                           bg="#ffffff",
                           width=5)
        determine.config(command=lambda mode=2: self.SetCurrentColorValue(mode))
        determine.pack(side=tk.RIGHT)
        # 应用按钮
        apply = Button(row5,
                       text="应用",
                       bg="#ffffff",
                       width=5)
        apply.config(command=lambda mode=1: self.SetCurrentColorValue(mode))
        apply.pack(side=tk.RIGHT)

    # @_debug.printk()
    def create_obj_group(self, frame, start, end):
        # 前向数据梳理
        this_color_list = []
        for num in range(start, end):
            # 获取随机数下标
            random_color_index = self.random_color_list[num]
            # 筛选随机颜色
            this_color_list.append(self.color_list[random_color_index])

        # print(this_color_list)

        '''
            行控件生成 结构：
            占位符|Label标签|选定按钮
        '''
        for count in range(5):
            current_color_list = this_color_list[count].split(' ')
            color_hex = current_color_list[0]
            color_en = current_color_list[1]
            color_zh = current_color_list[2]

            # 占位符
            Label(frame, text=' ', width=1).pack(side=tk.LEFT)
            # 颜色label
            Label(frame,
                  text=color_zh,
                  fg="#000000",
                  bg=color_hex,
                  width=7).pack(side=tk.LEFT)

            # 颜色选中按钮
            obj = Button(frame,
                         text='×',
                         width=3)
            obj.config(command=lambda button=obj, color=color_zh: self.ChangeBtnStyle(button, color))
            obj.pack(side=tk.LEFT)
            obj.place_forget()

            self.btn_list.append(obj)

    # @_debug.printk()
    def ChangeBtnStyle(self, obj, color):
        '''
            按钮样式更改函数，更改时同样需要检测是否存在已按下按钮
        '''
        status = self.CheckIfOtherBtnIsSunken()
        if obj['text'] == '×':

            if not status:
                obj['text'] = '√'
                obj.config(relief='sunken')  # 设置按钮样式为按下
                self.current_btn_value = color
        else:
            obj['text'] = '×'
            obj.config(relief='raised')  # 设置按钮样式为升起

    # @_debug.printk()
    def CheckIfOtherBtnIsSunken(self):
        '''
            检查是否有其他按钮已经被按下
        '''
        for btn in self.btn_list:
            if btn['text'] == '√':
                return True
            else:
                pass
        return False

    # @_debug.printk()
    def SetCurrentColorValue(self, mode):

        if mode == 1:
            for btn in self.btn_list:
                if btn['text'] == '√':
                    self.color_data_list.clear()
                    self.color_data_list.append(self.current_btn_value)
        elif mode == 2:
            for btn in self.btn_list:
                if btn['text'] == '√':
                    self.color_data_list.clear()
                    self.color_data_list.append(self.current_btn_value)
            self.destroy()
        else:
            pass

    def destroy_command(self):
        self.color_data_list.clear()
        self.current_btn_value="None"
        self.color_data_list.append("None")
        self.destroy()


if __name__ == '__main__':
    # root = tk.Tk()
    # app = ColorChoiceFrame(master=root)
    # app.mainloop()
    # GetColor('橙红色')

    font = FontStyle()
    print(font.color_font("Hello World!", display_type=8))      # 下划线
    print(font.color_font("Hello World!", display_type=7))      # 反显
    print(font.color_font("Hello World!", foreground_color=32))     # 绿色前景
    print(font.color_font("Hello World!", foreground_color=36, backgroud_color=43))     # 青色前景，黄色背景
    print(font.color_font("Hello World!", backgroud_color=44))      # 蓝色背景
    # 反显，红色前景变红色背景，青色背景变青色亲啊前景
    print(font.color_font("Hello World!", display_type=7, foreground_color=31, backgroud_color=46))
    pass
