import cv2,os
import numpy as np
import pyzbar.pyzbar as pyzbar
from tkinter import *
from datetime import datetime, date
window = Tk()
window.geometry("400x400+0+0")
window.title("Scan plate")

#os.add_dll_directory(r'C:\Users\Akansha joshi\Desktop\venv\lib\site-packages')


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

            print('Slot : ',y[0:1])
            print('In Date :',y[1:11])
            print('In Time :',y[11:19])
            print('Vehicle No :',y[19:])


            # print('In Time :',y[4:13])
            # print('')
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
