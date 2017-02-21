#
#  Extra_Windows.py
#
#  Copyright2014 Mosaic Team Alex <zfmedisonxfmt@126.com>
#
#  This program is the additional part of the GUI
from tkinter import*
from tkinter.ttk import*
from tkinter.messagebox import*
from GUIplus.tkFileDialog import*
from GUIplus.tkMessageBox import*
from GUIplus.Cut_Copy_Paste import*
import WORD_SEG
import Sentence_Segmentation

#
#  name: processfile
#  @param       None
#  @return      None
#
#  The next function is used to read a file ,split the text into words
#  and save the outcome as a new file
def processfile():
    o=askopenfilename()
    s=asksaveasfilename()
    if o!='' and s!='':
        f=open(o,'r')
        a=f.readlines()
        f.close()

        g=open(s,'w')
        d=''
        for b in a:
            d+=b
        e=Sentence_Segmentation.sentence_segment(d)
        for i in range(len(e)):
            c=WORD_SEG.word_seg(e[i])
            g.write(c+'\n')
        g.close()

#
#  name: processfile
#  @param       None
#  @return      c       <class 'str'>
#
#  The next two functions are used to read a file or save a file
def loadfile():
    o=askopenfilename()
    if o!='':
        f=open(o,'r')
        a=f.readlines()
        f.close()
        c=''
        for b in a:
            c += b
        return c
    
#
#  name: processfile
#  @param       None
#  @return      s       <class 'str'>
def savefile():
    s=asksaveasfilename()
    if s!='':
        return s

#
#  name: add_dict_Window
#
#  The window used to add new words to the dictionary

class add_dict_Window(Toplevel):

#
#  name: add_dict_Window.fade_in
#  @param       None
#  @return      None
#
#  The next function is used to have the Toplevel fade in
    def fade_in(self):
        if self.alpha_ < 1:
            self.alpha_ += 0.1
            self.attributes('-alpha',self.alpha_)
            self.after(25,self.fade_in)

#
#  name: add_dict_Window.fade_in_toplevel
#  @param       None
#  @param       None
#
#  The next function is used to have the Toplevel of the Toplevel fade in
    def fade_in_toplevel(self):
        if self.toplevel.alpha_ < 1:
            self.toplevel.alpha_ += 0.1
            self.toplevel.attributes('-alpha',self.toplevel.alpha_)
            self.toplevel.after(25,self.fade_in_toplevel)

#
#  name: add_dict_Window.is_Chinese
#  @param       word        <class 'str'>
#  @return                  <class 'bool'>
#
#  The next function is used to judge whether the input is Chinese or not
    def is_chinese(self,word):
        for ch in word:
            if not '\u4e00'<=ch<='\u9fa5':
                return False
        return True

#
#  name: add_dict_Window._add_word
#  @param       None
#  @return      None
#
#  The next function is called when the button '添加' in the toplevel
#  is pressed, and it add the word to the dictionary
    def add_word(self):
        word_add = self.text_1.get('1.0','end').strip()
        if word_add=='':
            self.is_empty()
            return
        if self.is_chinese(word_add):
            but_cho=self.button_choose.get()
            if but_cho == 0:
                WORD_SEG.dictionary.A[word_add]=(500000,'1')
                self.destroy()
            elif but_cho == 1:
                WORD_SEG.dictionary.A[word_add]=(50000,'1')
                self.destroy()
            elif but_cho == -1:
                self.no_choice()
        else:
            self.not_chinese()

#
#  name: add_dict_Window.no_choice
#  @param       None
#  @return      None
#
#  The next function create a Toplevel used to show no Radiobutton is chosen
    def no_choice(self):
        self.toplevel = Toplevel(background='White')
        self.toplevel.title('错误')
        self.toplevel.iconbitmap('logo.ico')
        self.toplevel.geometry('250x200')

        self.toplevel.alpha_ = 0
        self.toplevel.attributes('-alpha',0)
        self.toplevel.after(1,self.fade_in_toplevel)

        self.toplevel.resizable(width=False,height=False)
        label_1 = Label(self.toplevel,image=self.logo)
        label_1.place(relx=0.08,rely=0.1)
        label_2 = Label(self.toplevel,background='White',text="""
    错误！

    请选择词语类型！
    """)
        label_2.place(relx=0.25,rely=0.1)
        button = Button(self.toplevel,text='关闭',command=self.toplevel.destroy)
        button.place(relx=0.6,rely=0.75)
        self.toplevel.mainloop()

#
#  name: add_dict_Window.not_chinese
#  @param       None
#  @return      None
#
#  The next function create a Toplevel used to show the input is not Chinese
    def not_chinese(self):
        self.toplevel = Toplevel(background='White')
        self.toplevel.title('错误')
        self.toplevel.iconbitmap('logo.ico')
        self.toplevel.geometry('250x200')

        self.toplevel.alpha_ = 0
        self.toplevel.attributes('-alpha',0)
        self.toplevel.after(1,self.fade_in_toplevel)
        
        self.toplevel.resizable(width=False,height=False)
        label_1 = Label(self.toplevel,image=self.logo)
        label_1.place(relx=0.08,rely=0.1)
        label_2 = Label(self.toplevel,background='White',text="""
    错误！

    请输入中文词语！
    """)
        label_2.place(relx=0.25,rely=0.1)
        button = Button(self.toplevel,text='关闭',command=self.toplevel.destroy)
        button.place(relx=0.6,rely=0.75)
        self.toplevel.mainloop()

#
#  name: add_dict_Window.is_empty
#  @param       None
#  @return      None
#
#  The next function create a Toplevel used to show nothing is entered
    def is_empty(self):
        self.toplevel = Toplevel(background='White')
        self.toplevel.title('错误')
        self.toplevel.iconbitmap('logo.ico')
        self.toplevel.geometry('250x200')

        self.toplevel.alpha_ = 0
        self.toplevel.attributes('-alpha',0)
        self.toplevel.after(1,self.fade_in_toplevel)

        self.toplevel.resizable(width=False,height=False)
        label_1 = Label(self.toplevel,image=self.logo)
        label_1.place(relx=0.08,rely=0.1)
        label_2 = Label(self.toplevel,background='White',text="""
    错误！

    输入不能为空！
    """)
        label_2.place(relx=0.25,rely=0.1)
        button = Button(self.toplevel,text='关闭',command=self.toplevel.destroy)
        button.place(relx=0.6,rely=0.75)
        self.toplevel.mainloop()
    
#
#  name: add_dict_Window.__init__
#  @param       None
#  @return      None
#
#  Initialize the toplevel and add several objects to it
#  The window will never terminate until the window is closed!
    def __init__(self):
        Toplevel.__init__(self,background='White',takefocus=True)

        self.alpha_ = 0
        self.attributes('-alpha',0)
        self.after(1,self.fade_in)

        self.title('添加新词')
        self.geometry('450x220')
        self.resizable(width=False,height=False)
        self.option_add('Font','微软雅黑')
        self.iconbitmap('logo.ico')

        self.bg = PhotoImage(file='bg_00.png')
        self.img = Canvas(self,width=450,height=300)
        self.img.create_image(225,150,image=self.bg)
        self.img.place(x=0,y=0,relwidth=1,relheight=1)

        self.lift()
        
        self.logo=PhotoImage(file='logo_1.png')
        self.label_1 = Label(self,image=self.logo)
        self.label_1.place(relx=0.05,rely=0.1)

        self.label_2=Label(self,text='请输入想添加的词语',background='white',foreground='grey')
        self.label_2.place(relx=0.18,rely=0.16,relwidth=0.72)
        self.label_3=Label(self,text='请选择词语类型',background='white',foreground='grey')
        self.label_3.place(relx=0.18,rely=0.56,relwidth=0.72)

        self.text_1=TextPlus(self,relief=FLAT,height=5)
        self.text_1.place(relx=0.18,rely=0.25,relwidth=0.72)

        self.button_choose=IntVar()
        self.button_choose.set(-1)

        style = Style()
        style.configure('BW.TRadiobutton',background='#FFFFFF')
        self.c1=Radiobutton(self,style='BW.TRadiobutton',variable=self.button_choose,value=0,text='人名')
        self.c2=Radiobutton(self,style='BW.TRadiobutton',variable=self.button_choose,value=1,text='常用词')
        self.c1.place(relx=0.18,rely=0.65,relwidth=0.36)
        self.c2.place(relx=0.54,rely=0.65,relwidth=0.36)

        self.button_1=Button(self,text='添加',command=self.add_word)
        self.button_1.place(relx=0.25,rely=0.8)
        self.button_2=Button(self,text='返回',command=self.destroy)
        self.button_2.place(relx=0.65,rely=0.8)

        self.mainloop()


#
#  name: del_dict_Window
#
#  The window used to delete a word from the dictionary

class del_dict_Window(Toplevel):

#
#  name: del_dict_Window.fade_in
#  @param       None
#  @return      None
#
#  The next function is used to have the Toplevel fade in
    def fade_in(self):
        if self.alpha_ < 1:
            self.alpha_ += 0.1
            self.attributes('-alpha',self.alpha_)
            self.after(25,self.fade_in)

#
#  name: del_dict_Window.fade_in_toplevel
#  @param       None
#  @param       None
#
#  The next function is used to have the Toplevel of the Toplevel fade in
    def fade_in_toplevel(self):
        if self.toplevel.alpha_ < 1:
            self.toplevel.alpha_ += 0.1
            self.toplevel.attributes('-alpha',self.toplevel.alpha_)
            self.toplevel.after(25,self.fade_in_toplevel)

#
#  name: del_dict_Window.no_choice
#  @param       None
#  @return      None
#
#  The next function create a Toplevel used to show the input
#  is not in the dictionary
    def not_in_dictionary(self):
        self.toplevel = Toplevel(background='White')
        self.toplevel.title('错误')
        self.toplevel.iconbitmap('logo.ico')
        self.toplevel.geometry('250x200')

        self.toplevel.alpha_ = 0
        self.toplevel.attributes('-alpha',0)
        self.toplevel.after(1,self.fade_in_toplevel)

        self.toplevel.resizable(width=False,height=False)
        label_1 = Label(self.toplevel,image=self.logo)
        label_1.place(relx=0.08,rely=0.1)
        label_2 = Label(self.toplevel,background='White',text="""
    错误！

    您输入的内容不在词典中！
    """)
        label_2.place(relx=0.25,rely=0.1)
        button = Button(self.toplevel,text='关闭',command=self.toplevel.destroy)
        button.place(relx=0.6,rely=0.75)
        self.toplevel.mainloop()

#
#  name: del_dict_Window.delete_word
#  @param       None
#  @return      None
#
#  The next function is called when the button '删除' in the toplevel
#  is pressed, and it delete the word from the dictionary
    def delete_word(self):
        word_delete=self.text_1.get('1.0','end').strip()
        if word_delete=='':
            self.is_empty()
            return
        if word_delete not in WORD_SEG.dictionary.A.keys():
            self.not_in_dictionary()
        else:
            del WORD_SEG.dictionary.A[word_delete]
            self.destroy()

#
#  name: del_dict_Window.is_empty
#  @param       None
#  @return      None
#
#  The next function create a Toplevel used to show nothing is entered
    def is_empty(self):
        self.toplevel = Toplevel(background='White')
        self.toplevel.title('错误')
        self.toplevel.iconbitmap('logo.ico')
        self.toplevel.geometry('250x200')

        self.toplevel.alpha_ = 0
        self.toplevel.attributes('-alpha',0)
        self.toplevel.after(1,self.fade_in_toplevel)

        self.toplevel.resizable(width=False,height=False)
        label_1 = Label(self.toplevel,image=self.logo)
        label_1.place(relx=0.08,rely=0.1)
        label_2 = Label(self.toplevel,background='White',text="""
    错误！

    输入不能为空！
    """)
        label_2.place(relx=0.25,rely=0.1)
        button = Button(self.toplevel,text='关闭',command=self.toplevel.destroy)
        button.place(relx=0.6,rely=0.75)
        self.toplevel.mainloop()

#
#  name: del_dict_Window.__init__
#  @param       None
#  @return      None
#
#  Initialize the toplevel and add several objects to it
#  The window will never terminate until the window is closed!
    def __init__(self):
        Toplevel.__init__(self,background='White',takefocus=True)

        self.alpha_ = 0
        self.attributes('-alpha',0)
        self.after(1,self.fade_in)

        self.title('删除原词')
        self.geometry('450x180')
        self.resizable(width=False,height=False)
        self.option_add('Font','微软雅黑')
        self.iconbitmap('logo.ico')

        self.bg = PhotoImage(file='bg_00.png')
        self.img = Canvas(self,width=450,height=300)
        self.img.create_image(225,150,image=self.bg)
        self.img.place(x=0,y=0,relwidth=1,relheight=1)

        self.lift()
        
        self.logo=PhotoImage(file='logo_1.png')
        self.label_1 = Label(self,image=self.logo)
        self.label_1.place(relx=0.05,rely=0.1)

        self.label_2=Label(self,text='请输入想删除的词语',background='white',foreground='grey')
        self.label_2.place(relx=0.18,rely=0.2,relwidth=0.72)

        self.text_1=TextPlus(self,relief=FLAT,height=5)
        self.text_1.place(relx=0.18,rely=0.31,relwidth=0.72)

        self.button_1=Button(self,text='删除',command=self.delete_word)
        self.button_1.place(relx=0.23,rely=0.75)
        self.button_2=Button(self,text='返回',command=self.destroy)
        self.button_2.place(relx=0.68,rely=0.75)

        self.mainloop()


#
#  name: ss_Window
#
#  The window used to split a sentence into several words

class ss_Window(Toplevel):

#
#  name: ss_Window.show_help
#  @param       event       <class 'tkinter.Event'>
#  @return      None
#
# The next function is used to show help of the Toplevel
    def show_help(self,event=None):
        self.toplevel = Toplevel(background='White')
        self.toplevel.title('帮助·逐句分词')
        self.toplevel.iconbitmap('logo.ico')
        self.toplevel.geometry('360x320')

        self.toplevel.alpha_ = 0
        self.toplevel.attributes('-alpha',0)
        self.toplevel.after(1,self.fade_in_toplevel)
        
        self.toplevel.resizable(width=False,height=False)
        label_1 = Label(self.toplevel,image=self.logo)
        label_1.place(relx=0.08,rely=0.07)
        label_2 = Label(self.toplevel,background='White',text="""
    中文分词器·逐句分词


    "分词"    点击想进行分词的语句,然后点击
               该按钮,结果将在"结果"文本框中显示;
    
    "存储"    存储"结果"文本框中内容，选择
               存储路径并命名文件;
               (注意:请将文件格式命名为.txt)
    
    "返回"    点击以返回主界面
    
    """)
        label_2.place(relx=0.2,rely=0.075)
        button = Button(self.toplevel,text='关闭',command=self.toplevel.destroy)
        button.place(relx=0.7,rely=0.85)
        self.toplevel.mainloop()

#
#  name: ss_Window.change_bg
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
#  name: ss_Window.fade_in
#  @param       None
#  @return      None
    def fade_in(self):
        if self.alpha_ < 1:
            self.alpha_ += 0.1
            self.attributes('-alpha',self.alpha_)
            self.after(25,self.fade_in)

#
#  name: ss_Window.fade_in_toplevel
#  @param       None
#  @return      None
    def fade_in_toplevel(self):
        if self.toplevel.alpha_ < 1:
            self.toplevel.alpha_ += 0.1
            self.toplevel.attributes('-alpha',self.toplevel.alpha_)
            self.toplevel.after(25,self.fade_in_toplevel)

#
#  name: ss_Window.button_word_split_1
#  @param       None
#  @return      None
#
#  The next function is called when the button '分词' in the Toplevel is pressed,
#  and it calls the function named 'sentence_segment' defined in the file
#  'Sentence_Segmentation' to split the sentence into several words
    def button_word_split_1(self):
        if self.listbox.curselection()==():
            pass
        else:
            self.get_index=self.listbox.curselection()[0]
            self.word_split_outcome=WORD_SEG.word_seg(self.ss_outcome[self.get_index])
            self.text.insert(0.0,self.word_split_outcome+'\n')

#
#  name: ss_Window.button_save_file
#  @param       None
#  @return      None
#
#  The next function is called when the button '存储' in the Toplevel is pressed,
#  and it saves the outcome as a new file
    def button_save_file(self):
        save_file=self.text.get('1.0','end')
        s=savefile()
        if s == None:
            pass
        else:
            g=open(s,'w')
            g.write(save_file)
            g.close()

#
#  name: ss_Window.__init__
#  @param       None
#  @return      None
#
#  Initialize the main window and add several objects to it
#  The window will never terminate until the window is closed!           
    def __init__(self,ss_outcome):
        self.ss_outcome = ss_outcome
        
        Toplevel.__init__(self,takefocus=True)

        self.alpha_ = 0
        self.attributes('-alpha',0)
        self.after(1,self.fade_in)

        self.title('逐句分词')
        self.geometry('660x580')
        self.resizable(width=False,height=False)
        self.option_add('Font','微软雅黑')
        self.iconbitmap('logo.ico')

        self.bg = PhotoImage(file='bg_1.png')
        self.img = Canvas(self,height=660,width=580)
        self.img.create_image(330,290,image=self.bg)
        self.img.place(x=0,y=0,relwidth=1,relheight=1)
        self.bg_num =1

        self.logo=PhotoImage(file='logo_1.png')
        self.button_logo = Button(self,image=self.logo)
        self.button_logo.bind('<Button-1>',self.change_bg)
        self.button_logo.bind('<Button-3>',self.show_help)
        self.button_logo.grid(row=0,column=0)

        self.lift()

#  create labels in the Toplevel
        self.label_1 = Label(self,text='原文',background='white',foreground='grey')
        self.label_1.grid(row=1,column=1,columnspan=3,ipadx=268,ipady=4,sticky=W)
        self.label_2 = Label(self,text='结果',background='white',foreground='grey')
        self.label_2.grid(row=4,column=1,columnspan=3,ipadx=268,ipady=4,sticky=W)

        self.listbox=Listbox(self,selectmode=SINGLE,relief=FLAT,width=80,height=12)
        self.listbox.insert(0,*ss_outcome)
        self.listbox.grid(row=2,column=1,columnspan=3)

        self.text=TextPlus(self,relief=FLAT,width=80,height=15)
        self.text.grid(row=5,column=1,columnspan=3)
        
#  create buttons in the Toplevel
        self.button_1=Button(self,text='分词',command=self.button_word_split_1)
        self.button_1.grid(row=3,column=1,pady=4)
        self.button_2=Button(self,text='存储',command=self.button_save_file)
        self.button_2.grid(row=3,column=2)
        self.button_3=Button(self,text='返回',command=self.destroy)
        self.button_3.grid(row=3,column=3)
        

        self.mainloop()
