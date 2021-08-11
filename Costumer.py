from tkinter import *
from pymysql import *
import pymysql.cursors
from tkinter import messagebox
from datetime import *

win=Tk()
win.geometry("500x366")
win.title("Welcome to the main page")
win.resizable(0,0)
win.config(bg="#e0c568")
mainlb = Label(win,text="Welcome to ATM",width=32,height=1,font="Times 20",bg="#D198C5",relief=RAISED,bd=10).place(x=1,y=2)
def deposit():
    upwin=Tk()
    upwin.geometry("380x250")
    upwin.title("Welcome to the deposit")
    upwin.resizable(0,0)
    upwin.config(bg = "#5d00ff")

    asklb=Label(upwin,text="Enter account number",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=20)
    asktb.place(x=230,y=40)

    vallb=Label(upwin,text="Enter pin",font="Times 15").place(x=26,y=90)

    val=StringVar()
    valtb = Entry(upwin,textvariable=val,width=20)
    valtb.place(x=230,y=90)

    nwlb=Label(upwin,text="Enter ammount",font="Times 15").place(x=26,y=140)

    nw=StringVar()
    nwtb = Entry(upwin,textvariable=nw,width=20)
    nwtb.place(x=230,y=140)

    def depo():
       
        acc=asktb.get()
        pi=valtb.get()
        am=nwtb.get()
       
        conn = connect(host="localhost",user="root",password="",db='admin')
        var = conn.cursor()
        var.execute("select * from users where Account='"+acc+"' and Password='"+pi+"' ")
        row=var.rowcount
        if(row>0):
            var.execute("update users set Cash=Cash+'"+am+"' where Account='"+acc+"' and Password='"+pi+"' ")
            conn.commit()
            messagebox.showinfo("Information","deposited  successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")

    updatebtn=Button(upwin,text="deposit",font="Times 10",relief=RAISED,bd=8,command=depo).place(x=150,y=200)
       
def withdraw():
    upwin=Tk()
    upwin.geometry("380x260")
    upwin.title("Welcome to the withdraw")
    upwin.resizable(0,0)
    upwin.config(bg = "#5d00ff")
  

    asklb=Label(upwin,text="Enter account number",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=20)
    asktb.place(x=230,y=40)

    vallb=Label(upwin,text="Enter pin",font="Times 15").place(x=26,y=90)

    val=StringVar()
    valtb = Entry(upwin,textvariable=val,width=20)
    valtb.place(x=230,y=90)

    nwlb=Label(upwin,text="Enter ammount",font="Times 15").place(x=26,y=140)

    nw=StringVar()
    nwtb = Entry(upwin,textvariable=nw,width=20)
    nwtb.place(x=230,y=140)

    def minus():
       
        acc=asktb.get()
        pi=valtb.get()
        am=nwtb.get()
       
        conn = connect(host="localhost",user="root",password="",db='admin')
        var = conn.cursor()
        var.execute("select * from users where Account='"+acc+"' and Password='"+pi+"' ")
        
        row=var.rowcount
        if(row>0):
            var.execute("update users set Cash=Cash-'"+am+"' where Account='"+acc+"' and Password='"+pi+"' ")
            conn.commit()
            messagebox.showinfo("Information","withdrawl successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")
            
    updatebtn=Button(upwin,text="withdrwal",font="Times 10",relief=RAISED,bd=8,command=minus).place(x=150,y=200)
      

def fastcash():
    win=Tk()
    win.geometry("380x280")
    win.title("Welcome to fast cash")
    win.resizable(0,0)
    win.config(bg = "#5d00ff")

    asklb=Label(win,text="Enter account number",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(win,textvariable=ask,width=20)
    asktb.place(x=230,y=40)

    vallb=Label(win,text="Enter pin",font="Times 15").place(x=26,y=90)

    val=StringVar()
    valtb = Entry(win,textvariable=val,width=20)
    valtb.place(x=230,y=90)

    def two():
        
        acc=asktb.get()
        pi=valtb.get()
        
        
        conn = connect(host="localhost",user="root",password="",db='admin')
        var = conn.cursor()
        var.execute("select * from users where Account='"+acc+"' and Password='"+pi+"' ")
        row=var.rowcount
        if(row>0):
            var.execute("update users set Cash=amount-'200' where Account='"+acc+"' and Password='"+pi+"' ")
            conn.commit()
            messagebox.showinfo("Information","withdrawl successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")

    def five():
        
        acc=asktb.get()
        pi=valtb.get()
        
        
        conn = connect(host="localhost",user="root",password="",db='admin')
        var = conn.cursor()
        var.execute("select * from users where Account='"+acc+"' and Password='"+pi+"' ")
        row=var.rowcount
        if(row>0):
            var.execute("update users set Cash=amount-'500' where Account='"+acc+"' and Password='"+pi+"' ")
            conn.commit()
            messagebox.showinfo("Information","withdrawl successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")

    def thousand():
        
        acc=asktb.get()
        pi=valtb.get()
        
        
        conn = connect(host="localhost",user="root",password="",db='admin')
        var = conn.cursor()
        var.execute("select * from users where Account='"+acc+"' and Password='"+pi+"' ")
        row=var.rowcount
        if(row>0):
            var.execute("update users set Cash=amount-'1000' where Account='"+acc+"' and Password='"+pi+"' ")
            conn.commit()
            messagebox.showinfo("Information","withdrawl successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")

    def twoth():
        acc=asktb.get()
        pi=valtb.get()
        
        
        conn = connect(host="localhost",user="root",password="",db='admin')
        var = conn.cursor()
        var.execute("select * from users where Account='"+acc+"' and Password='"+pi+"' ")
        row=var.rowcount
        if(row>0):
            var.execute("update users set Cash=amount-'1000' where Account='"+acc+"' and Password='"+pi+"' ")
            conn.commit()
            messagebox.showinfo("Information","withdrawl successfully")
        else:
            messagebox.showinfo("Information","not valid")
            conn.rollback()
            messagebox.showinfo("Information","Data Transfer Failed")
            

    submitbtn = Button(win,text="200",width=15,height=1,font="Times 11",relief=RAISED,bd=10,command=two).place(x=40,y=140)
    deletebtn = Button(win,text="500",width=15,height=1,font="Times 11",relief=RAISED,bd=10,command=five).place(x=200,y=140)
    updatebtn = Button(win,text="1000",width=15,height=1,font="Times 11",relief=RAISED,bd=10,command=thousand).place(x=40,y=200)
    showbtn = Button(win,text="2000",width=15,height=1,font="Times 11",relief=RAISED,bd=10,command=twoth).place(x=200,y=200)

    


def balenq():
    upwin=Tk()
    upwin.geometry("400x200")
    upwin.title("Welcome to the transfer page")
    upwin.resizable(0,0)
    upwin.config(bg = "#5d00ff")

    asklb=Label(upwin,text="Enter account number ",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=20)
    asktb.place(x=250,y=40)

    vallb=Label(upwin,text="Enter pin",font="Times 15").place(x=26,y=90)

    val=StringVar()
    valtb = Entry(upwin,textvariable=val,width=20)
    valtb.place(x=250,y=90)

    def bal():
        acc=asktb.get()
        blc=valtb.get()
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='admin')
            a=conn.cursor()

            a.execute("select Cash from users where Account='"+acc+"'and Password='"+blc+"'")
            results=a.fetchall()
            count=a.rowcount
            if(count>0):
                for row in results:
                    for j in range(0,count):
                        messagebox.showinfo("Balance",row[j])
            else:
                #print("Not Found")
                messagebox.showinfo("message","not found")
        except:
            conn.rollback()
            messagebox.showinfo("message","not change")
            conn.close()  

    updatebtn=Button(upwin,text="show",font="Times 11",relief=RAISED,bd=10,command=bal).place(x=150,y=130)    
       
def pinchange():
    upwin=Tk()
    upwin.geometry("420x300")
    upwin.title("Welcome to the main page")
    upwin.resizable(0,0)
    upwin.config(bg = "#5d00ff")

    asklb=Label(upwin,text="Enter account ",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=20)
    asktb.place(x=220,y=40)

    vallb=Label(upwin,text="Enter old pin!",font="Times 15").place(x=26,y=90)

    val=StringVar()
    valtb = Entry(upwin,textvariable=val,width=20)
    valtb.place(x=220,y=90)

    nwlb=Label(upwin,text="Enter new pin!",font="Times 15").place(x=26,y=140)

    nw=StringVar()
    nwtb = Entry(upwin,textvariable=nw,width=20)
    nwtb.place(x=220,y=140)

    relb=Label(upwin,text="Re-Enter the new pin",font="Times 15").place(x=26,y=190)

    re=StringVar()
    retb = Entry(upwin,textvariable=re,width=20)
    retb.place(x=220,y=190)

    def change():
        acc=asktb.get()
        ol=valtb.get()
        np=nwtb.get()
        cn=retb.get()
        try:
            if(np==cn):
                conn=pymysql.connect(host='localhost',user='root',password='',db='admin')
                a=conn.cursor()
                a.execute("update users set Password='"+np+"' where Account='"+acc+"' and Password='"+ol+"'")
                conn.commit()
                messagebox.showinfo("message","change")
            else:
                messagebox.showinfo("message","not match password")
        except:
             conn.rollback()
             messagebox.showinfo("message","not change")
             conn.close()

    updatebtn=Button(upwin,text="change",font="Times 10",relief=RAISED,bd=10,command=change).place(x=150,y=240)

def conchange():
    upwin=Tk()
    upwin.geometry("500x340")
    upwin.title("Welcome to contact page details")
    upwin.resizable(0,0)
    upwin.config(bg = "#5d00ff")

    asklb=Label(upwin,text="Enter account number",font="Times 15").place(x=26,y=40)

    ask=StringVar()
    asktb = Entry(upwin,textvariable=ask,width=20)
    asktb.place(x=280,y=40)

    pilb=Label(upwin,text="Enter pin",font="Times 15").place(x=26,y=90)

    pi=StringVar()
    pitb = Entry(upwin,textvariable=pi,width=20)
    pitb.place(x=280,y=90)

    oldlb=Label(upwin,text="Enter old contact number!",font="Times 15").place(x=26,y=140)

    old=StringVar()
    oldtb = Entry(upwin,textvariable=old,width=20)
    oldtb.place(x=280,y=140)

    nwlb=Label(upwin,text="Enter new contact number",font="Times 15").place(x=26,y=190)

    nw=StringVar()
    nwtb = Entry(upwin,textvariable=nw,width=20)
    nwtb.place(x=280,y=190)

    relb=Label(upwin,text="Re-Enter the new  pin",font="Times 15").place(x=26,y=240)

    re=StringVar()
    retb = Entry(upwin,textvariable=re,width=20)
    retb.place(x=280,y=240)

    def changecon():
        acc=asktb.get()
        pii=pitb.get()
        ol=oldtb.get()
        new=nwtb.get()
        ree=retb.get()
    
        try:
            if(ree==new):
                conn=pymysql.connect(host='localhost',user='root',password='',db='admin')
                a=conn.cursor()
                a.execute("update users set Mobile='"+new+"' where Account='"+acc+"' and Password='"+pii+"' and Mobile='"+ol+"'")
                conn.commit()
                messagebox.showinfo("message","change")
            else:
                messagebox.showinfo("message","not match password")
        except:
             conn.rollback()
             messagebox.showinfo("message","not change")
             conn.close()

    updatebtn=Button(upwin,text="change",font="Times 10",relief=RAISED,bd=10,command=changecon).place(x=200,y=290)

    



    

submitbtn = Button(win,text="Deposit Cash",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=deposit).place(x=30,y=85)
deletebtn = Button(win,text="Withdraw Cash",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=withdraw).place(x=30,y=155)

deletebtn = Button(win,text="Fast Cash",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=fastcash).place(x=275,y=85)
updatebtn = Button(win,text="Blanace Enquiry",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=balenq).place(x=30,y=225)

updatebtn = Button(win,text="Change Pin",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=pinchange).place(x=275,y=155)
showbtn = Button(win,text="Update Contact ",width=15,height=1,font="Times 15",relief=RAISED,bd=10,command=conchange).place(x=275,y=225)

lastlb = Label(win,text="We are happy to serve you",width=32,height=1,bg="#D198C5",font="Times 20",relief=RAISED,bd=10).place(x=1,y=310)



win.mainloop()
