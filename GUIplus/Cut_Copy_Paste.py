import tkinter as tk
import tkinter.ttk as ttk

class EntryPlus(ttk.Entry):
    def __init__(self, *args, **kwargs):
        ttk.Entry.__init__(self, *args, **kwargs)
        _rc_menu_install(self)
        # overwrite default class binding so we don't need to return "break"
        #self.bind_class("Entry", "<Control-a>", self.event_select_all)  
        self.bind("<Button-3><ButtonRelease-3>", self.show_menu)

    def event_select_all(self, *args):
        self.focus_force()
        self.selection_range(0, tk.END)

    def event_delete(self, *args):
        self.focus_force
        try:
            self.delete(tk.SEL_FIRST,tk.SEL_LAST)
        except:
            pass

    def event_delete_all(self, *args):
        self.focus_force()
        self.delete(0,"end")

    def show_menu(self, e):
        self.tk.call("tk_popup", self.menu, e.x_root, e.y_root)

class TextPlus(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        _rc_menu_install(self)
        # overwrite default class binding so we don't need to return "break"
        #self.bind_class("Text", "<Control-a>", self.event_select_all)  
        self.bind("<Button-3><ButtonRelease-3>", self.show_menu)
    
    def event_select_all(self, *args):
        self.focus_force()        
        self.tag_add("sel","1.0","end")

    def event_delete(self, *args):
        self.focus_force()
        try:
            self.delete(tk.SEL_FIRST,tk.SEL_LAST)
        except:
            pass
            

    def event_delete_all(self, *args):
        self.focus_force()
        self.delete('1.0','end')

    def show_menu(self, e):
        self.tk.call("tk_popup", self.menu, e.x_root, e.y_root)


def _rc_menu_install(w):
    w.menu = tk.Menu(w, tearoff=0)
    w.menu.add_command(label="剪切")
    w.menu.add_command(label="复制")
    w.menu.add_command(label="粘贴")
    w.menu.add_command(label="删除")
    w.menu.add_separator()
    w.menu.add_command(label="全选")
    w.menu.add_separator()
    w.menu.add_command(label="清空")
            

    w.menu.entryconfigure("剪切", command=lambda: w.focus_force() or w.event_generate("<<Cut>>"))
    w.menu.entryconfigure("复制", command=lambda: w.focus_force() or w.event_generate("<<Copy>>"))
    w.menu.entryconfigure("粘贴", command=lambda: w.focus_force() or w.event_generate("<<Paste>>"))
    w.menu.entryconfigure("删除", command=w.event_delete)
    w.menu.entryconfigure("全选", command=w.event_select_all)
    w.menu.entryconfigure("清空", command=w.event_delete_all)


if __name__ == "__main__":

    class SampleApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            self.entry = EntryPlus(self)
            self.text = TextPlus(self)

            self.entry.pack()
            self.text.pack()

            self.entry.insert(0, "copy paste")
            self.text.insert(tk.INSERT, "copy paste")

    app = SampleApp()
    app.mainloop()
