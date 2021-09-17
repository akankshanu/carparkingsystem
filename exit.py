import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from tkinter import *
from datetime import datetime, date
import pymysql
window = Tk()
window.geometry("400x400+0+0")
window.title("Scan plate")



def scan():
    cap = cv2.VideoCapture(0)
    x = True
    while x:
        ret, frame = cap.read()
        decodedobj = pyzbar.decode(frame)
        string = decodedobj
        # print(string)
        for obj in decodedobj:
            # print(obj.data)
            y=obj.data
            y =y.decode()

            print('Vehicle No :', y[19:])
            print('Slot : ',y[0:1])
            print('In Date :',y[1:11])
            print('In Time :',y[11:19])
            print('exit time :', datetime.now().time())
            now = datetime.now().time()
            now.strftime("%H:%M:%S")

            str = y[11:19]
            time_object = datetime.strptime(str, '%H:%M:%S').time()

            duration = datetime.combine(date.min, now) - datetime.combine(date.min, time_object)
            print("How long did the Car parked in parking area",duration)
            seconds = duration.seconds
            hours = seconds / 3600


            print("you have to pay rupee :- ",int(hours)*5)

            s = y[0:1]

            con = pymysql.connect(user='root', password='', host='localhost', database='parking_db')
            cur = con.cursor()

            sql = "update slots set status=%s where id=%s"
            val=('0',s)
            cur.execute(sql,val)
            con.commit()
            # print('In Time :',y[4:13])
            # print('')
            print("Good Bye .....Visit Again")
            x = False
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            # cv2.destroyAllWindows()
            break

    # cv2.release()
    cv2.destroyAllWindows()



btn1=Button(window,text="scan",command=scan,font=('arial',20))
btn1.grid()


window.mainloop()







# img = cv2.imread("myqr.png")
#
# decodedData = pyzbar.decode(img)
#
# for i in decodedData:
#     print("data:", i.data)
#
#
#
# cv2.imshow("Image", img)
# cv2.waitKey(0)
#
#
