import pymysql
# import qrcode
# qr=qrcode.make(5)
# print("inside finally")
# qr.save('myqr.png')
# from PIL import Image
# img = Image.open('myqr.png')
# img.show()
print("i am here")
con=pymysql.connect(user='root',password='',host='localhost',database='parking_db')
cur=con.cursor()
print(con)
