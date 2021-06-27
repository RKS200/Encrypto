from cryptography.fernet import Fernet as cg
import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.filedialog as fd
import os.path as path

FORMAT = 'utf-8'
filetype = ''
filepath = ''

def msgcopy():
    global mainwin
    global msgen_ent
    mainwin.clipboard_clear()
    mainwin.clipboard_append(msgen_ent.get())
    mainwin.update()
    
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
    
def fileselect():
    global file_ent
    global filetype
    global filepath
    filename = fd.askopenfilename(
        title='Open a file to Encrypt')
    file_ent.delete(0, tk.END)
    file_ent.insert(0 , filename)
    filepath, filetype = path.splitext(filename)    
    
def fileencrypt():
    global filetype
    global filepath
    global file_ent
    if file_ent.get() == '':
        msgbox.showerror('Encrypto','Select a file please')
    else:
        try:
            file = open(file_ent.get() , 'rb')
        except:
            msgbox.showerror('Encrypto','Invalid file')
        #filename = fd.asksaveasfile(title = 'Save as', filetypes = [('Encrypted file' , '*.encrypto')], defaultextension = [('Encrypted file' , '*.encrypto')])
        filename = filepath + filetype + '.encrypto'
        enfile = open(filename , 'wb')
        genkey = cg.generate_key()
        encry = cg(genkey)
        enfile.write(genkey)
        prefile = file.read()
        enfile.write(encry.encrypt(prefile))
        enfile.close()
        file.close()
        msgbox.showinfo('Encrypto' , 'Encrypted Successfully: ' + filename)
    
mainwin = tk.Tk()
mainwin.title('Encrypto')
ico = tk.PhotoImage(file = 'iconen.png')
mainwin.iconphoto(False,ico)

enmsgframe = tk.LabelFrame(mainwin, height = 200, width = 400, text = 'Encrypt Message')
msg_ent = tk.Entry(enmsgframe, width = 40)
msg_ent.grid(row = 0, column = 0, padx = 10 , pady = 10)
msgen_btn = tk.Button(enmsgframe, text = '↓Encrypt↓', command = msgencrypt)
msgen_btn.grid(row = 1, column = 0, padx = 10 , pady = 10)
msgen_ent = tk.Entry(enmsgframe, width = 40)
msgen_ent.grid(row = 2, column = 0, padx = 10 , pady = 10)
msgcopy_btn = tk.Button(enmsgframe, text = 'Copy', command = msgcopy)
msgcopy_btn.grid(row = 2, column = 1, padx = 10 , pady = 10)
enmsgframe.grid(row = 0 , column = 0)

#enfileframe = tk.LabelFrame(mainwin, height = 200, width = 400, text = 'Encrypt File')
#file_ent = tk.Entry(enfileframe, width = 40)
#file_ent.grid(row = 0, column = 0, padx = 10 , pady = 10)
#sel_btn = tk.Button(enfileframe, text = 'Select', command = fileselect)
#sel_btn.grid(row = 0, column = 1, padx = 10 , pady = 10)
#fileen_btn = tk.Button(enfileframe, text = 'Encrypt', command = fileencrypt)
#fileen_btn.grid(row = 1, column = 0, padx = 10 , pady = 10)
#enfileframe.grid(row = 1 , column = 0)

mainwin.resizable(False,False)
mainwin.mainloop()
