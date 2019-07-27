import sys
import pyperclip
from PIL import ImageTk, Image
from tkinter import filedialog

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import gui_support

def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    root.mainloop() 
w = None
def create_Toplevel1(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe Print} -size 13 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("854x525+438+181")
        top.title("HANDWRITTEN TO DIGITAL TEXT")
        top.configure(relief="ridge")
        top.configure(background="#d8133b")
        top.configure(highlightbackground="#dfd7ef")
        top.configure(highlightcolor="#3c2363")
        def BROWSE():
            #global file_path
            file_path = filedialog.askopenfilename()
            #print(file_path)
            pyperclip.copy(file_path)
            #print(pyperclip.paste())
            img=Image.open(file_path)
            img=img.resize((694, 371), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            panel = tk.Label(top, image = img)
            panel.place(relx=0.012, rely=0.133, height=371, width=694)
            textbox = tk.Label(top)
            textbox.place(relx=0.194, rely=0.933, relheight=0.046, relwidth=0.578)
            textbox.configure(text= pyperclip.paste())
            textbox.mainloop()
            panel.mainloop()
            return(file_path)
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.141, rely=0.019, height=41, width=500)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''HANDWRITTEN TO DIGITAL TEXT''')
        self.Label1.configure(width=384)
        
        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.843, rely=0.267, height=45, width=116)
        self.TButton1.configure(command=gui_support.START)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''CONVERT TO TEXT''')
        self.TButton1.configure(width=116)
        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.843, rely=0.367, height=45, width=116)
        self.TButton2.configure(command=gui_support.Exit)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''EXIT''')
        self.TButton2.configure(width=116)
        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.843, rely=0.467, height=45, width=116)
        self.TButton3.configure(command=gui_support.ShowFile)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''SHOW FILE''')
        self.TButton3.configure(width=116)
        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.012, rely=0.133, height=371, width=694)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Import Picture Here''')
        self.Label6.configure(width=694)
        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.012, rely=0.933, height=21, width=82)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''SELECT IMAGE''')
        self.Text1 = tk.Label(top)
        self.Text1.place(relx=0.194, rely=0.933, relheight=0.046, relwidth=0.578)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(width=494)
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.791, rely=0.933, height=24, width=20)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=BROWSE)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''...''')
        """print("hello")
        x=self.Text1.cget("text")
        print(x)
        print("hey")"""
"""def pass_path(self):
    global path
    path=self.Text1.get()
    print(path)"""    
if __name__ == '__main__':
    vp_start_gui()
