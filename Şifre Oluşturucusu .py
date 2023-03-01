import random
from tkinter import *
import string
from tkinter.font import Font

def sifre_olustur():
  password=[]
  for i in range(7):
    alpha=random.choice(string.ascii_letters)
    symbol=random.choice(string.punctuation)
    numbers=random.choice(string.digits)
    password.append(alpha)
    password.append(symbol)
    password.append(numbers)
  y="".join(str(x)for x in password)
  lbl.config(text=y)

root=Tk()
root.geometry("1000x1280")
btn=Button(root,text="Şifre Oluştur !",command=sifre_olustur)
btn.place(relx=0.4, rely=0.4, anchor=N)
myFont = Font(family="Yukrx", size=12)
lbl=Label(root,font=myFont)
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()

print ("By Yukrx")
