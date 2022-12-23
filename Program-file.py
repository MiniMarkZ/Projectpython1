from tkinter import *
import csv
import datetime

today = datetime.date.today()
day = today.day                    #เวลา

#------------คำสั่งปิด----------------------
def close_1():
    mywin.destroy()
    convert()

#-----หน้าใส่ชื่อ-------------------------------------------------------------------------------------------
def convert():

    # ------------หน้าเช็คชื่อ----------------------
    def chcek_name():  # ไว้เช็คชื่อ
        filepath = 'myfile1.txt'                                  #เปิดอ่าน data file
        try:
            with open(filepath, 'r', encoding='utf-8') as infile:        #เปิดอ่าน data file
                rd = csv.reader(infile)                                 #เปิดอ่าน data file
                mylist = list(rd)                                        #เปิดอ่าน data file
        except Exception as e:
            print(e)

        print(mylist)                       #เช็ค data file

        name = myname.get()                 #เรียกค่าชื่อใส่ไป

        def close_4():                      # ไว้กลับไปหน้าใส่ชื่อ
            root.destroy()                  #ปิดหน้า root
            filepath = 'myfile1.txt'
            listbox = mylist
            try:
                with open(filepath, 'w', encoding='utf-8')as outfile:
                    writer = csv.writer(outfile, lineterminator='\n')
                    writer.writerows(listbox)
            except Exception as e:
                print(e)

            print('end of file')
            convert()                       #เปิดหน้าใส่ชื่อ

        def caltime():                      #คำนวณเวลาเเล้วใส่ค่าคืนกลับ mylist
            try :
                sum = 0                         #ค่าเอาไว้เช็คเฉยๆว่าวนไปกี่ครั้ง
                number = eval(my_time.get())    #ดึงค่าเวลาที่ใส่ไป
                print(number)                   #เช็คชื่อ
                bl['text'] = 'ค่าที่ใส่ไป:', number  # ใส่ค่าตรงช่องล่าง
                for row2 in mylist:                     #for เพื่อหาชื่อใน data
                    calnum2 = str(calnum)
                    cal2 = calnum2 in str(row2[0])
                    if cal2 == True:
                        lsttest = []
                        print('ได้เเล้วครั้งที่ ', sum)
                        com_number = eval(row2[4]) + number
                        ot_bonus=int(((int(row2[3])/30)/8)*1.5)*com_number
                        print('ot_bonus',ot_bonus)
                        final_bonus= ot_bonus+eval(row2[6])
                        print('final_bonus',final_bonus)
                        print('com :', com_number)
                        lsttest.append(row2[0])
                        lsttest.append(row2[1])
                        lsttest.append(row2[2])
                        lsttest.append(row2[3])
                        lsttest.append(str(com_number))
                        lsttest.append(str(ot_bonus))
                        lsttest.append(str(final_bonus))
                        print(lsttest)
                        mylist.insert(calnum, lsttest)
                        mylist.pop(calnum + 1)
                        print('row4 :', row2[4])
                        print('row5 :', row2[5])
                        print('row6 :', row2[6])
                        print(mylist)
                        break
                    else:
                        print('ไม่ได้')
                        sum = sum + 1
            except Exception as e:
                bl['text'] = 'ระบุเป็นตัวเลขเท่านั้น'
                print(e)

        def Cumulative_time() : #ปุ่มกดเวลาสะสม
            sum = 0                #ค่าเอาไว้เช็คเฉยๆว่าวนไปกี่ครั้ง
            for row2 in mylist:    #for เพื่อหาข้อมูลใน data
                calnum2 = str(calnum)
                cal2 = calnum2 in str(row2[0])
                if cal2 == True:
                    print('ได้เเล้วครั้งที่ ', sum)
                    final_str = 'ชื่อ : {} \nเวลา OT สะสม : {} ชั่วโมง \nเงินโบนัส : {} บาท'.format(row2[1],row2[4],row2[5])
                    bl['text'] = final_str
                    break
                else:
                    print('ไม่ได้')
                    sum = sum + 1

        def chcek():  # หาว่ามีชื่อไหม
            for row in mylist:
                A = name in row[1]
                print(A)
                if A == True:
                    print('ได้')
                    return A
                    break

                else:
                    print('ไม่ได้')


        def chcek_num():  # หาว่าอยู่เลขที่เท่าไหร่
            B = 0
            for row in mylist:
                A = name in row[1]
                print(A)
                if A == True:
                    return B
                    break
                else:
                    print('ไม่ได้')
                    B = B + 1
                    print(B)

        cal = chcek()
        calnum = chcek_num()



        if cal == True:  # ถ้ามีชื่อ
            root30.destroy()
            root = Tk()
            root.minsize(800, 500)
            root.title('เมนู')
            my_time = StringVar()

            head = Label(root, text='ชื่อ', font=('Courier', 10))  # ชื่อขวาบน
            head.place(relx=0.8, rely=0.01, anchor='n')

            disname = Label(root, text=name, font=('Courier', 10))  # ชื่อขวาบน
            disname.place(relx=0.9, rely=0.01, anchor='n')

            head = Label(root, text='ระบุชั่วโมงการทํางาน OT', font=('Courier', 18))  # ตัวหนังสือ
            head.place(relx=0.3, rely=0.099, relwidth=0.75, relheight=0.1, anchor='n')

            frame = Frame(root, bg='#80c1ff', bd=5)  # สีตรงที่ใส่ข้อความ
            frame.place(relx=0.33, rely=0.2, relwidth=0.55, relheight=0.1, anchor='n')
            entry_number = Entry(frame, textvariable=my_time, font=('Courier', 15))  # ใส่เวลาใส่ช่องเล็ก
            entry_number.place(relwidth=1, relheight=1)

            button = Button(root, text='ตกลง',command=caltime, font=('Courier', 15))  # ปุ่มกดตกลง
            button.place(relx=0.65, rely=0.2, relwidth=0.3, relheight=0.1)

            bt = Button(root, text='เซฟและออกจากโปรแกรม',command=close_4,  width=20, font=('Courier', 15))  # ปุ่มกดออก
            bt.place(relx=0.65, rely=0.35, relwidth=0.3, relheight=0.1)

            btv = Button(root, text='เวลางานสะสม', width=20,command=Cumulative_time,font=('Courier', 15))  # ตั้งใจว่าจะเป็นปุ่มกดเเสดงเวลาที่ทำไปเเล้ว
            btv.place(relx=0.33, rely=0.35, relwidth=0.55, relheight=0.1, anchor='n')

            lower_frame = Frame(root, bg='#80c1ff', bd=5)  # ไว้แสดงข้อความ
            lower_frame.place(relx=0.5, rely=0.55, relwidth=0.9, relheight=0.4, anchor='n')  # ไว้แสดงข้อความ
            bl = Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left')  # ไว้แสดงข้อความ
            bl.place(relwidth=1, relheight=1)

            head = Label(root, text='เมนูการทำงาน', font=('Courier', 10))
            head.place(relx=0.13, rely=0.5, relwidth=0.1, relheight=0.05, anchor='n')

            root.mainloop()
        else:  # ถ้าไม่มีชื่อ
            nothave=Label(root30,text='*ไม่พบชื่อในระบบ*',fg='red', font=('Courier', 12))
            nothave.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.1, anchor='n')

    if day == 30:  # ถ้าวันที่ถึง 30
        def final_30():
            def close_5():
                root30.destroy()
                convert()

            try:
                filepath = 'myfile1.txt'                                # เปิดอ่าน data file
                with open(filepath, 'r', encoding='utf-8') as infile:   # เปิดอ่าน data file
                    rd = csv.reader(infile)                             # เปิดอ่าน data file
                    mylist = list(rd)                                   # เปิดอ่าน data file
            except Exception as e :
                print(e)

            sum = 0
            for row2 in mylist:             #for เพื่อหาชื่อใน data
                name30 = myname.get()
                name_30 = name30 in str(row2[1])
                if name_30 == True:
                    print('ได้เเล้วครั้งที่ ', sum)
                    final_str = 'ชื่อ : {} \nตําแหน่ง : {} \nเงินเดือน : {} บาท \nเวลา OT สะสม : {} ชั่วโมง \nเงินเดือนโบนัส : {} บาท' \
                                '\nสรุปเงินเดือน : {} บาท'.format(row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
                    label['text'] = final_str
                    button = Button(frame, text='กลับ', command=close_5, font=40)
                    button.place(relx=0.7, relwidth=0.3, relheight=1)
                    break
                else:
                    print('ไม่ได้')
                    sum = sum + 1

        root30 = Tk()
        root30.minsize(800, 500)
        root30.title('โปรเเกรมคำนวณโบนัส')
        myname = StringVar()  # ใส่ชื่อ


        head = Label(root30, text='ระบุชื่อ', font=('Courier', 18))
        head.place(relx=0.5, rely=0.025, relwidth=0.75, relheight=0.1, anchor='n')

        frame = Frame(root30, bg='#80c1ff', bd=5)
        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
        entry_name = Entry(frame, textvariable=myname, font=('Courier', 18))  # ใส่ชื่อ
        entry_name.place(relwidth=0.65, relheight=1)
        button = Button(frame, text='ตกลง',command=final_30, font=40)
        button.place(relx=0.7, relwidth=0.3, relheight=1)

        lower_frame = Frame(root30, bg='#ff2266', bd=5)  # ตารางข้อความที่เหลือ
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
        label = Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left')  # ไว้แสดงข้อความบน lower_frame
        label.place(relwidth=1, relheight=1)
        root30.mainloop()
    else:  # ถ้าวันไม่ใช่วันที่ 30
        root30 = Tk()
        root30.minsize(800, 500)
        root30.title('โปรเเกรมคำนวณโบนัส')
        myname = StringVar()  # ค่าชื่อ

        frame = Frame(root30, bg='#80c1ff', bd=5)
        frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')

        head = Label(root30, text='ระบุชื่อ', font=('Courier', 18))
        head.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        entry = Entry(frame, textvariable=myname, font=('Courier', 18))  # ใส่ชื่อ
        entry.place(relwidth=1, relheight=1)

        btOK = Button(root30, text='OK', fg='white',command=chcek_name, bg='#0060B9', width=20, )  # ไปที่ time0
        btOK.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.2)
        bt = Button(root30, text='Close', fg='white', bg='#F8002E', command=root30.destroy, width=20)
        bt.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.2)
        root30.mainloop()
#-----หน้าแรก--------------------------------------------------------------------------------------------


mywin = Tk()
mywin.minsize(800, 500)
mywin.title('โปรเเกรมคำนวณโบนัส')

head = Label(mywin, text='ขณะนี้วันที่', font=('Courier', 18))
head.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
time = Label(mywin, text=today, font=('Courier', 18), fg='green')
time.place(relx=0.5, rely=0.2, anchor='n')
deadday = Label(mywin, text='* ถ้าถึงวันที่ 30 จะสรุปผล *', font=('Courier', 12))
deadday.place(relx=0.5, rely=0.3, anchor='n')

btOK = Button(mywin, text='OK', fg='white', bg='#0060B9', width=20, command=close_1)
btOK.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.2)
bt = Button(mywin, text='Close', fg='white', bg='#F8002E', command=mywin.destroy, width=20)
bt.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.2)
mywin.mainloop()

