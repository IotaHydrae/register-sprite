from tkinter import *


class MyGui():
    def __init__(self, Window):
        self.Window = Window
        self.btn_list=[]
        self.btn_num=31
        self.frame = Frame(self.Window)


        #
        self.frame_btn_row1 = Frame(self.Window)
        self.frame_btn_row2 = Frame(self.Window)


    def init_frame(self):
        self.Window.title('寄存器小精灵')
        self.Window.geometry('650x320+100+200')

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


    def init_view(self):
        '''
            这两个for循环并不涉及数据的更改和显示
            仅仅作为占位控件来使按钮易于布局
        '''
        for i in range(19):
            j = abs(i-31)
            Label(self.frame_btn_row1, text='  ', font=("宋体", 8, "bold")).grid(row=5, column=i,
                                                                         sticky=W + E + N + S, padx=7, pady=7)
        for i in range(19):
            j = abs(i-31)
            Label(self.frame_btn_row2, text='  ', font=("宋体", 8, "bold")).grid(row=5, column=i,
                                                                         sticky=W + E + N + S, padx=7, pady=7)

        '''第一部分用来生成31-16位的label和button'''
        pad = 0
        call_mode = 0       # 用来设置是否为第一组控件
        for i in range(4):
            if call_mode == 0:
                self.create_obj_group(self.frame_btn_row1, 0, pad)
                pad += 4
                call_mode = 1   # 第一组控件生成完毕，更改标志位
            else:
                # 生成其余组控件
                self.create_obj_group(self.frame_btn_row1, 0, pad+1)
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
                self.create_obj_group(self.frame_btn_row2, 2, pad+1)
                pad += 5

        # 将第二部分控件pack
        self.frame_btn_row2.pack(side=TOP)

        # 将两部分控件打包
        self.frame.pack(side=LEFT)

        # for i in range(16):
        #
        #     # label 字符
        #     j = abs(i-31)
        #     column = i
        #     Label(self.frame,text=j,font=("宋体", 12, "bold")).grid(row=0,column=column,sticky=W+E+N+S, padx=7, pady=7)
        #     # 创建按钮
        #     obj = Button(self.frame,text='0',width='3',height='2',font=("宋体", 12, "bold"))
        #     obj.config(command=lambda button=obj: self.set_bit(button))
        #     obj.grid(row=1, column=column)
        #     # 将按钮添加到列表中
        #     self.btn_list.append(obj)



        # for i in range(16):
        #     j = abs(i-15)
        #     Label(self.frame,text=j,font=("宋体", 12, "bold")).grid(row=3,column=i,sticky=W+E+N+S, padx=7, pady=7)
        #     obj = Button(self.frame,text='0',width='3',height='2',font=("宋体", 12, "bold"))
        #     obj.config(command=lambda button=obj:self.set_bit(button))
        #     obj.grid(row=4, column=i)
        #     self.btn_list.append(obj)

        '''
        以下代码用来创建下半部分空间，包括x进制的label、Entry和复选框功能区
        frame_show继承自Window
        frame_label用来存放进制的提示区
        frame_entry用来存放进制的回显区
        frame_choice用来存放复选功能
        '''
        self.frame_show = Frame(self.Window)
        self.frame_show.pack()

        self.frame_label = Frame(self.frame_show)
        self.hex = Label(self.frame_label,text="16进制",font=("宋体", 12, "bold"))
        self.hex.pack(side=TOP)
        self.decimal = Label(self.frame_label,text="10进制",font=("宋体", 12, "bold"))
        self.decimal.pack(side=TOP)
        self.octal = Label(self.frame_label,text="8进制",font=("宋体", 12, "bold"))
        self.octal.pack(side=TOP)
        self.binary = Label(self.frame_label,text="2进制",font=("宋体", 12, "bold"))
        self.binary.pack(side=TOP)
        self.frame_label.pack(side=LEFT)

        self.frame_entry = Frame(self.frame_show)
        self.hex_output = Entry(self.frame_entry,width=40,font=("宋体", 12, "bold"))
        self.hex_output.pack(side=TOP)
        self.decimal_output = Entry(self.frame_entry,width=40,font=("宋体", 12, "bold"))
        self.decimal_output.pack(side=TOP)
        self.octal_output = Entry(self.frame_entry,width=40,font=("宋体", 12, "bold"))
        self.octal_output.pack(side=TOP)
        self.binary_output = Entry(self.frame_entry,width=40,font=("宋体", 12, "bold"))

        self.binary_output.pack(side=TOP)

        self.frame_entry.pack(side=LEFT)


        # 这部分代码用来向回显区插入初始数据，并无实际作用
        self.hex_output.insert(0, '0x00000000')
        self.decimal_output.insert(0, '0')
        self.octal_output.insert(0, '0o0')
        self.binary_output['state'] = 'normal'
        self.binary_output.insert(0, '0000 0000 0000 0000 0000 0000 0000 0000')
        self.binary_output['state'] = 'readonly'

        # 这里创建复选框功能区
        self.frame_choice = Frame(self.frame_show)
        self.CheckVar = IntVar()
        self.ck_btn = Checkbutton(self.frame_choice, text="窗口保持在全屏幕的顶部", variable=self.CheckVar, \
                                  onvalue=1, offvalue=0, command=self.isChecked)
        self.ck_btn.pack(side=TOP)
        self.frame_choice.pack(side=TOP)




    def show_data(self):
        self.binary_output['state'] = 'normal'  # 将二进制回显区设置为可写

        '''清空各进制回显区，每次修改前都要先清空'''
        self.hex_output.delete(0, END)
        self.decimal_output.delete(0, END)
        self.octal_output.delete(0, END)
        self.binary_output.delete(0, END)

        # 初始化
        _bin=''
        dec=''
        _oct=''
        _hex=''
        bin_show=''
        space_cnt=0     # bin_show中的空格位计数

        # 遍历按钮数组，将按钮值拼接为字符串，得到一个二进制数据
        # _bin为初始数据
        # bin_show为显示到回显区的数据，因为便于查看，每隔4位插入了一个空格，不能用于进制转换,仅作显示
        for i in self.btn_list:
            _bin+=i['text']
            bin_show+=i['text']
            space_cnt+=1
            if space_cnt == 4:
                bin_show+=' '
                space_cnt=0

        # 进制转换
        dec = int(_bin,2)
        _hex = hex(dec)

        '''
            直接使用hex()函数会得到一个这样的数据 0x7
            而我们要显示这样的                   0x00000007
            其实两者相等，只不过后者更加便于查看
        '''
        temp_str=''     # 临时字符串，用来存放0

        # 根据hex()得到最低为3位的数据，可以得出0的个数，累加到temp_str中
        for n in range(10-len(_hex)):
            temp_str+='0'

        # 拼接字符串，以'x'隔开字符串，取后半部分
        # 0x + n0(n=7) + 0x7.split('x')[1] 等于 7 即 0x00000007
        _hex = '0x'+temp_str+_hex.split('x')[1]

        # 得到8进制数据，八进制在32位cpu中不常用，这里为了功能拓展才添加的
        _oct = oct(dec)

        '''更新各个进制的数据'''
        self.hex_output.insert(0, _hex)
        self.decimal_output.insert(0, dec)
        self.octal_output.insert(0, _oct)
        self.binary_output.insert(0, bin_show)

        self.binary_output['state'] = 'readonly'    # 将二进制回显区设置为只读


    '''
        按钮每次点击都会调用该函数，执行完样式更改后调用数据更新函数
    '''
    def set_bit(self,obj):

        # 根据按钮值更改按钮显示信息
        if obj['text'] == '0':
            obj.config(text='1')
            obj.config(relief='sunken')     # 设置按钮样式为按下
        elif obj['text'] == '1':
            obj.config(text='0')
            obj.config(relief='raised')     # 设置按钮样式为升起

        # 调用数据更新函数
        self.show_data()

    # 窗口置顶函数
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

