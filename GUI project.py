from tkinter import*
import random
import os
import time
d={'1':1}
d1={}
d2={}
d3={}
d4={'1':1}
d5={}
d6={}
d7={'1':"",'2':""}
global bill
bill={}
global ct
ct={}
global i
i=1
def welcome():
    
    rt=Tk()
    rt.geometry("1600x800+0+0")
    rt.title("WELCOME TO SBI")
    Tops=Frame(rt,width=1600,height=800,bg="powder blue",relief=SUNKEN)
    Tops.pack(side=TOP)
    f=Frame(rt,width=1600,height=200,bg="powder blue",relief=SUNKEN)
    f.pack(side=BOTTOM)

    l=Label(Tops,font=('arial',50,'bold'),text="WELCOME TO SBI",fg="Steel blue",bd=10,anchor='w')
    l.grid(row=0,column=0)
    l=Label(Tops,font=('arial',20,'bold'),text="INORDER TO CREATE YOUR ACCOUNT AT SBI PRESS CONTINUE",fg="Steel blue",bd=10,anchor='w')
    l.grid(row=1,column=0)
    b=Button(f,padx=45,pady=45,bd=8,fg="black",font=('arial',20,'bold'),text="CONTINUE",bg="powder blue",command=lambda: rt.destroy()).grid(row=0,column=0)
    rt.mainloop()
welcome()
def createAccount():
    rt=Tk()
    rt.geometry("1600x800+0+0")
    T=Frame(rt,width=1600,height=800,bg="steel blue",relief=SUNKEN)
    T.pack(side=TOP)
    e=Entry(T,font=("default",75),bg="black",fg="white")
    e.grid(row=0,column=1)
    e.insert(0,"ENTER YOUR PIN")
    f=Frame(rt,width=1600,height=200,bg="powder blue",relief=SUNKEN)
    f.pack(side=BOTTOM)
    l=Label(f,font=('arial',45,'bold'),text="PRESS ENTER TO SAVE AND EXIT TO END",fg="Steel blue",bd=10,anchor='w')
    l.grid(row=0,column=0)
    
    def fun1():
        if len(d)==2: 
             d3.update({'1':e.get()})
             if (d1.get(d3.get('1'))):
                 pass
             else:
                 d1.update({e.get():0})
             e.delete(0,END)
             e.insert(0,"DEPOSIT YOUR MONEY AND PRESS ENTER")
             
             d.update({'3':3})
             
             return()
        if len(d)==3:
            
            if (d1.get(d3.get('1'))):
                d1[d3.get('1')]=(int(d1.get(d3.get('1')))+int(e.get()))
            else:
                d1.update({d3.get('1'):e.get()})
            def moreAccount():
                rf=Tk()
                rf.geometry("1600x800+0+0")
                
                Tp=Frame(rf,width=1600,height=800,bg="powder blue",relief=SUNKEN)
                Tp.pack(side=TOP)
                f2=Frame(rf,width=1600,height=200,bg="powder blue",relief=SUNKEN)
                f2.pack(side=BOTTOM)

                l1=Label(Tp,font=('arial',50,'bold'),text="ACCOUNT CREATED",fg="Steel blue",bd=10,anchor='w')
                l1.grid(row=0,column=0)
                l1=Label(Tp,font=('arial',20,'bold'),text="DO YOU WANT TO CREATE MORE ACCOUNT ?",fg="Steel blue",bd=10,anchor='w')
                l1.grid(row=1,column=0)
                def hello():
                    d3.clear()
                    e.delete(0,END)
                    e.insert(0,"ENTER YOUR PIN")
                    del(d['3'])
                    del(d['2'])
                    rf.destroy()
                def hello1():
                    rf.destroy()
                    rt.destroy()
                b99=Button(f2,padx=45,pady=45,bd=8,fg="black",font=('arial',20,'bold'),text="YES",bg="powder blue",command=lambda: hello()).grid(row=0,column=0)
                b98=Button(f2,padx=45,pady=45,bd=8,fg="black",font=('arial',20,'bold'),text="NO",bg="powder blue",command=lambda: hello1()).grid(row=0,column=1)
                rf.mainloop()
            moreAccount()
            
        
    def fun(s):
        if len(d)==1:
            e.delete(0,END)
            d.update({'2':2})
            d2.update({'1':1})
            
        if (len(d)==3)&(len(d2)==1):
            d2.clear()
            e.delete(0,END)
        e.insert(END,s)
        

    b=Button(T,text="1",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("1"))
    b.grid(row=1,column=0)
    b.config(height=3,width=10)
    
    b1=Button(T,text="2",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("2"))
    b1.grid(row=1,column=1)
    b1.config(height=3,width=10)
    b2=Button(T,text="3",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("3"))
    b2.grid(row=1,column=2)
    b2.config(height=3,width=10)

    b3=Button(T,text="4",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("4"))
    b3.grid(row=2,column=0)
    b3.config(height=3,width=10)
    b4=Button(T,text="5",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("5"))
    b4.grid(row=2,column=1)
    b4.config(height=3,width=10)
    b5=Button(T,text="6",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("6"))
    b5.grid(row=2,column=2)
    b5.config(height=3,width=10)

    b6=Button(T,text="7",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("7"))
    b6.grid(row=3,column=0)
    b6.config(height=3,width=10)
    b7=Button(T,text="8",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("8"))
    b7.grid(row=3,column=1)
    b7.config(height=3,width=10)
    b8=Button(T,text="9",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("9"))
    b8.grid(row=3,column=2)
    b8.config(height=3,width=10)
    b9=Button(T,text="0",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("0"))
    b9.grid(row=4,column=1)
    b9.config(height=3,width=10)
    b10=Button(T,text="Del",font=("default",15),bg="black",fg="white",command=lambda :e.delete(0,END))
    b10.grid(row=4,column=0)
    b10.config(height=3,width=10)
    b11=Button(T,text="ENTER",font=("default",15),bg="yellow",fg="black",command=lambda :fun1())
    b11.grid(row=4,column=2)
    b11.config(height=3,width=10)
    b12=Button(T,text="EXIT",font=("default",15),bg="red",fg="black",command=lambda :os._exit(0))
    b12.grid(row=5,column=1)
    b12.config(height=3,width=10)
    rt.mainloop()
createAccount()    
# WITHDRAWL#####################################################################################################################################################
def withdrawl():
    def welcomeOfWithdraw():
        rg=Tk()
        rg.geometry("1600x800+0+0")
        Tops=Frame(rg,width=1600,height=800,bg="powder blue",relief=SUNKEN)
        Tops.pack(side=TOP)
        f=Frame(rg,width=1600,height=200,bg="powder blue",relief=SUNKEN)
        f.pack(side=BOTTOM)

        l=Label(Tops,font=('arial',50,'bold'),text="DO YOU WANT TO WITHDRAW MONEY ?",fg="Steel blue",bd=10,anchor='w')
        l.grid(row=0,column=0)
        l=Label(Tops,font=('arial',20,'bold'),text="INSERT YOUR ATM CARD AND PRESS ENTER TO CONTINUE",fg="Steel blue",bd=10,anchor='w')
        l.grid(row=1,column=0)
        b=Button(f,padx=45,pady=45,bd=8,fg="black",font=('arial',20,'bold'),text="ENTER",bg="powder blue",command=lambda: rg.destroy()).grid(row=0,column=0)
        rg.mainloop()
    welcomeOfWithdraw()
    rt=Tk()
    rt.geometry("1600x800+0+0")
    T=Frame(rt,width=1600,height=800,bg="steel blue",relief=SUNKEN)
    T.pack(side=TOP)
    e=Entry(T,font=("default",75),bg="black",fg="white")
    e.grid(row=0,column=1)
    e.insert(0,"ENTER YOUR PIN")
    f=Frame(rt,width=1600,height=200,bg="powder blue",relief=SUNKEN)
    f.pack(side=BOTTOM)
    l=Label(f,font=('arial',45,'bold'),text="PRESS ENTER TO SAVE AND EXIT TO END",fg="Steel blue",bd=10,anchor='w')
    l.grid(row=0,column=0)
    
    def fun1():
        
        if len(d4)==2:
            if d1.get(d7.get('1')):
                e.delete(0,END)
                e.insert(0,"WITHDRAW  MONEY")
                d4.update({'3':3})
                
                return()
            else:
                
                e.delete(0,END)
                e.insert(0,"WRONG PIN")
                del(d4['2'])
                del(d5['1'])
                del(d7['1'])
                d7.update({'1':""})
            
                       
             
        if len(d4)==3:
            if int((d1.get(d7.get('1'))))>=int(d7.get('2')):
                global bill
                global i
                global ct
                bill.update({i:d7.get('2')})
                ct.update({i:time.ctime()})
                i+=1
                
                
                
                d1[d7.get('1')]=str(int(d1.get(d7.get('1')))-int(d7.get('2')))
                def moreWithdraw():
                    
                    rf=Tk()
                    rf.geometry("1600x800+0+0")
                
                    Tp=Frame(rf,width=1600,height=800,bg="powder blue",relief=SUNKEN)
                    Tp.pack(side=TOP)
                    f2=Frame(rf,width=1600,height=200,bg="powder blue",relief=SUNKEN)
                    f2.pack(side=BOTTOM)

                    l1=Label(Tp,font=('arial',50,'bold'),text="TRANSACTION IS SUCCESSFUL",fg="Steel blue",bd=10,anchor='w')
                    l1.grid(row=0,column=0)
                    l1=Label(Tp,font=('arial',20,'bold'),text="DO YOU WANT MORE TRANSACTION ?",fg="Steel blue",bd=10,anchor='w')
                    l1.grid(row=1,column=0)
                    def hello():
                        i1=+1
                        e.delete(0,END)
                        e.insert(0,"WITHDRAW MONEY")
                        del(d7['2'])
                        d7.update({'2':""})
                        d5.update({'1':1})
                        rf.destroy()
                    def hello1():
                        rf.destroy()
                        rt.destroy()
                    b99=Button(f2,padx=45,pady=45,bd=8,fg="black",font=('arial',20,'bold'),text="YES",bg="powder blue",command=lambda: hello()).grid(row=0,column=0)
                    b98=Button(f2,padx=45,pady=45,bd=8,fg="black",font=('arial',20,'bold'),text="NO",bg="powder blue",command=lambda: hello1()).grid(row=0,column=1)
                    rf.mainloop()
                moreWithdraw()
                
            else:
                e.delete(0,END)
                e.insert(0,"BALANCE IS LOW")
                del(d7['2'])
                d7.update({'2':""})
                d5.update({'1':1})
           
         
        
    def fun(s):
        
        if len(d4)==1:
            e.delete(0,END)
            d4.update({'2':2})
            d5.update({'1':1})
            
        if (len(d4)==3)&(len(d5)==1):
            d5.clear()
            e.delete(0,END)
        if len(d4)==3: 
            e.insert(END,s)
            d7.update({'2':(d7.get('2')+s)})
        else:
            e.insert(0,"X")
            d7.update({'1':(d7.get('1')+s)})
    b=Button(T,text="1",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("1"))
    b.grid(row=1,column=0)
    b.config(height=3,width=10)
    
    b1=Button(T,text="2",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("2"))
    b1.grid(row=1,column=1)
    b1.config(height=3,width=10)
    b2=Button(T,text="3",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("3"))
    b2.grid(row=1,column=2)
    b2.config(height=3,width=10)
    b3=Button(T,text="4",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("4"))
    b3.grid(row=2,column=0)
    b3.config(height=3,width=10)
    b4=Button(T,text="5",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("5"))
    b4.grid(row=2,column=1)
    b4.config(height=3,width=10)
    b5=Button(T,text="6",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("6"))
    b5.grid(row=2,column=2)
    b5.config(height=3,width=10)

    b6=Button(T,text="7",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("7"))
    b6.grid(row=3,column=0)
    b6.config(height=3,width=10)
    b7=Button(T,text="8",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("8"))
    b7.grid(row=3,column=1)
    b7.config(height=3,width=10)
    b8=Button(T,text="9",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("9"))
    b8.grid(row=3,column=2)
    b8.config(height=3,width=10)
    b9=Button(T,text="0",font=("default",15),bg="powder blue",fg="black",command=lambda :fun("0"))
    b9.grid(row=4,column=1)
    b9.config(height=3,width=10)
    b10=Button(T,text="Del",font=("default",15),bg="black",fg="white",command=lambda :e.delete(0,END))
    b10.grid(row=4,column=0)
    b10.config(height=3,width=10)
    b11=Button(T,text="ENTER",font=("default",15),bg="green",fg="black",command=lambda :fun1())
    b11.grid(row=4,column=2)
    b11.config(height=3,width=10)
    b12=Button(T,text="EXIT",font=("default",15),bg="red",fg="black",command=lambda :os._exit(0)())
    b12.grid(row=5,column=1)
    b12.config(height=3,width=10)
    rt.mainloop()
     
withdrawl()
   

def showBill():
    rt=Tk()
    rt.geometry("1600x800+0+0")
    rt.title("WELCOME TO SBI")
    Tops=Frame(rt,width=1600,height=800,bg="powder blue",relief=SUNKEN)
    Tops.pack(side=TOP)
    f=Frame(rt,width=1600,height=200,bg="powder blue",relief=SUNKEN)
    f.pack(side=BOTTOM)
    j=1
    l=Label(Tops,font=('arial',50,'bold'),text="SBI DEBIT BILL",fg="Steel blue",bd=10,anchor='w')
    l.grid(row=0,column=0)
    for i in bill: 
        l=Label(Tops,font=('arial',20,'bold'),text="RUPEES "+str(bill.get(i))+" WITHDRAWN FROM YOUR ACCOUNT  AT TIME "+str(ct.get(i)),fg="Steel blue",bd=10,anchor='w')
        l.grid(row=j,column=0)
        j+=1
    l=Label(Tops,font=('arial',40,'bold'),text="CURRENT BALANCE IS "+str(d1[d7.get('1')]),fg="Steel blue",bd=10,anchor='w')
    l.grid(row=j,column=0)

    
showBill()
    
    




    

    
