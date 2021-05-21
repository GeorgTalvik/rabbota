from tkinter import *
foto_list=["pc1.png","pc2.png","pc3.png","pc4.png","pc5.png"]
ttt="ttt"
list_ = ["Компьютер1","Компьютер2","Компьютер3","Компьютер4","Компьютер5"]
def list_to_txt(event):
    global can,foto
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))
    can.delete(ALL)
    foto=PhotoImage(file=foto_list[valik[0]])
    can.create_image(0,0,image=foto,anchor=NW)

def txt_to_list(event):
    text=txt.get(0.0,END)
    text=text[-2:-1]
    if text=="\n":
        pass
    else:
        list_.append(text)
        print(list_)
        lbox.config(height=len(list_))
        lbox.insert(END,text)   
        txt.delete(0.0,END)
def opisanie():
    global ttt
    text = txt.get(0.0, END)
    print(list(text))
    if text=="Компьютер5\n":
        ttt="игровой компьютер имеет 960m видеокарту 16 гб оперативной памяти 500w блок питания стоит 700 евро"
    elif text=="Компьютер2\n":
        ttt="компьтер игровой имеет видео карту ртх 3090, процессор i9, 32гб оперативной памяти ddr4, стоит он 2000 евро."
    elif text=="Компьютер1 \n":
        ttt=" игровой компьютер он имеет core i5, 16гб оперативной памяти, 500w, 1050 видеокарта "
    elif text=="Компьютер4\n":
        ttt="компьютер стоит 900 евро он игровой "
    elif text=="Компьютер3\n":
        ttt="Компьютер имеет core i5 видеокарту 1050, 16 гб оперативной памяти, компьютер стоит 500 евро."
    else:
        ttt="Компьютер"
    opis.config(text=ttt)



win=Tk()
win.geometry("600x700")
win.title("Проверочная работа")
lbox=Listbox(win,width=25,height=7,selectmode=SINGLE)
lbox.insert(1, "Компьютер1 ")
lbox.insert(2, "Компьютер2")
lbox.insert(3, "Компьютер3")
lbox.insert(4, "Компьютер4")
lbox.insert(5, "Компьютер5")
for element in foto_list:
    lbox.insert(END,element)

lbox.grid(row=0,column=0)
lbox.bind("<<ListboxSelect>>",list_to_txt)
txt=Text(win,height=4,width=20,wrap=WORD)
txt.grid(row=1,column=1)
txt.bind("<Return>",txt_to_list)
can=Canvas(win,width=400,height=400,bg="gold")
can.grid(row=1,column=2,columnspan=2)
pc = PhotoImage(file="")#220px-PelobatesFuscus.png
panel = Label(win, image = pc)
panel.grid(row=1, column=3)
foto=PhotoImage(file="pc3.png")
btn=Button(text='Информация ', command=opisanie)
btn.grid(row=1, column=2)
opis=Label(win, text="", width=60, height=30)
opis.grid(row=5, column=6)
can.grid(row=4, column=6)
win.mainloop()


