from ast import Lambda
from tkinter import*
root=Tk()
root.title("Calculator")
e=Entry(root,borderwidth=7,font=('Arial',24),width=40)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def button_click(number):
  c=e.get()
  e.delete(0,END)
  e.insert(0,str(c)+str(number))

def button_clear():
   d=e.get()
   n=len(d)
   e.delete(n-1,END)
def button_add():
  first_number=e.get()
  global f_num
  global math
  math="addition"
  f_num=int(first_number)
  e.delete(0,END)
def button_minus():
  first_number=e.get()
  global f_num
  global math
  math="subtraction"
  f_num=int(first_number)
  e.delete(0,END)
def button_multiply():
  first_number=e.get()
  global f_num
  global math
  math="multiplication"
  f_num=int(first_number)
  e.delete(0,END)
def button_divide():
  first_number=e.get()
  global f_num
  global math
  math="division"
  f_num=int(first_number)
  e.delete(0,END)
   
def button_equal():
   second_number=e.get()
   e.delete(0,END)
   if math=="addition":
     e.insert(0,f_num+int(second_number))
   if math=="multiplication":
      e.insert(0,f_num*int(second_number))
   if math=="subtraction":
      e.insert(0,f_num-int(second_number))
   if math=="division":
      e.insert(0,f_num/int(second_number))

    

button_1= Button(root,text="1",padx=80,pady=25,command=lambda: button_click("1"))
button_2= Button(root,text="2",padx=80,pady=25,command=lambda: button_click("2"))
button_3= Button(root,text="3",padx=80,pady=25,command=lambda: button_click("3"))
button_4= Button(root,text="4",padx=80,pady=25,command=lambda: button_click("4"))
button_5= Button(root,text="5",padx=80,pady=25,command=lambda: button_click("5"))
button_6= Button(root,text="6",padx=80,pady=25,command=lambda: button_click("6"))
button_7= Button(root,text="7",padx=80,pady=25,command=lambda: button_click("7"))
button_8= Button(root,text="8",padx=80,pady=25,command=lambda: button_click("8"))
button_9= Button(root,text="9",padx=80,pady=25,command=lambda: button_click("9"))
button_0= Button(root,text="0",padx=80,pady=25,command=lambda: button_click("0"))
button_add= Button(root,text="+",padx=80,pady=25,command=button_add)
button_minus=Button(root,text="-",padx=80,pady=25,command=button_minus)
button_multiply=Button(root,text="x",padx=80,pady=25,command=button_multiply)
button_divide=Button(root,text="/",padx=80,pady=25,command=button_divide)

button_equal=Button(root,text="=",padx=110,pady=25,command=button_equal)
button_clear=Button(root,text="Clear",padx=80,pady=25,command=button_clear)

button_1.grid(row=3,column=0,sticky="nsew")
button_2.grid(row=3,column=1,sticky="nsew")
button_3.grid(row=3,column=2,sticky="nsew")
button_5.grid(row=2,column=1,sticky="nsew")
button_4.grid(row=2,column=0,sticky="nsew")
button_6.grid(row=2,column=2,sticky="nsew")
button_7.grid(row=1,column=0,sticky="nsew")
button_8.grid(row=1,column=1,sticky="nsew")
button_9.grid(row=1,column=2,sticky="nsew")
button_0.grid(row=4,column=0,sticky="nsew")
button_add.grid(row=3,column=3,sticky="nsew")
button_minus.grid(row=2,column=3,sticky="nsew")
button_multiply.grid(row=1,column=3,sticky="nsew")
button_divide.grid(row=4,column=3,sticky="nsew")
button_equal.grid(row=4,column=1,sticky="nsew")
button_clear.grid(row=4,column=2,sticky="nsew")


root.mainloop()