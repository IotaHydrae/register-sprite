from tkinter import *

QWORD = 64
DWORD = 32
WORD = 16


class MyGui():
    def __init__(self, Window):
        self.Window = Window  # 主窗体
        self.btn_list = []  # 位按钮列表
        self.btn_num = 31  # 按钮顶部label字符
        self.cpu_word_length = DWORD  # 默认CPU字长
        self.frame = Frame(self.Window)

        # 31-16 和 15-0 位按钮
        self.frame_btn_row1 = Frame(self.Window)
        self.frame_btn_row2 = Frame(self.Window)

    def init_frame(self):
        self.Window.title('寄存器小精灵')
        # 长宽 和 xy偏移
        width = 650
        height = 350
        offset_x = 100
        offset_y = 200
        self.Window.geometry('{0}x{1}+{2}+{3}'.format(width, height, offset_x, offset_y))

    def create_obj_group(self, frame, row, column):
        # 4次循环
        for i in range(4):
            # print(i)
            # j = abs(i - 31)  这里原用来设置各按键上部label字符，后来改用了全局变量的方式
            Label(frame, text=self.btn_num, font=("宋体", 9, "bold")).grid(row=row, column=column + i,
                                                                         sticky=W + E + N + S, padx=7, pady=7)
            # 创建按钮
            obj = Button(frame, text='0', width='3', height='2', font=("宋体", 9, "bold"))

            '''
                这是for循环生成按钮，同时单独操作每个按钮的解决方案
                lambda button=obj: self_bit(button)
                这样每个按钮被点击时都会有自己独立的调用方式——将自己传给处理函数
                
            '''
            obj.config(command=lambda button=obj: self.set_bit(button))
            obj.grid(row=row + 1, column=column + i)

            # label上显示的字符减一
            self.btn_num -= 1
            # 将按钮添加到 总按钮列表用  数据更新函数会遍历列表取得二进制数据
            self.btn_list.append(obj)

    '''
        控件生成函数
    '''

    def init_view(self):
        '''
            这两个for循环并不涉及数据的更改和显示
            仅仅作为占位控件来使按钮易于布局
        '''
        for i in range(19):
            j = abs(i - 31)
            Label(self.frame_btn_row1, text='  ', font=("宋体", 8, "bold")).grid(row=5, column=i,
                                                                               sticky=W + E + N + S, padx=7, pady=7)
        for i in range(19):
            j = abs(i - 31)
            Label(self.frame_btn_row2, text='  ', font=("宋体", 8, "bold")).grid(row=5, column=i,
                                                                               sticky=W + E + N + S, padx=7, pady=7)

        '''第一部分用来生成31-16位的label和button'''
        pad = 0
        call_mode = 0  # 用来设置是否为第一组控件
        for i in range(4):
            if call_mode == 0:
                self.create_obj_group(self.frame_btn_row1, 0, pad)
                pad += 4
                call_mode = 1  # 第一组控件生成完毕，更改标志位
            else:
                # 生成其余组控件
                self.create_obj_group(self.frame_btn_row1, 0, pad + 1)
                pad += 5

        # 将第一部分控件pack
        self.frame_btn_row1.pack(side=TOP)

        '''第二部分用来生成15-0位的label和button， 相关解释看第一部分'''
        pad = 0
        call_mode = 0
        for i in range(4):
            if call_mode == 0:
                self.create_obj_group(self.frame_btn_row2, 2, pad)
                pad += 4
                call_mode = 1
            else:
                self.create_obj_group(self.frame_btn_row2, 2, pad + 1)
                pad += 5

        # 将第二部分控件pack
        self.frame_btn_row2.pack(side=TOP)

        # 将两部分控件打包
        self.frame.pack(side=LEFT)

        '''
        以下代码用来创建下半部分空间，包括x进制的label、Entry和复选框功能区
        frame_show继承自Window
        frame_label用来存放进制的提示区
        frame_entry用来存放进制的回显区
        frame_choice用来存放复选功能
        '''
        self.frame_show = Frame(self.Window)
        self.frame_show.pack()

        # 进制label区
        self.frame_label = Frame(self.frame_show)
        self.hex = Label(self.frame_label, text="16进制", font=("宋体", 12, "bold"))
        self.hex.pack(side=TOP)
        self.decimal = Label(self.frame_label, text="10进制", font=("宋体", 12, "bold"))
        self.decimal.pack(side=TOP)
        self.octal = Label(self.frame_label, text="8进制", font=("宋体", 12, "bold"))
        self.octal.pack(side=TOP)
        self.binary = Label(self.frame_label, text="2进制", font=("宋体", 12, "bold"))
        self.binary.pack(side=TOP)

        # 进制换算区
        self.frame_entry = Frame(self.frame_show)
        self.hex_output = Entry(self.frame_entry, width=40, font=("宋体", 12, "bold"))
        self.hex_output.pack(side=TOP)
        self.decimal_output = Entry(self.frame_entry, width=40, font=("宋体", 12, "bold"))
        self.decimal_output.pack(side=TOP)
        self.octal_output = Entry(self.frame_entry, width=40, font=("宋体", 12, "bold"))
        self.octal_output.pack(side=TOP)
        self.binary_output = Entry(self.frame_entry, width=40, font=("宋体", 12, "bold"))
        self.binary_output.pack(side=TOP)

        '''
            拓展功能区，主要拓展如下
            十六进制以位位移形式显示
        '''
        # 置位
        self.label_hex_shift_set = Label(self.frame_label, text="置位", font=("宋体", 10))
        self.label_hex_shift_set.pack(side=TOP, pady=5)
        self.entry_hex_shift_set = Entry(self.frame_entry, width=45, font=("宋体", 10, "bold"))
        self.entry_hex_shift_set.pack(side=TOP, pady=5)

        # 清零
        self.label_hex_shift_clear = Label(self.frame_label, text="清零", font=("宋体", 10))
        self.label_hex_shift_clear.pack(side=TOP)
        self.entry_hex_shift_clear = Entry(self.frame_entry, width=45, font=("宋体", 10, "bold"))
        self.entry_hex_shift_clear.pack(side=TOP)

        self.frame_label.pack(side=LEFT)
        self.frame_entry.pack(side=LEFT)

        self.init_value()

        # 这里创建复选框功能区
        self.frame_choice = Frame(self.frame_show)
        self.CheckVar = IntVar()
        self.ck_btn = Checkbutton(self.frame_choice, text="窗口保持在全屏幕的顶部", variable=self.CheckVar, \
                                  onvalue=1, offvalue=0, command=self.isChecked)
        self.ck_btn.pack(side=TOP)

        # 左移功能按钮
        self.lsh_btn = Button(self.frame_choice, text="左移")
        self.lsh_btn.config(command=self.left_shift)
        self.lsh_btn.pack(side=LEFT)

        # 右移功能按键
        self.rsh_btn = Button(self.frame_choice, text="右移")
        self.rsh_btn.config(command=self.right_shift)
        self.rsh_btn.pack(side=LEFT)

        # 求非功能按键
        self.not_btn = Button(self.frame_choice, text="求非")
        self.not_btn.config(command=self.calc_not)
        self.not_btn.pack(side=LEFT)

        # 复位功能按键
        self.rst_btn = Button(self.frame_choice, text="复位")
        self.rst_btn.config(command=self.bit_reset)
        self.rst_btn.pack(side=LEFT)

        # 复选框区域打包
        self.frame_choice.pack(side=TOP)

    '''
        数据初始化函数
    '''

    def init_value(self):
        # 这部分代码用来向回显区插入初始数据，并无实际作用
        self.binary_output['state'] = 'normal'
        self.hex_output.insert(0, '0x00000000')
        self.decimal_output.insert(0, '0')
        self.octal_output.insert(0, '0o0')
        self.binary_output['state'] = 'normal'
        self.binary_output.insert(0, '0000 0000 0000 0000 0000 0000 0000 0000')
        self.binary_output['state'] = 'readonly'

        self.entry_hex_shift_set.insert(0, '0')
        self.entry_hex_shift_clear.insert(0, '0')
        self.binary_output['state'] = 'readonly'

    '''
        数据清除函数
    '''

    def clear_value(self):
        '''清空各进制回显区，每次修改前都要先清空'''
        self.binary_output['state'] = 'normal'
        self.hex_output.delete(0, END)
        self.decimal_output.delete(0, END)
        self.octal_output.delete(0, END)
        self.binary_output.delete(0, END)

        self.entry_hex_shift_set.delete(0, END)
        self.entry_hex_shift_clear.delete(0, END)
        self.binary_output['state'] = 'readonly'

    '''
        show_data 数据显示函数
        该函数用来将按钮数据处理后显示到进制换算区
    '''

    def show_data(self):
        self.clear_value()
        self.binary_output['state'] = 'normal'  # 将二进制回显区设置为可写

        # 初始化
        _bin = self.get_bin_value(mode='normal')
        not_bin = self.get_bin_value(mode='not')
        _oct = ''
        _hex = ''
        bin_show = self.get_bin_value(mode='show')

        # 进制转换
        dec = int(_bin, 2)
        not_dec = int(not_bin, 2)
        _hex = hex(dec)
        not_hex = hex(not_dec)
        '''
            直接使用hex()函数会得到一个这样的数据 0x7
            而我们要显示这样的                   0x00000007
            其实两者相等，只不过后者更加便于查看
        '''
        temp_str = ''  # 临时字符串，用来存放0
        temp_str_not = ''
        # 根据hex()得到最低为3位的数据，可以得出0的个数，累加到temp_str中
        for n in range(10 - len(_hex)):
            temp_str += '0'

        # 拼接字符串，以'x'隔开字符串，取后半部分
        # 0x + n0(n=7) + 0x7.split('x')[1] 等于 7 即 0x00000007
        _hex = '0x' + temp_str + _hex.split('x')[1]
        not_hex = '0x' + temp_str_not + not_hex.split('x')[1]

        # 得到8进制数据，八进制在32位cpu中不常用，这里为了功能拓展才添加的
        _oct = oct(dec)

        '''
            进阶功能区数据处理
            这部分的思路是将二进制数据每四个分为一组处理，32位模式下共8组
            这里并没有考虑其他字长模式cpu的情况，后期如果添加其他字长模式要修改这部分代码
        '''
        # 置位数据处理
        hex_bit_dict = {}  # 总16进制数据字典
        hex_bit_list = bin_show.split(' ')[:8]
        bit_index = 7  # 32位模式  8组4位二进制数据

        # 遍历列表将数据以如下形式保存到字典中
        # 7:0000  6:0000
        for hex_bit in hex_bit_list:
            hex_bit_dict[bit_index] = hex_bit
            bit_index -= 1

        # 获取有效值，即不为0的组
        current_value_dict = {}  # 有效值字典

        # 遍历上一步得到的字典，得到有效值字典
        for key in hex_bit_dict:
            if hex_bit_dict[key] != '0000':
                current_value_dict[key] = hex_bit_dict[key]

        # 获得字典长度，后边判断显示格式会用到
        len_current_value_dict = len(current_value_dict)

        # 要拼接显示的到置位区的字符串，格式如下
        # （1 << 10） | (3 << 12)
        current_value_str = ''

        # 根据字典长度处理字符串格式
        if len_current_value_dict == 1:
            for pkey in current_value_dict:
                current_hex_value = hex(int(current_value_dict[pkey], 2))
                current_value_str += '({0}<<{1})'.format(current_hex_value, pkey * 4)
        elif len_current_value_dict > 1:
            for pkey in current_value_dict:
                current_hex_value = hex(int(current_value_dict[pkey], 2))
                current_value_str += '|({0}<<{1})'.format(current_hex_value, pkey * 4)
            current_value_str = current_value_str[1:]
        else:
            pass

        # 清零数据处理在遍历按钮和进制转换时已经处理完成

        '''
            更新数据
        '''
        self.hex_output.insert(0, _hex)
        self.decimal_output.insert(0, dec)
        self.octal_output.insert(0, _oct)
        self.binary_output.insert(0, bin_show)

        # 更新进阶功能区
        self.entry_hex_shift_set.insert(0, current_value_str)
        self.entry_hex_shift_clear.insert(0, not_hex)
        self.binary_output['state'] = 'readonly'  # 将二进制回显区设置为只读

    '''
        按钮每次点击都会调用该函数，执行完样式更改后调用数据更新函数
    '''

    def set_bit(self, obj):

        # 根据按钮值更改按钮显示信息
        if obj['text'] == '0':
            obj.config(text='1')
        elif obj['text'] == '1':
            obj.config(text='0')

        # 调用数据更新函数
        self.update_btn_style()
        self.show_data()

    '''
        mode
            normal : 二进制数据
            not    : 求非后的二进制数据
            bin_show  :  用于显示给用户的二进制数据
    '''

    def get_bin_value(self, mode):
        # 遍历按钮数组，将按钮值拼接为字符串，得到一个二进制数据
        # _bin为初始数据
        # bin_show为显示到回显区的数据，因为便于查看，每隔4位插入了一个空格，不能用于进制转换,仅作显示
        _bin = ''
        not_bin = ''
        bin_show = ''
        space_cnt = 0

        for i in self.btn_list:
            if i['text'] == '1':
                _bin += i['text']
                bin_show += i['text']
                not_bin += '0'
                space_cnt += 1
            elif i['text'] == '0':
                _bin += i['text']
                bin_show += i['text']
                not_bin += '1'
                space_cnt += 1

            if space_cnt == 4:
                bin_show += ' '
                space_cnt = 0

        if mode == 'normal':
            return _bin
        elif mode == 'not':
            return not_bin
        else:
            return bin_show

    '''
        按钮样式更新函数
    '''

    def update_btn_style(self):
        for btn in self.btn_list:
            if btn['text'] == '0':
                btn.config(relief='raised')  # 设置按钮样式为升起
            else:
                btn.config(relief='sunken')  # 设置按钮样式为按下

    '''
        复位功能函数
    '''

    def bit_reset(self):
        # 遍历按钮列表，将按钮恢复至初始状态，即数值0样式为升起
        for btn in self.btn_list:
            btn.config(text='0')

        self.update_btn_style()
        '''
            复位的数据处理其实可以有很多种方法，这里提供了两种
            1.先清除显示区，再插入初始值
            2.直接调用show_data()函数处理按钮数据
            两种方法最终效果都差不多，但是前者的资源开销应该小一点
        '''
        self.clear_value()  # 清除数据
        self.init_value()  # 初始化数据
        # self.show_data()

    '''
        求非功能函数
    '''

    def calc_not(self):
        # 遍历按钮列表,反转按钮值和样式
        for btn in self.btn_list:
            if btn['text'] == '0':
                btn.config(text='1')
            else:
                btn.config(text='0')

        self.update_btn_style()
        # 这里直接调用数据处理显示函数就行了
        self.show_data()

    '''
        左右移位这个功能
    '''

    def left_shift(self):
        # 得到二进制数据
        _bin = self.get_bin_value(mode='normal')
        # 左移数据
        _bin += '0'
        _bin = _bin[1:]

        # 更新数据
        cnt = 0
        for bit in _bin:
            self.btn_list[cnt]['text'] = bit
            cnt += 1

        # 显示更新
        self.update_btn_style()
        self.show_data()

    def right_shift(self):
        print('right_shift called！')
        # 得到二进制数据
        _bin = self.get_bin_value(mode='normal')
        # 右移数据处理
        origin_bin = '0'
        origin_bin += _bin
        _bin = origin_bin[:32]

        # 更新数据
        cnt = 0
        for bit in _bin:
            self.btn_list[cnt]['text'] = bit
            cnt += 1

        # 显示更新
        self.update_btn_style()
        self.show_data()


    '''
        窗口置顶函数
    '''
    def isChecked(self):
        val = self.CheckVar.get()
        if val == 1:
            # 窗口保持在全屏幕的顶部
            self.Window.attributes("-toolwindow", 1)
            self.Window.wm_attributes("-topmost", 1)
        else:
            # 取消 窗口保持在全屏幕的顶部
            self.Window.attributes("-toolwindow", 0)
            self.Window.wm_attributes("-topmost", 0)


def guiStart():
    window = Tk()
    window.resizable(0, 0)
    frame = MyGui(window)
    frame.init_frame()
    frame.init_view()
    window.mainloop()


if __name__ == '__main__':
    guiStart()
