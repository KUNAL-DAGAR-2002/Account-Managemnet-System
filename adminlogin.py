from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os



#Submit function

def Submit():
    user_name = uname.get()
    user_password = upassword.get()
    conn = pymysql.connect(host='localhost',user='root',password='',db='admin')
    a = conn.cursor()
    a.execute("select * from emp where Account ='"+user_name+"' and Password ='"+user_password+"'")
    result = a.fetchall()
    count = a.rowcount
    conn.commit()
    messagebox.showinfo("Info","Login Successful welcome admin")
    if(count>0):
        
        def ins():
            acnt = ACN.get()
            acp = ACP.get()
            iD = HID.get()
            Nam = HN.get()
            Mob = HM.get()
            con = pymysql.connect(host='localhost',user='root',password='',db='admin')
            b = con.cursor()
            b.execute("insert into userdata(id,Name,Account,Password,Mobile)values('"+iD+"','"+Nam+"','"+acnt+"','"+acp+"','"+Mob+"')")
            con.commit()
            print('done')
        def upd():
            ACNO = ACN.get()
            ACPIN = ACP.get()
            iD = HID.get()
            Nam = HN.get()
            Mob = HM.get()
            conn = pymysql.connect(host='localhost',user='root',password='',db='admin')
            c = conn.cursor()
            c.execute("update userdata set Account ='"+ACNO+"',Password='"+acp+"',Name='"+Nam+"',Mobile='"+Mob+"' where iD='"+HID+"'")
            conn.commit()
            print('done')
        def dele():
            ACNO = ACN.get()
            ACPIN = ACP.get()
            iD = HID.get()
            Nam = HN.get()
            Mob = HM.get()
            connn = pymysql.connect(host='localhost',user='root',password='',db='admin')
            d = connn.cursor()
            d.execute("delete from userdata where Account='"+ACNO+"' and Password = '"+ACPIN+"'")
            connn.commit()
            print('done')
        def getdata():
            connnn = pymysql.connect(host='localhost',user='root',password='',db='admin')
            e = connnn.cursor()
            e.execute("select * from userdata")
            get = e.fetchall()
            connnn.commit()
            output = ''
            for x in get:
                output = output+x[0]+' '+x[1]+' '+x[2]+' '+x[3]+' '+x[4]+' '+'\n'
            return(output)
            
            
        
        
       
        win.geometry("450x500")
        mainlb = Label(win,text="Welcome to Admin",width=29,height=1,font="Times 20",bg="#D198C5",relief=RAISED,bd=10).place(x=1,y=2)
        #Details
        AccountNum = Label(win , text = "Accout No",font="Times 15")
        AccountNum.place(x=30,y=85)
        ACN = StringVar()
        tab3 = Entry(win,textvariable = ACN)
        tab3.place(x=120,y=90,width=120)

        AccountPass = Label(win , text = "Password",font="Times 15")
        AccountPass.place(x= 30,y=150)
        ACP = StringVar()
        tab4 = Entry(win,textvariable = ACP)
        tab4.place(x=120,y=155,width=120)

        Name = Label(win , text = "Name",font="Times 15")
        Name.place(x=30,y=200)
        HN= StringVar()
        tab5 = Entry(win,textvariable = HN)
        tab5.place(x=120,y=200)

        ID = Label(win , text = "Unique ID",font="Times 15")
        ID.place(x=30,y=250)
        HID = StringVar()
        tab6 = Entry(win,textvariable = HID)
        tab6.place(x=120,y=250)

        Mobile = Label(win , text = "Mobile",font="Times 15")
        Mobile.place(x=30,y=300)
        HM = StringVar()
        tab7 = Entry(win,textvariable = HM)
        tab7.place(x=120,y=300)

        #submit Button
        submit= Button(win,text="Insert",command=ins,width=10,height=1,font="Times 10",relief=RAISED,bd=10)
        submit.place(x=300,y=110)
        submit= Button(win,text="Update",command=upd,width=10,height=1,font="Times 10",relief=RAISED,bd=10)
        submit.place(x=300,y=160)
        submit= Button(win,text="Delete",command=dele,width=10,height=1,font="Times 10",relief=RAISED,bd=10)
        submit.place(x=300,y=210)
        submit= Button(win,text="Show Data",command=lambda:text.insert(END,getdata()),width=10,height=1,font="Times 10",relief=RAISED,bd=10).place(x=300,y=260)
        

        '''Result = Label(win,text="Output ")
        Result.grid(row=6,column = 0)
        z = StringVar()'''
        text = Text(win,height = 6 , width = 40)
        text.place(x=30,y = 350)
        
        
win = Tk()
win.geometry("500x200")
win.title("Admin Pannel")
win.resizable(False,False)

mainlb = Label(win,text="Welcome to ATM",width=32,height=1,font="Times 20",bg="#D198C5",relief=RAISED,bd=10).place(x=1,y=2)


#Details
username = Label(win , text = "Username",font="Times 15")
username.place(x=30,y=85)
uname = StringVar()
tab = Entry(win,textvariable = uname)
tab.place(x=120,y=90,width=120)

password = Label(win , text = "Password" ,font="Times 15")
password.place(x= 30,y=150)
upassword = StringVar()
tab1 = Entry(win,textvariable = upassword)
tab1.place(x=120,y=155,width=120)

#submit Button
submit= Button(win,text="Login",command=Submit,width=10,height=1,font="Times 10",relief=RAISED,bd=10)
submit.place(x=300,y=110)


win.mainloop()
