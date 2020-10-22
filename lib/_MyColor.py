'''
    @file: _MyColor.py
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
import os
import tkinter as tk
from tkinter import Tk, Label, Button, Toplevel


def ColorInit():
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
    :param color: 颜色参数，见上部列表16进制颜色值后
    :return: selected color
    '''
    color_list = ColorInit()
    for color in color_list:
        more_info_list = color.split(' ')
        # print(more_info_list)
        if (color_in == more_info_list[1]) or (color_in == more_info_list[2]):
            # print(more_info_list[0])
            return more_info_list[0]

# import **************************************************
import random
# from lib import _debug

class ColorChoiceFrame(Toplevel):
    '''
        @file: _MyColor.py
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
        close.config(command=self.destroy)
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
            color_en  = current_color_list[1]
            color_zh  = current_color_list[2]

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
            obj.config(command = lambda button=obj, color=color_zh: self.ChangeBtnStyle(button, color))
            obj.pack(side=tk.LEFT)
            obj.place_forget()

            self.btn_list.append(obj)

    # @_debug.printk()
    def ChangeBtnStyle(self, obj, color):
        # print(color)
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

if __name__ == '__main__':
    # root = tk.Tk()
    # app = ColorChoiceFrame(master=root)
    # app.mainloop()
    # GetColor('橙红色')
    pass