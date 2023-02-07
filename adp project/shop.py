#- import modules
from tkinter import *
import tkinter as tk
from tkinter import messagebox

 
root = Tk()
root.geometry("900x450+0+0")
root.resizable(False,False)
root.title("Shop Management System ")
root.configure(width=1500,height=700,bg="#e3f4f1")
var=-1

def Add_Items():
    global variable
    EN1= Entry_1.get()
    EN2=Entry_2.get()
    EN3=Entry_3.get()
    EN4=Entry_4.get()
    EN5=Entry_5.get()
    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    Entry_3.delete(0, END)
    Entry_4.delete(0, END)
    Entry_5.delete(0, END)
    messagebox.showinfo("ADD ITEM", "ITEM ADDED SUCCESSFULLY....!!!!!")

def Delete_Items():
    EN1=Entry_1.get()
    Entry1.delete(0, END)
    Entry2.delete(0, END)
    Entry3.delete(0, END)
    Entry4.delete(0, END)
    Entry5.delete(0, END)
    messagebox.showinfo("DELETE ITEM", "ITEM DELETED SUCCESSFULLY....!!!!!")
 
    f.close()
    working.close()


def Search_Item():
    Entry1.delete(0, END)
    Entry2.delete(0, END)
    Entry3.delete(0, END)
    Entry4.delete(0, END)
    entry5.delete(0, END)
    i=0
    flag = 1
    E1 = Entry6.get()
    with open(r"Proj_Database") as working:
        for line in working:
            i=i+1
            if str(E1) in line:
                flag = 0
                break
        try:
           if flag != 1:
                v = list(line.split(" "))
                Entry1.delete(0, END)
                Entry2.delete(0, END)
                Entry3.delete(0, END)
                Entry4.delete(0, END)
                Entry5.delete(0, END)
                Entry1.insert(0, str(v[0]))
                Entry2.insert(0, str(v[1]))
                Entry3.insert(0, str(v[2]))
                Entry4.insert(0, str(v[3]))
                Entry5.insert(0, str(v[4]))
 
        except:
            messagebox.showinfo("Title", "Error end of file")
 
        if flag !=0:
            messagebox.showinfo("Title", "NOT FOUND")
    working.close()

def Clear_Item():
    Entry1.delete(0, END)
    Entry2.delete(0, END)
    Entry3.delete(0, END)
    Entry4.delete(0, END)
    Entry5.delete(0, END)
    Entry6.delete(0, END)

def Exit():
    Exit= messagebox.askyesno("Exit the System","Do you want to Exit?...THANKS... :)")
    if Exit > 0:
        root.destroy()
        return

#All labels Entrys Button grid place
Label_0= Label(root,text="SHOP MANAGEMENT SYSTEM ",fg="black",font=("Times new roman", 30, 'bold'))
Label_0.grid(columnspan=6)
 
Label_1=Label(root,text="ENTER ITEM NAME",bg="#e8c1c7",fg="black",bd=8,font=("Times new roman", 12, 'bold'),width=25)
Label_1.grid(row=1,column=0)
Entry_1=Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_1.grid(row=1,column=1)
 
Label_2=Label(root, text="ENTER ITEM PRICE",height="1",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=25)
Label_2.grid(row=2,column=0)
Entry_2= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_2.grid(row=2,column=1)
 
Label_3=Label(root, text="ENTER ITEM QUANTITY",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=25)
Label_3.grid(row=3,column=0)
Entry_3= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_3.grid(row=3,column=1)
 
Label_4=Label(root, text="ENTER ITEM CATEGORY",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=25)
Label_4.grid(row=4,column=0)
Entry_4= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_4.grid(row=4,column=1)
 
Label_5=Label(root, text="ENTER ITEM DISCOUNT",bg="#e8c1c7",fg="black",bd=8, font=("Times new roman", 12, 'bold'),width=25)
Label_5.grid(row=5,column=0, padx=10, pady=10)
Entry_5= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_5.grid(row=5,column=1, padx=10, pady=10)
 
Button_1= Button(root,text="ADD ITEM",bd=8, bg="#49D810", fg="black", width=25, font=("Times new roman", 12),command=Add_Items)
Button_1.grid(row=6,column=0, padx=10, pady=10)
Button_2= Button(root, text="DELETE ITEM",bd=8, bg="#49D810", fg="black", width =25, font=("Times new roman", 12),command=Delete_Items)
Button_2.grid(row=6,column=1, padx=40, pady=10)
Button_4= Button(root, text="SEARCH ITEM",bd=8, bg="#49D810", fg="black", width =25, font=("Times new roman", 12),command=Search_Item)
Button_4.grid(row=2,column=3, padx=40, pady=10)
Button_5= Button(root, text="CLEAR SCREEN",bd=8, bg="#49D810", fg="black", width=25, font=("Times new roman", 12),command=Clear_Item)
Button_5.grid(row=4,column=3, padx=40, pady=10)
Button_6= Button(root,highlightcolor="blue",activebackground="red", text="Exit",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 40),command=Exit)
Button_6.place(x=635,y=337,height= 102,width=245)
Entry_6= Entry(root, font=("Times new roman", 14),justify='left',bd=8,width=25)
Entry_6.grid(row=1,column=3, padx=10, pady=10)
 
root.mainloop()
