import qrcode
# import PIL.Image
import pymysql
from tkinter import *
import tkinter as tk
import random
import time
import datetime
# root=Tk()
# Ent1=Entry(root)
# Ent2=Entry(root)

def clear(Ent1,Ent2):
    Ent1.insert(0,"")
    Ent2.insert(0,"")

def search(Ent1,Ent2):
    try:
        con=pymysql.connect(user='root',password='',host='localhost',database='parking_db')
        cur=con.cursor()
        print(cur)
        sql="select * from slots where status='0'"
        cur.execute(sql)
        print("status vali line")
        res=cur.fetchone()
        print("i am res",res)
        Ent2.delete(0, END)
        Ent2.insert(0,res[0])
        print(Ent1,Ent2)
        con.close()
    except:
        print('no data found')


def inst(Ent1,Ent2):
    try:
        dt=str(datetime.datetime.now().date())
        tm = str(datetime.datetime.now().time())
        con=pymysql.connect(user='root',password='',host='localhost',database='parking_db')
        cur=con.cursor()
        print("inserting into bookings table")
        sql="INSERT INTO `bookings` (`Id`, `vehicle_num`,`slot`,`dop`,`top`) VALUES (NULL, %s, %s, %s ,%s)"
        val=(Ent1.get(),Ent2.get(),dt,tm)
        print(Ent1.get(),Ent2.get())
        cur.execute(sql,val)
        con.commit()
        print("hi")
        try:
            print('1')
            print(con)
            cur1=con.cursor()
            print(cur1)
            print("mmmm")
            sql1 = "UPDATE slots SET status = %s WHERE id = %s "
            val1 = ("1",Ent2.get())
            print(Ent2.get())
            cur1.execute(sql1,val1)
            con.commit()
            print("slot update")

        except:
            print('error','No Data Inserted')
        finally:
            qr=qrcode.make(Ent2.get()+dt+tm[0:8]+Ent1.get())
            print("inside finally")
            qr.save('myqr.png')
            from PIL import Image
            img = Image.open('myqr.png')
            img.show()
        con.close()
        print('success','Data Inserted')
    except:
        print('!!no data Inserted')
    finally:
        clear(Ent1, Ent2)




def gui(number):
    window = Tk()
    window.title("Update Data")
    window.geometry("1000x500+0+0")
    top=Frame(window,width = 1000)
    top.pack()
    titl=Label(top,font=('arial',50,'bold'),text="Car Parking System")
    titl.grid()
    mid=Frame(window,width =1000)
    mid.pack()
    txt1=Label(mid,font=('arial',20),text="Vehicle no : ")
    txt1.grid(row=0,column=0)
    vehicle_no=StringVar(mid, value=number)
    Ent1=Entry(mid,textvariable = vehicle_no ,font=('arial',20,'bold'))
    Ent1.grid(row=0,column=1)
    Ent2 = Entry(mid, font=('arial', 20, 'bold'))
    Ent2.grid(row=1, column=1)
    btn1=Button(mid,text="scan" ,command=search(Ent1,Ent2),font=('arial',20,'bold'))
    btn1.grid(row=0,column=2)
    txt2=Label(mid,font=('arial',20),text="Slot no : ")
    txt2.grid(row=1,column=0)
    # Ent2=Entry(mid,font=('arial',20,'bold'))
    # Ent2.grid(row=1,column=1)
    btn2=Button(mid,text="Book" ,command=inst(Ent1,Ent2),font=('arial',20,'bold'))
    btn2.grid(row=1,column=2)
    window.mainloop()
def getui(plate):
    print("i am here")
    gui(plate)
# getui("123")