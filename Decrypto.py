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
    global msgde_ent
    mainwin.clipboard_clear()
    mainwin.clipboard_append(msgde_ent.get())
    mainwin.update()
    
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
        msgbox.showerror('Decrypto' , 'Invalid Key')
    try:
        demsg = decry.decrypt(enmsg)
    except:
        msgbox.showerror('Decrypto' , 'Decryption Error (May be invalid key)')
    msg_ent.delete(0 , tk.END)
    msgde_ent.insert(0 , demsg)
    
def fileselect():
    global file_ent
    global filetype
    global filepath
    filename = fd.askopenfilename(title='Select the encrypted file', filetypes = [('Encrypted file' , '*.encrypto')], defaultextension = [('Encrypted file' , '*.encrypto')])
    file_ent.delete(0, tk.END)
    file_ent.insert(0 , filename)
    filepath, filetype = path.splitext(filename)

def filedecrypt():
    global file_ent
    global filepath
    if file_ent.get() == '':
        msgbox.showerror('Decrypto','Select a file please')
    else:
        try:
            file = open(file_ent.get() , 'rb')
        except:
            msgbox.showerror('Decrypto','Invalid file')
        prefile = file.read()
        key = prefile[0:44]
        decry  = cg(key)
        print(key)
        prefile = prefile.decode(FORMAT)
        prefile.replace(key.decode(FORMAT) , '')
        prefile = prefile.encode(FORMAT)
        with open(filepath , 'wb') as defile:
            defile.write(decry.decrypt(key))
        file.close
        msgbox.showinfo('Decrypto' , 'Decrypted Successfully: ' + filepath)

mainwin = tk.Tk()
mainwin.title('Decrypto')
ico = tk.PhotoImage(file = 'iconde.png')
mainwin.iconphoto(False,ico)

demsgframe = tk.LabelFrame(mainwin, height = 200, width = 400, text = 'Decrypt Message')
msg_ent = tk.Entry(demsgframe, width = 40)
msg_ent.grid(row = 0, column = 0, padx = 10 , pady = 10)
msgde_btn = tk.Button(demsgframe, text = '↓Decrypt↓', command = msgdecrypt)
msgde_btn.grid(row = 1, column = 0, padx = 10 , pady = 10)
msgde_ent = tk.Entry(demsgframe, width = 40)
msgde_ent.grid(row = 2, column = 0, padx = 10 , pady = 10)
msgcopy_btn = tk.Button(demsgframe, text = 'Copy', command = msgcopy)
msgcopy_btn.grid(row = 2, column = 1, padx = 10 , pady = 10)
demsgframe.grid(row = 0 , column = 0)

#defileframe = tk.LabelFrame(mainwin, height = 200, width = 400, text = 'Decrypt File')
#file_ent = tk.Entry(defileframe, width = 40)
#file_ent.grid(row = 0, column = 0, padx = 10 , pady = 10)
#sel_btn = tk.Button(defileframe, text = 'Select', command = fileselect)
#sel_btn.grid(row = 0, column = 1, padx = 10 , pady = 10)
#filede_btn = tk.Button(defileframe, text = 'Decrypt', command = filedecrypt)
#filede_btn.grid(row = 1, column = 0, padx = 10 , pady = 10)
#defileframe.grid(row = 1 , column = 0)

mainwin.resizable(False,False)
mainwin.mainloop()
