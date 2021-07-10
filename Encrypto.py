from cryptography.fernet import Fernet as cg
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import tkinter.filedialog as fd
import os.path as path
import os
from zipfile import ZipFile
import webbrowser as web

FORMAT = 'utf-8'

enmsgframe = None
demsgframe = None
czipframe = None
ezipframe = None

msg_ent = None
msgen_ent = None
msgde_ent = None

file_lbl = None

mainwin = None
menubar = None

def emptywin():
    global mainwin
    global menubar
    mainwin = tk.Tk()
    mainwin.title('Encrypto - Welcome')
    ico = tk.PhotoImage(file = 'iconen.png')
    mainwin.iconphoto(False,ico)
    style = ttk.Style(mainwin)
    style.theme_use('vista')

    menubar = tk.Menu(mainwin)

    file = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    #file.add_command(label ='Compress Files', command = czipwin)
    #file.add_command(label ='Extract a Zip file', command = None)
    #file.add_separator()
    file.add_command(label ='Exit', command = mainwin.destroy)

    tools = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Tools', menu = tools)
    tools.add_command(label = 'Encrypt Message', command = enmsgwin)
    tools.add_command(label = 'Decrypt Message', command = demsgwin)

    helpm = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = helpm)
    helpm.add_command(label = 'Github page', command = lambda:web.open('https://github.com/RKS200/Encrypto'))
    helpm.add_command(label = 'About', command = lambda:msgbox.showinfo('Encrypto - About' , '''Encrypto v2021.1
Encrypto is a Message Encryption tool to encrypt and decrypt message that you want to be safe.
Encrypto is a open source project.'''))
    
    mainwin.resizable(False,False)
    mainwin.config(menu = menubar)

def msgcopy(ent):
    global mainwin
    mainwin.clipboard_clear()
    mainwin.clipboard_append(ent.get())
    mainwin.update()
    
def msgpaste():
    global mainwin
    global msg_ent
    msg_ent.delete(0, tk.END)
    msg_ent.insert(0,mainwin.clipboard_get())
    
def msgencrypt():
    global msg_ent
    global msgen_ent
    msgen_ent.delete(0, tk.END)
    genkey = cg.generate_key()
    encry = cg(genkey)
    if msg_ent.get() == '':
        msgbox.showwarning('Encrypto' , 'Nothing Entered')
    bimsg = msg_ent.get().encode(FORMAT)
    enmsg = encry.encrypt(bimsg)
    msgen_ent.insert(0,(genkey + enmsg))

def msgdecrypt():
    demsg = ''
    global msg_ent
    global msgde_ent
    msgde_ent.delete(0 , tk.END)
    msg = msg_ent.get()
    key = msg[0:44]
    msg_ent.delete(0 , 44)
    enmsg = msg_ent.get().encode(FORMAT)
    try:
        decry  = cg(key)
    except:
        msgbox.showerror('Encrypto' , 'Invalid Key')
    try:
        demsg = decry.decrypt(enmsg)
    except:
        msgbox.showerror('Encrypto' , 'Decryption Error (May be invalid key)')
    msg_ent.delete(0 , tk.END)
    msgde_ent.insert(0 , demsg)
    
def fileselect():
    global file_lbl
    filename = fd.askopenfilename(
        title='Open a file to Encrypt')
    file_lbl.config(text = filename)
    
def createzip(clevel,password):
    global file_lbl
    if file_lbl.cget('text') == 'No file Selected':
        msgbox.showwarning('Warning','Please select a file')
    elif password == '':
        msgbox.showwarning('Warning','Please enter a password')
    else:
        with ZipFile(fd.asksaveasfile(filetype = [('Zip Files','*.zip')]) , 'w') as zipfile:
            with open(file_lbl.cget('text') , 'r') as file:
                zipfile.write('Hi')

def enmsgwin():
    global mainwin
    global msg_ent
    global msgen_ent
    mainwin.destroy()
    emptywin()
    mainwin.title('Encrypto - Message Encryption')
    enmsgframe = ttk.LabelFrame(mainwin, height = 200, width = 400, text = 'Encrypt Message')
    msg_ent = ttk.Entry(enmsgframe, width = 40)
    msg_ent.grid(row = 0, column = 0, padx = 10 , pady = 10)
    msgen_btn = ttk.Button(enmsgframe, text = '↓Encrypt↓', command = msgencrypt)
    msgen_btn.grid(row = 1, column = 0, padx = 10 , pady = 10)
    msgen_ent = ttk.Entry(enmsgframe, width = 40)
    msgen_ent.grid(row = 2, column = 0, padx = 10 , pady = 10)
    msgcopy_btn = ttk.Button(enmsgframe, text = 'Copy', command = lambda: msgcopy(msgen_ent))
    msgcopy_btn.grid(row = 2, column = 1, padx = 10 , pady = 10)
    msgpaste_btn = ttk.Button(enmsgframe, text = 'Paste', command = msgpaste)
    msgpaste_btn.grid(row = 0, column = 1, padx = 10 , pady = 10)
    enmsgframe.pack(padx = 5 , pady = 5)
    
def demsgwin():
    global mainwin
    global msg_ent
    global msgde_ent
    mainwin.destroy()
    emptywin()
    mainwin.title('Encrypto - Message Decryption')
    demsgframe = ttk.LabelFrame(mainwin, height = 200, width = 400, text = 'Decrypt Message')
    msg_ent = ttk.Entry(demsgframe, width = 40)
    msg_ent.grid(row = 0, column = 0, padx = 10 , pady = 10)
    msgde_btn = ttk.Button(demsgframe, text = '↓Decrypt↓', command = msgdecrypt)
    msgde_btn.grid(row = 1, column = 0, padx = 10 , pady = 10)
    msgde_ent = ttk.Entry(demsgframe, width = 40)
    msgde_ent.grid(row = 2, column = 0, padx = 10 , pady = 10)
    msgcopy_btn = ttk.Button(demsgframe, text = 'Copy', command = lambda: msgcopy(msgde_ent))
    msgcopy_btn.grid(row = 2, column = 1, padx = 10 , pady = 10)
    msgpaste_btn = ttk.Button(demsgframe, text = 'Paste', command = msgpaste)
    msgpaste_btn.grid(row = 0, column = 1, padx = 10 , pady = 10)
    demsgframe.pack(padx = 5 , pady = 5)
    
def czipwin():
    global mainwin
    global msg_ent
    global msgde_ent
    global file_lbl
    clevel = 12
    mainwin.destroy()
    emptywin()

    mainwin.title('pyZip - File Compression')
    czipframe = ttk.LabelFrame(mainwin, height = 200, width = 400, text = 'Compress file')
    file_lbl = ttk.Label(czipframe,text = 'No file Selected', width = 40)
    file_lbl.grid(row = 0, column = 0, padx = 10 , pady = 10)
    fileselect_btn = ttk.Button(czipframe, text = 'Select file', command = fileselect)
    fileselect_btn.grid(row = 0, column = 1, padx = 10 , pady = 10)
    clevel_lbl = ttk.Label(czipframe,text = 'Compression Level:', width = 40)
    clevel_lbl.grid(row = 2, column = 0, padx = 10 , pady = 10)
    low_rb = tk.Radiobutton(czipframe,text = 'Low (Fast)', variable = clevel, value = 14, command = lambda:high_rb.deselect())
    low_rb.grid(row = 3, column = 0, padx = 10 , pady = 10)
    high_rb = tk.Radiobutton(czipframe,text = 'High (Recommended)', variable = clevel, value = 12, command = lambda:low_rb.deselect())
    high_rb.grid(row = 3, column = 1, padx = 10 , pady = 10)
    high_rb.select()
    low_rb.deselect()
    password_lbl = ttk.Label(czipframe,text = 'Password:', width = 40)
    password_lbl.grid(row = 4, column = 0, padx = 10 , pady = 10)
    password_ent = ttk.Entry(czipframe, width = 40)
    password_ent.grid(row = 4, column = 1, padx = 10 , pady = 10)
    create_btn = ttk.Button(czipframe, text = 'Create', command = lambda:createzip(clevel,password_ent.get()))
    create_btn.grid(row = 5, column = 1, padx = 10 , pady = 10)
    czipframe.pack(padx = 5 , pady = 5)

emptywin()
welcome_frame = ttk.LabelFrame(mainwin, text = 'Welcome to Encrypto')
#czip_btn = ttk.Button(welcome_frame, text = 'Compress Files',width = 20, command = czipwin)
#czip_btn.grid(row = 1, column = 1, padx = 10 , pady = 10)
#ezip_btn = ttk.Button(welcome_frame, text = 'Extract a Zip file',width = 20, command = None)
#ezip_btn.grid(row = 1, column = 2, padx = 10 , pady = 10)
emsg_btn = ttk.Button(welcome_frame, text = 'Encrypt Message',width = 20, command = enmsgwin)
emsg_btn.grid(row = 2, column = 1, padx = 10 , pady = 10)
dmsg_btn = ttk.Button(welcome_frame, text = 'Decrypt Message',width = 20, command = demsgwin)
dmsg_btn.grid(row = 2, column = 2, padx = 10 , pady = 10)
welcome_frame.pack(padx = 5 , pady = 5)

mainwin.mainloop()