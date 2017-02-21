#
#  GUI.py
#
#  Copyright2014 Mosaic Team Alex <zfmedisonxfmt@126.com>
#
#  This program is the Graphical User Interface
#  Please start with this program
from tkinter import*
from tkinter.ttk import*
from tkinter.messagebox import*
from GUIplus.Cut_Copy_Paste import*
import Sentence_Segmentation
import WORD_SEG
import Extra_Windows


#
#  name: App
#
#  Main window class, inherited from Tk class

class App(Tk):

#
#  name: App.showcopyright
#  @param       None
#  @return      None
#
#  The next four functions create four Toplevels which are used to
#  show copyright, show help of main window, show help of menu and
#  show welcome respectively
    def showcopyright(self):
        self.toplevel = Toplevel(background='White')
        self.toplevel.title('版权信息')
        self.toplevel.iconbitmap('logo.ico')
        self.toplevel.geometry('360x400')

        self.toplevel.alpha_ = 0
        self.toplevel.attributes('-alpha',0)
        self.toplevel.after(1,self.fade_in_toplevel)
        
        self.toplevel.resizable(width=False,height=False)
        label_1 = Label(self.toplevel,image=self.logo)
        label_1.place(relx=0.08,rely=0.07)
        label_2 = Label(self.toplevel,background='White',text="""
    中文分词器
    版本号：Final Beta1
    
    制作者：Mosaic Team
            成员：宋肇哲 瞿文浩 张福明
           
    联系我们：
            E-mail: songzhaozhe@126.com
            QQ: 407482446

    特别感谢：骆铮@灰天飞雁
    
    
    版权所有2014 Mosaic Team保留所有权利。 
    """)
        label_2.place(relx=0.2,rely=0.075)
        button = Button(self.toplevel,text='关闭',command=self.toplevel.destroy)
        button.place(relx=0.7,rely=0.85)
        self.toplevel.mainloop()

#
#  name: App.showhelp
#  @param       event       <class 'tkinter.Event'>   
#  @return      None
    def showhelp(self,event=None):
        self.toplevel = Toplevel(background='White')
        self.toplevel.title('帮助·主界面')
        self.toplevel.iconbitmap('logo.ico')
        self.toplevel.geometry('360x450')

        self.toplevel.alpha_ = 0
        self.toplevel.attributes('-alpha',0)
        self.toplevel.after(1,self.fade_in_toplevel)
        
        self.toplevel.resizable(width=False,height=False)
        label_1 = Label(self.toplevel,image=self.logo)
        label_1.place(relx=0.06,rely=0.045)
        label_2 = Label(self.toplevel,background='White',text="""
    中文分词器·主界面

    "一键分词"    对"原文"文本框中内容进行分词，
                     结果将在"结果"文本框中显示;

    "段落分句"    对"原文"文本框中内容进行分句,
                     结果将在"结果"文本框中显示;

    "逐句分词"    对"结果"文本框中内容进行分词，
                     将打开新的"逐句分词"界面;

    "清空全部"    清空所有文本框中的内容;

    "文件分词"    选择读取路径，然后选择存储路径并
                    命名文件，对读取的文本进行自动分词；
                    (注意:请将文件格式命名为.txt)

    "结果存储"    存储"结果"文本框中内容，选择
                     存储路径并命名文件;
                     (注意:请将文件格式命名为.txt)

    *菜单功能介绍请参阅菜单"关于"-"菜单介绍"
    *文本框有右键菜单选项
    """)
        label_2.place(relx=0.18,rely=0.03)
        button = Button(self.toplevel,text='关闭',command=self.toplevel.destroy)
        button.place(relx=0.7,rely=0.9)
        self.toplevel.mainloop()

#
#  name: App.showmenu
#  @param       None
#  @return      None
    def showmenu(self):
        self.toplevel = Toplevel(background='White')
        self.toplevel.title('菜单介绍')
        self.toplevel.iconbitmap('logo.ico')
        self.toplevel.geometry('360x400')

        self.toplevel.alpha_ = 0
        self.toplevel.attributes('-alpha',0)
        self.toplevel.after(1,self.fade_in_toplevel)
        
        self.toplevel.resizable(width=False,height=False)
        label_1 = Label(self.toplevel,image=self.logo)
        label_1.place(relx=0.06,rely=0.045)
        label_2 = Label(self.toplevel,background='White',text="""
    中文分词器·菜单介绍
    
    "文件"
    "读入文本"    读取txt文件内容到"原文"文本框
                    
    "词典" 
    "添加新词"    请将词语输入到文本框中，选择
                     词语类型，点击"添加"按钮

    "删除原词"    请将词语输入到文本框中，点击
                     "删除"按钮

    *文本框有右键菜单选项
    """)
        label_2.place(relx=0.18,rely=0.03)
        button = Button(self.toplevel,text='关闭',command=self.toplevel.destroy)
        button.place(relx=0.7,rely=0.9)
        self.toplevel.mainloop()

#
#  name: App.welcome
#  @param       None
#  @return      None
    def welcome(self):
        self.toplevel = Toplevel(background='White')
        self.toplevel.title('欢迎')
        self.toplevel.iconbitmap('logo.ico')
        self.toplevel.geometry('360x200')
        
        self.toplevel.alpha_ = 0
        self.toplevel.attributes('-alpha',0)
        self.toplevel.after(1,self.fade_in_toplevel)
        
        self.toplevel.resizable(width=False,height=False)
        label_1 = Label(self.toplevel,image=self.logo)
        label_1.place(relx=0.08,rely=0.1)
        label_2 = Label(self.toplevel,background='White',text="""
    欢迎您使用中文分词器！

        
    左键点击主界面左上方图标以更换主题；
    右键点击主界面左上方图标以显示帮助。   
    """)
        label_2.place(relx=0.2,rely=0.075)
        button = Button(self.toplevel,text='关闭',command=self.toplevel.destroy)
        button.place(relx=0.7,rely=0.8)
        self.toplevel.mainloop()

#
#  name: App.change_bg
#  @param       None
#  @return      None
#
#  The next three functions are used to change the background and 
#  have the main window and Toplevels fade in
    def change_bg(self,event):
        bg2add = {0:'bg_1.png',1:'bg_2.png',2:'bg_3.png',3:'bg_4.png',4:'bg_5.png',5:'bg_6.png',6:'bg_7.png',7:'bg_8.png'}
        if self.bg_num > 7:
            self.bg_num = 0
        self.bg = PhotoImage(file=bg2add[self.bg_num])
        self.img.create_image(330,290,image=self.bg,anchor='center')
        self.img.place(in_=self)
        self.bg_num +=1

#
#  name: App.fade_in
#  @param       None
#  @return      None
    def fade_in(self):
        if self.alpha_ < 1:
            self.alpha_ += 0.1
            self.attributes('-alpha',self.alpha_)
            self.after(25,self.fade_in)

#
#  name: App.fade_in_toplevel
#  @param       None
#  @return      None
    def fade_in_toplevel(self):
        if self.toplevel.alpha_ < 1:
            self.toplevel.alpha_ += 0.1
            self.toplevel.attributes('-alpha',self.toplevel.alpha_)
            self.toplevel.after(25,self.fade_in_toplevel)

#
#  name: App.button_sentence_split
#  @param       None
#  @return      None
#
#  The next function is called when the button '段落分句' in the main window
#  is pressed, and it calls the function named 'sentence_segment' defined
#  in the file 'Sentence_Segmentation' to split the text into sentences
    def button_sentence_split(self):
        self.text_2.delete('1.0','end')
        self.passage=self.text_1.get('1.0','end')
        self.passagelist=Sentence_Segmentation.sentence_segment(self.passage)
        self.passagelist.reverse()
        for i in self.passagelist:
            self.text_2.insert(0.0,i+'\n')
        self.passagelist.reverse()

#
#  name: App.button_word_split
#  @param       None
#  @return      None
#
#  The next function is called when the button '逐句分词' in the main window
#  is pressed, and it calls the class named 'ss_Window' defined in the file
#  'Extra_Windows' to create a Toplevel
    def button_word_split(self):
        Extra_Windows.ss_Window(self.passagelist)

#
#  name: App.button_sentence_word_split
#  @param       None
#  @return      None
#
#  The next function is called when the button '一键分词' in the main window
#  is pressed, and it calls the function named 'sentence_segment' defined
#  in the file 'Sentence_Segmentation' then the function namend 'participle'
#  defined in the file 'participle' to split the text into words
    def button_sentence_word_split(self):
        self.text_2.delete('1.0','end')
        a=self.text_1.get('1.0','end')
        b=Sentence_Segmentation.sentence_segment(a)
        b.reverse()
        for i in range(len(b)):
            c=WORD_SEG.word_seg(b[i])
            self.text_2.insert(0.0,c+'\n')
            
#
#  name: App.menu_read_file
#  @param       None
#  @return      None
#
#  The next function is called when the item '读入文本' in the menu is pressed,
#  and it will show the text read from the chosen path in the upper textbox
#  in the main window
    def menu_read_file(self):
        read_file=Extra_Windows.loadfile()
        if read_file == None:
            pass
        else:
            self.text_1.delete('1.0','end')
            self.text_1.insert(0.0,read_file)

#
#  name: App.menu_save_file
#  @param       None
#  @return      None
#
#  The next function is called when the item '结果存储' in the menu or the button
#  '结果存储' in the main window is pressed, and it will show the text read from
#  the chosen path in the upper textbox in the main window
    def menu_save_file(self):
        save_file=self.text_2.get('1.0','end')
        s=Extra_Windows.savefile()
        if s == None:
            pass
        else:
            g=open(s,'w')
            g.write(save_file)
            g.close()

#
#  name: App.button_delete_all
#  @param       None
#  @return      None
#
#  The next function is called when the item '清空全部' in the main window is
#  pressed, and it will delete all the contents in both of the textboxes
    def button_delete_all(self):
        self.text_1.delete('1.0','end')
        self.text_2.delete('1.0','end')
        self.passagelist=[]

#
#  name: App.__init__
#  @param       None
#  @return      None
#
#  Initialize the main window and add several objects to it
#  The window will never terminate until the window is closed!
    def __init__(self):
        Tk.__init__(self)
        
        self.alpha_ = 0
        self.attributes('-alpha',0)
        self.after(1,self.fade_in)
        
        self.title('中文分词器')
        self.geometry('660x580')
        self.resizable(width=False,height=False)
        self.option_add('Font','微软雅黑')
        self.iconbitmap('logo.ico')

        self.bg = PhotoImage(file='bg_1.png')
        self.img = Canvas(self,width=660,height=580)
        self.img.create_image(330,290,image=self.bg)
        self.img.place(x=0,y=0,relwidth=1,relheight=1)
        self.bg_num =1
        
        self.logo=PhotoImage(file='logo_1.png')
        self.button_logo = Button(self,image=self.logo)
        self.button_logo.bind('<Button-1>',self.change_bg)
        self.button_logo.bind('<Button-3>',self.showhelp)
        self.button_logo.grid(row=0,column=0)

# create menus in the main window
        menu_1 = Menu(self)        
        menu_2 = Menu(menu_1,tearoff = 0)
        menu_2.add_command(label='文件分词',command=Extra_Windows.processfile)
        menu_2.add_separator()
        menu_2.add_command(label='读入文本',command=self.menu_read_file)
        menu_2.add_command(label='结果存储',command=self.menu_save_file)
        menu_2.add_separator()
        menu_2.add_command(label='退出界面',command=self.destroy)
        
        menu_3 = Menu(menu_1,tearoff = 0)
        #menu_3.add_command(label='读入词典')
        #menu_3.add_separator()
        menu_3.add_command(label='添加新词',command=Extra_Windows.add_dict_Window)
        menu_3.add_command(label='删除原词',command=Extra_Windows.del_dict_Window)

        #menu_4 = Menu(menu_1,tearoff = 0)
        #menu_4.add_command(label='读入规则')
        #menu_4.add_separator()
        #menu_4.add_command(label='更改规则',command=Extra_Windows.change_rule_Window)

        menu_5 = Menu(menu_1,tearoff = 0)
        menu_5.add_command(label='欢迎',command = self.welcome)
        menu_5.add_command(label='版权信息',command = self.showcopyright)
        menu_5.add_separator()
        menu_5.add_command(label='菜单介绍',command = self.showmenu)
        menu_5.add_command(label='帮助',command = self.showhelp)

        menu_1.add_cascade(label = '文件',menu = menu_2)
        menu_1.add_cascade(label = '词典',menu = menu_3)
        #menu_1.add_cascade(label = '规则',menu = menu_4)
        menu_1.add_cascade(label = '关于',menu = menu_5)
        self['menu']= menu_1

#  create buttons in the main window
        self.button_1 = Button(self,text = '一键分词',command=self.button_sentence_word_split)
        self.button_1.grid(row=3,column=1,pady=4)
        self.button_2 = Button(self,text = '段落分句',command=self.button_sentence_split)
        self.button_2.grid(row=3,column=2)
        self.button_3 = Button(self,text = '逐句分词',command=self.button_word_split)
        self.button_3.grid(row=3,column=3)
        self.button_4 = Button(self,text = '清空全部',command=self.button_delete_all)
        self.button_4.grid(row=3,column=4)
        self.button_5 = Button(self,text = '文件分词',command=Extra_Windows.processfile)
        self.button_5.grid(row=3,column=5)
        self.button_6 = Button(self,text = '结果存储',command=self.menu_save_file)
        self.button_6.grid(row=3,column=6)

#  create labels in the main window
        self.label_1 = Label(self,text='原文',background='white',foreground='grey')
        self.label_1.grid(row=1,column=1,columnspan=6,ipadx=268,ipady=4,sticky=W)
        self.label_2 = Label(self,text='结果',background='white',foreground='grey')
        self.label_2.grid(row=4,column=1,columnspan=6,ipadx=268,ipady=4,sticky=W)

#  create textboxes and scroll bars in the main window
        self.scr_1 = Scrollbar(self)
        self.text_1 = TextPlus(self,width=80,height=15,relief=FLAT,yscrollcommand=self.scr_1.set)
        self.scr_1.config(command=self.text_1.yview)
        self.text_1.insert(0.0,'Hi,Astrid!\n')
        self.text_1.grid(row=2,column=1,columnspan=6)
        self.scr_1.grid(row=2,column=7,ipady=74)

        self.scr_2 = Scrollbar(self)
        self.text_2 = TextPlus(self,width=80,height=15,relief=FLAT,yscrollcommand=self.scr_2.set)
        self.scr_2.config(command=self.text_2.yview)
        self.text_2.insert(0.0,'Hi,Astrid!\n')
        self.text_2.grid(row=5,column=1,columnspan=6)
        self.scr_2.grid(row=5,column=7,ipady=74)

        self.passagelist=[]

        self.welcome()

        self.mainloop()


app = App()
