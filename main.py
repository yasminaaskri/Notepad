from tkinter import *
from tkinter import filedialog


#colors 
color1="lightblue"

root = Tk()
root.title("Notepad")
root.geometry("600x600")
root.configure(bg=color1)
root.resizable(FALSE,FALSE)

def save_file():
   saved_file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
   if saved_file is None:
      return
   text=str(entry.get(1.0,END))
   saved_file.write(text)
   saved_file.close()

def open_file():
  file =filedialog.askopenfile(mode='r',filetypes=[('text files','*.txt')])
  if file is not None:
    content=file.read()
  entry.insert(INSERT,content)

b1=Button(root,width='20',height='2',bg="#fff",text="save file",command=save_file)   
b1.place(x=100,y=5)

b2=Button(root,width='20',height='2',bg="#fff",text="open file",command=open_file)
b2.place(x=300,y=5)

entry=Text(root,width=72,height=33, wrap=WORD)
entry.place(x=10,y=60)

root.mainloop()