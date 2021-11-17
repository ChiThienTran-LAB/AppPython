import tkinter
from typing_extensions import IntVar

def tinhtien(out_data_2:tkinter.DoubleVar,dientieuthu:tkinter.DoubleVar,thue10:tkinter.DoubleVar,tongcong:tkinter.DoubleVar,capbac1:tkinter.DoubleVar,capbac2:tkinter.DoubleVar,capbac3:tkinter.DoubleVar,capbac4:tkinter.DoubleVar,capbac5:tkinter.DoubleVar,capbac6:tkinter.DoubleVar):
    dien_tieu_thu = float(dientieuthu.get())
    muc1 = 50
    muc2 = 50
    muc3 = 100
    muc4 = 100
    muc5 = 100
    
    dongia1 = 1678
    dongia2 = 1734
    dongia3 = 2014
    dongia4 = 2536
    dongia5 = 2834
    dongia6 = 2927
       
    if dien_tieu_thu >0 and dien_tieu_thu <=50:
        done = dongia1 * dien_tieu_thu
        thue = done *0.1
        thue10.set(thue)
        out_data_2.set(done)
        sum = done + thue
        tongcong.set(sum)
        capbac1.set(dien_tieu_thu)
        capbac2.set(0)
        capbac3.set(0)
        capbac4.set(0)
        capbac5.set(0)
        capbac6.set(0)
    elif dien_tieu_thu>50 and dien_tieu_thu <=100:
        done = 50 * 1678 + (dien_tieu_thu-50) * dongia2
        thue = done *0.1
        thue10.set(thue)
        out_data_2.set(done)
        sum = done + thue
        tongcong.set(sum)
        capbac1.set(muc1)
        capbac2.set(dien_tieu_thu-muc1)
        capbac3.set(0)
        capbac4.set(0)
        capbac5.set(0)
        capbac6.set(0)
    elif dien_tieu_thu> 100 and dien_tieu_thu <=200:
        done = 50 * 1678 + 50 * 1734 + (dien_tieu_thu-100)*dongia3
        thue = done *0.1
        thue10.set(thue)
        out_data_2.set(done)
        sum = done + thue
        tongcong.set(sum)
        capbac1.set(muc1)
        capbac2.set(muc2)
        capbac3.set(dien_tieu_thu-(muc1+muc2))
        capbac4.set(0)
        capbac5.set(0)
        capbac6.set(0)
    elif dien_tieu_thu>200 and dien_tieu_thu <=300:
        done = 50 * 1678 + 50 * 1734 + 100 * 2014 + (dien_tieu_thu-200) *dongia4
        thue = done * 0.1
        thue10.set(thue)
        out_data_2.set(done)
        sum = done + thue
        tongcong.set(sum)
        capbac1.set(muc1)
        capbac2.set(muc2)
        capbac3.set(muc3)
        capbac4.set(dien_tieu_thu-(muc1+muc2+muc3))
        capbac5.set(0)
        capbac6.set(0)
    elif dien_tieu_thu>300 and dien_tieu_thu <=400:
        done = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (dien_tieu_thu-300) * dongia5
        thue = done *0.1
        thue10.set(thue)
        out_data_2.set(done)
        sum = done + thue
        tongcong.set(sum)
        capbac1.set(muc1)
        capbac2.set(muc2)
        capbac3.set(muc3)
        capbac4.set(muc4)
        capbac5.set(dien_tieu_thu-(muc1+muc2+muc3+muc4))
        capbac6.set(0)
    elif dien_tieu_thu > 400:
        done = 50*  1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (dien_tieu_thu -400) * dongia6
        thue = done *0.1
        thue10.set(thue)
        out_data_2.set(done)
        sum = done + thue
        tongcong.set(sum)
        capbac1.set(muc1)
        capbac2.set(muc2)
        capbac3.set(muc3)
        capbac4.set(muc4)
        capbac5.set(muc5)
        capbac6.set(dien_tieu_thu-(muc1+muc2+muc3+muc4+muc5))
    elif dien_tieu_thu <= 0:
        thue10.set(0)
        out_data_2.set(0)
        tongcong.set(0)
        capbac1.set(0)
        capbac2.set(0)
        capbac3.set(0)
        capbac4.set(0)
        capbac5.set(0)
        capbac6.set(0)
def reset(dientieuthu: tkinter.DoubleVar,out_data_2: tkinter.DoubleVar):
    dientieuthu.set("") 
    out_data_2.set("") 
    tongcong.set("")
    thue10.set("")
    capbac1.set(0)
    capbac2.set(0)
    capbac3.set(0)
    capbac4.set(0)
    capbac5.set(0)
    capbac6.set(0)

window = tkinter.Tk()
window.title('Chí Thiện Trần App')
window.geometry("690x450")

out_data_2 = tkinter.DoubleVar()
dientieuthu = tkinter.DoubleVar()
thue10 = tkinter.DoubleVar()
tongcong = tkinter.DoubleVar()

capbac1 = tkinter.DoubleVar()
capbac2 = tkinter.DoubleVar()
capbac3 = tkinter.DoubleVar()
capbac4 = tkinter.DoubleVar()
capbac5 = tkinter.DoubleVar()
capbac6 = tkinter.DoubleVar()

thue = tkinter.DoubleVar()

label_chinh = tkinter.Label(window,text='TÍNH TIỀN ĐIỆN SINH HOẠT', fg='red',font=('Arial',20)).grid(row=0,columnspan=4)

lable_nhap = tkinter.Label(window,text="---------------------NHẬP THÔNG SỐ---------------------",font=('Arial',20)).grid(row=1,columnspan=4)

label_3 = tkinter.Label(window, text="Điện tiêu thụ trong kì: ").grid(row=3)
entry_dien = tkinter.Entry(window,width=20,textvariable=dientieuthu,fg="red").grid(row=3,column=1)
label_3_1 = tkinter.Label(window,text="kWh").grid(row=3,column=2)

lable_thongtin = tkinter.Label(window,text="---------------------BẢNG THỐNG KÊ---------------------",font=('Arial',20)).grid(row=4,columnspan=4)

lb_bacthang = tkinter.Label(window,text="Bậc thang",bg="yellow").grid(row=5,column=0)
lb_sanluong = tkinter.Label(window,text="Sản lượng (kWh)",bg="yellow").grid(row=5,column=1)
lb_donggia = tkinter.Label(window,text="Đơn giá (từng bậc)",bg="yellow").grid(row=5,column=3)


lable_capbac_1 = tkinter.Label(window,text="Cấp bậc 1: ").grid(row=6,column=0)
lable_text_1 = tkinter.Label(window,textvariable=capbac1).grid(row=6,column=1)
dongia_1 = tkinter.Label(window,text=1678).grid(row=6,column=3)

lable_capbac_2 = tkinter.Label(window,text="Cấp bậc 2: ").grid(row=7,column=0)
lable_text_2 = tkinter.Label(window,textvariable=capbac2).grid(row=7,column=1)
dongia_2 = tkinter.Label(window,text=1734).grid(row=7,column=3)

lable_capbac_3 = tkinter.Label(window,text="Cấp bậc 3: ").grid(row=8,column=0)
lable_text_3 = tkinter.Label(window,textvariable=capbac3).grid(row=8,column=1)
dongia_3 = tkinter.Label(window,text=2014).grid(row=8,column=3)

lable_capbac_4 = tkinter.Label(window,text="Cấp bậc 4: ").grid(row=9,column=0)
lable_text_4 = tkinter.Label(window,textvariable=capbac4).grid(row=9,column=1)
dongia_4 = tkinter.Label(window,text=2536).grid(row=9,column=3)

lable_capbac_5 = tkinter.Label(window,text="Cấp bậc 5: ").grid(row=10,column=0)
lable_text_5 = tkinter.Label(window,textvariable=capbac5).grid(row=10,column=1)
dongia_5 = tkinter.Label(window,text=2834).grid(row=10,column=3)

lable_capbac_6 = tkinter.Label(window,text="Cấp bậc 6: ").grid(row=11,column=0)
lable_text_6 = tkinter.Label(window,textvariable=capbac6).grid(row=11,column=1)
dongia_6 = tkinter.Label(window,text=2927).grid(row=11,column=3)

label_ketqua = tkinter.Label(window,text="--------------------------KẾT QUẢ--------------------------",font=('Arial',20)).grid(row=12,columnspan=4)

label_4 = tkinter.Label(window, text="Tiền phải trả tạm tính: ").grid(row=13)
lb_tien = tkinter.Label(window,width=30,textvariable=out_data_2).grid(row=13,column=1)
label_3_1 = tkinter.Label(window,text="VNĐ").grid(row=13,column=2)

label_5 = tkinter.Label(window, text="Tiền thuế 10%: ").grid(row=14)
label_thue = tkinter.Label(window,width=30,textvariable=thue10).grid(row=14,column=1)
label_thue_tien = tkinter.Label(window,text="VNĐ").grid(row=14,column=2)

label_6 = tkinter.Label(window,text="Tổng tiền phải trả: ").grid(row=15)
label_thucte = tkinter.Label(window,width=30,textvariable=tongcong,font=(20)).grid(row=15,column=1)
label_thucte_tien = tkinter.Label(window,text="VNĐ").grid(row=15,column=2)

button_tinhtien = tkinter.Button(window,bg='red',fg='yellow',width=10,text="Tính tiền",command=lambda:tinhtien(out_data_2,dientieuthu,thue10,tongcong,capbac1,capbac2,capbac3,capbac4,capbac5,capbac6,)).grid(row=16,column=0)
button_reset = tkinter.Button(window,width=10,fg='white',bg='purple',text='Reset',command=lambda:reset(dientieuthu,out_data_2)).grid(row=16,column=1)
button_thoat = tkinter.Button(window,fg='black',bg='gray',width=10,command=lambda:window.destroy(),text='Thoát').grid(row=16,column=3)

lable_nguon = tkinter.Label(window,text="*ĐƠN GIÁ THEO QĐ 648/QĐ-BCT").grid(row=17,column=0)

window.mainloop()