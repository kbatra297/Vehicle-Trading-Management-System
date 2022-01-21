from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("1400x800+0+0")
root.title("Vehicle Trading Management System")
root.configure(background="light green")

Tops = Frame(root, width=13500, height=100, bd=30, relief="raise",background="blue")
Tops.pack(side=TOP)

Name = Label(Tops, font=('calibre', 50), text="Vehicle Sales Trading Management System", bd=5, anchor='w',background="blue" )
Name.grid(row=0, column=0)

info = Frame(root, width=1352, height=500, bd=20, relief="sunken",background="green")
info.pack(side=TOP)

# Root is divided into two Info_left and receipt_right
# Info_left is divided into left_Top and left_Bottom
# left_Top is further divided into LeftTop_Left and LeftTop_Right
# left_Bottom is further divided into LeftBottom_Left and LeftBottom_Right
Info_Left = Frame(info, width=1000, height=650, bd=1, relief="raise", background="blue")
Info_Left.pack(side=LEFT)
# ========================================================================================================================#
Left_top = Frame(Info_Left, width=1000, height=300, relief="raise",bd=20,background="blue")
Left_top.pack(side=TOP)

LeftTop_Left = Frame(Left_top, width=500, height=400,relief="raise",background="blue" )
LeftTop_Left.pack(side=LEFT)

LeftTop_Right = Frame(Left_top, width=500, height=400, relief="raise")
LeftTop_Right.pack(side=RIGHT)
#**********************************************************************************************#

Left_Bottom = Frame(Info_Left, width=1000, height=300, bd=20, relief="raise",background="blue")
Left_Bottom.pack(side=BOTTOM)

LeftBottom_Left = Frame(Left_Bottom, width=500, height=300, relief="raise",background="blue")
LeftBottom_Left.pack(side=LEFT)

LeftBottom_Right = Frame(Left_Bottom, width=500, height=300, relief="raise",background="blue")
LeftBottom_Right.pack(side=RIGHT)

#**********************************************************************************************#

bottom_Right = Frame(info, width=352, height=650, bd=20, relief="raise",background="blue")
bottom_Right.pack(side=RIGHT)


# Exit Fn.*************************************************************************************#
def iExit():
    iExit = messagebox.askyesno("Vehicle Trading System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return


# Reset Fn.************************************************************************************#
def Reset():
    Modified.set('0')
    Stereo.set('0')
    AC.set('0')
    Leather_SeatCover.set('0')
    Android_Sterio.set('0')
    CostofCar.set("0")
    Car_Brand.set("0")
    CustomerName.set("")
    CustomerAddress.set("")
    CustomerPostcode.set("")
    CustomerTelephone.set("")
    VAT.set("")
    Discount.set("")
    Tax.set("")
    SubTotal.set("")
    Total.set("")
    txtReceipt.delete("1.0", END)

    modified_1_0.set(0)
    music_1_0.set(0)
    Seatcover_1_0.set(0)
    ac_1_0.set(0)
    androidste_1_0.set(0)
    var6.set(2)
    NameOf_Car.set(0)
    vat_y_n.set(0)
    discount_y_n.set(0)


# CarCost**************************************************************************************#
def CarCost():
    if (NameOf_Car.get() == 'Swift'):
        myCar = float(525600)
        CostofCar.set(myCar)
    elif (NameOf_Car.get() == 'City'):
        myCar = float(837800)
        CostofCar.set(myCar)
    elif (NameOf_Car.get() == 'Ecosport'):
        myCar = float(787900)
        CostofCar.set(myCar)
    elif (NameOf_Car.get() == 'jaguar '):
        myCar = float(655000)
        CostofCar.set(myCar)
    elif (NameOf_Car.get() == 'Micra'):
        myCar = float(437000)
        CostofCar.set(myCar)
    elif (NameOf_Car.get() == 'A4'):
        myCar = float(2790800)
        CostofCar.set(myCar)
    elif (NameOf_Car.get() == 'M5'):
        myCar = float(4570000)
        CostofCar.set(myCar)
    elif (NameOf_Car.get() == 'Land Rover Discovery'):
        myCar = float(7570000)
        CostofCar.set(myCar)

    # ****************Swift******************************
    if (mileage.get() == '100-500' and NameOf_Car.get() == 'Swift'):
        myCar = float(525000)
        iMile = 'Maruti Suzuki'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '501-2000' and NameOf_Car.get() == 'Swift'):
        myCar = float(520000)
        iMile = 'Maruti Suzuki'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '2001-10000' and NameOf_Car.get() == 'Swift'):
        myCar = float(515000)
        iMile = 'Maruti Suzuki'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '10001 or more' and NameOf_Car.get() == 'Swift'):
        myCar = float(510000)
        iMile = 'Maruti Suzuki'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    # *************************City*********************************
    if (mileage.get() == '100-500' and NameOf_Car.get() == 'City'):
        myCar = float(835000)
        iMile = 'Honda'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '501-2000' and NameOf_Car.get() == 'City'):
        myCar = float(810000)
        iMile = 'Honda'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '2001-10000' and NameOf_Car.get() == 'City'):
        myCar = float(740000)
        iMile = 'Honda'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '10001 or more' and NameOf_Car.get() == 'City'):
        myCar = float(650000)
        iMile = 'Honda'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    # **************************Ecosport********************************
    if (mileage.get() == '100-500' and NameOf_Car.get() == 'Ecosport'):
        myCar = float(835000)
        iMile = 'Ford'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '501-2000' and NameOf_Car.get() == 'Ecosport'):
        myCar = float(810000)
        iMile = 'Ford'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '2001-10000' and NameOf_Car.get() == 'Ecosport'):
        myCar = float(740000)
        iMile = 'Ford'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '10001 or more' and NameOf_Car.get() == 'Ecosport'):
        myCar = float(650000)
        iMile = 'Ford'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    # ******************************jaguar ****************************
    if (mileage.get() == '100-500' and NameOf_Car.get() == 'jaguar '):
        myCar = float(425000)
        iMile = 'Tata'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '501-2000' and NameOf_Car.get() == 'jaguar '):
        myCar = float(400000)
        iMile = 'Tata'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '2001-10000' and NameOf_Car.get() == 'jaguar '):
        myCar = float(380000)
        iMile = 'Tata'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '10001 or more' and NameOf_Car.get() == 'jaguar '):
        myCar = float(310000)
        iMile = 'Tata'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    # *********************************Micra*************************
    if (mileage.get() == '100-500' and NameOf_Car.get() == 'Micra'):
        myCar = float(230000)
        iMile = 'Nissan'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '501-2000' and NameOf_Car.get() == 'Micra'):
        myCar = float(210000)
        iMile = 'Nissan'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '2001-10000' and NameOf_Car.get() == 'Micra'):
        myCar = float(170000)
        iMile = 'Nissan'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '10001 or more' and NameOf_Car.get() == 'Micra'):
        myCar = float(140000)
        iMile = 'Nissan'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    #*******************************A4*********************************
    if (mileage.get() == '100-500' and NameOf_Car.get() == 'A4'):
        myCar = float(2700000)
        iMile = 'Nissan'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '501-2000' and NameOf_Car.get() == 'A4'):
        myCar = float(2690000)
        iMile = 'A4'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '2001-10000' and NameOf_Car.get() == 'A4'):
        myCar = float(2600000)
        iMile = 'A4'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '10001 or more' and NameOf_Car.get() == 'A4'):
        myCar = float(2520000)
        iMile = 'A4'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    #************************M5***********************************
    if (mileage.get() == '100-500' and NameOf_Car.get() == 'M5'):
        myCar = float(4400000)
        iMile = 'BMW'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '501-2000' and NameOf_Car.get() == 'M5'):
        myCar = float(4390000)
        iMile = 'BMW'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '2001-10000' and NameOf_Car.get() == 'M5'):
        myCar = float(4300000)
        iMile = 'BMW'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '10001 or more' and NameOf_Car.get() == 'M5'):
        myCar = float(4220000)
        iMile = 'BMW'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)
    # ************************land rover***********************************
    if (mileage.get() == '100-500' and NameOf_Car.get() == 'Land Rover Discovery'):
        myCar = float(4900000)
        iMile = 'Land Rover'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '501-2000' and NameOf_Car.get() == 'Land Rover Discovery'):
        myCar = float(4150000)
        iMile = 'Land Rover'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '2001-10000' and NameOf_Car.get() == 'Land Rover Discovery'):
        myCar = float(4100000)
        iMile = 'Land Rover'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    if (mileage.get() == '10001 or more' and NameOf_Car.get() == 'Land Rover Discovery'):
        myCar = float(3920000)
        iMile = 'Land Rover'
        CostofCar.set(myCar)
        Car_Brand.set(iMile)

    #********************************************************************#
    if (modified_1_0.get() == 1):
        Modified.set(22000)
    elif (modified_1_0.get() == 0):
        Modified.set(0)
    if (music_1_0.get() == 1):
        Stereo.set(8570)
    elif (music_1_0.get() == 0):
        Stereo.set(0)
    if (Seatcover_1_0.get() == 1):
        Leather_SeatCover.set(9500)
    elif (Seatcover_1_0.get() == 0):
        Leather_SeatCover.set(0)
    if (ac_1_0.get() == 1):
        AC.set(18755)
    elif (ac_1_0.get() == 0):
        AC.set(0)
    if (androidste_1_0.get() == 1):
        Android_Sterio.set(19550)
    elif (androidste_1_0.get() == 0):
        Android_Sterio.set(0)
    if (vat_y_n.get() == 1):
        VAT.set("Yes")
    elif (vat_y_n.get() == 0):
        VAT.set("No")
    if (discount_y_n.get() == 1):
        Discount.set("Yes")
    elif (discount_y_n.get() == 0):
        Discount.set("No")

    Item1 = float(CostofCar.get())
    Item2 = (Car_Brand.get())
    Item3 = float(Modified.get())
    Item4 = float(Stereo.get())
    Item5 = float(Leather_SeatCover.get())
    Item6 = float(AC.get())
    Item7 = float(Android_Sterio.get())
    Item8 = "Rs.", str('%.2f' % ((Item1) + Item3 + Item4 + Item5 + Item6 + Item7))
    Item9 = (((Item1) + Item3 + Item4 + Item5 + Item6 + Item7) * 0.45) / 100
    Item9 = "Rs.", str('%.2f' % (Item9))
    Item10 = (((Item1) + Item3 + Item4 + Item5 + Item6 + Item7) * 0.45) / 100
    Item11 = ((Item1) + Item3 + Item4 + Item5 + Item6 + Item7)
    Item12 = "Rs.", str('%.2f' % (Item10 + Item11))
    SubTotal.set(Item8)
    Tax.set(Item9)
    Total.set(Item12)


#Receipt Fn.*********************************************************************#
def Receipt():
    txtReceipt.delete("1.0", END)
    txtReceipt.insert(END, 'Items\t\t\t\t' + "Cost of Items \n\n")
    txtReceipt.insert(END, '========================================' "\n")
    txtReceipt.insert(END, 'Customer Name: \t\t\t\t' + CustomerName.get() + "\n")
    txtReceipt.insert(END, '========================================'"\n")
    txtReceipt.insert(END, 'Type of Car: \t\t\t\t' + NameOf_Car.get() + "\n")
    txtReceipt.insert(END, 'Cost of Car: \t\t\t\t' + CostofCar.get() + "\n")
    txtReceipt.insert(END, 'Total Mileage: \t\t\t\t' + mileage.get() + "\n")
    txtReceipt.insert(END, 'Trade in value: \t\t\t\t' + Car_Brand.get() + "\n")
    txtReceipt.insert(END, 'Cost of Modified: \t\t\t\t' + Modified.get() + "\n")
    txtReceipt.insert(END, 'Cost of Stereo: \t\t\t\t' + Stereo.get() + "\n")
    txtReceipt.insert(END, 'Cost of Leather_SeatCover: \t\t\t\t' + Leather_SeatCover.get() + "\n")
    txtReceipt.insert(END, 'Cost to AC: \t\t\t\t' + AC.get() + "\n")
    txtReceipt.insert(END, 'Cost of Android Sterio: \t\t\t\t' + Android_Sterio.get() + "\n")
    txtReceipt.insert(END, '========================================'"\n")
    txtReceipt.insert(END, 'Tax: \t\t\t\t' + Tax.get() + "\n")
    txtReceipt.insert(END, 'SubTotal: \t\t\t\t' + SubTotal.get() + "\n")
    txtReceipt.insert(END, 'Total Cost: \t\t\t\t' + Total.get() + "\n")
    txtReceipt.insert(END, '========================================'"\n")
    save()
#DatabaseSql Fnc.*******************************************************************************
def save():
    t1 = CustomerName.get()
    t2 = CustomerAddress.get()
    t3 = CustomerPostcode.get()
    t4 = CustomerTelephone.get()
    t5 = NameOf_Car.get()
    t6= CostofCar.get()
    t7= Car_Brand.get()
    t8= Modified.get()
    t9=Stereo.get()
    t10=AC.get()
    t11=Leather_SeatCover.get()
    t12=Android_Sterio.get()
    t13=VAT.get()
    t14=Discount.get()
    t15=Tax.get()
    t16=SubTotal.get()
    t17=Total.get()
    import pymysql
    db =pymysql.connect(host='localhost',user='root',password='root')
    cur = db.cursor()
    cur.execute('create database if not exists Vehicle_Trading_System')
    cur.execute("""use Vehicle_Trading_System""")
    cur.execute('''Create table if not exists vehicle_Trading_System(CustomerName varchar(255),CustomerAddress varchar(255)
    ,CustomerPostcode varchar(255) ,CustomerTelephone varchar(255),Nameof_car varchar(255)
    ,CostofCar varchar(255),Car_Brand varchar(255),Modified varchar(255),Sterio varchar(255),AC varchar(255)
    ,Leather_Seatcover varchar(255),Android_Sterio varchar(255), VAT varchar(255),Discount varchar(255)
    ,Tax varchar(255),SubTotal varchar(255),Total varchar(255) )''')
    cur.execute('insert into vehicle_Trading_System(CustomerName , CustomerAddress , CustomerPostcode , CustomerTelephone,NameOf_Car  '
                ', CostofCar , Car_Brand, Modified, Sterio, AC, Leather_SeatCover,Android_Sterio,VAT,Discount,Tax,SubTotal,Total) '
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (t1, t2 ,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17))
    db.commit()
    db.close()
    msg()


#************
def msg():
    messagebox.showinfo("Sucess","Data Is save In System")
# Frame 1****************************************************************************#
# Variables

CustomerName = StringVar()
CustomerAddress = StringVar()
CustomerPostcode = StringVar()
CustomerTelephone = StringVar()
#*************************************************************************************
lblName = Label(LeftTop_Left, font=('calibre', 16, 'bold'), text="Name:", fg="black", width=15, bd=10, anchor='w',background="blue")
lblName.grid(row=0, column=0)
txtName = Entry(LeftTop_Left, font=('calibre', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                textvariable=CustomerName)
txtName.grid(row=0, column=1)

lblAddress = Label(LeftTop_Left, font=('calibre', 16, 'bold'), text="Address:", fg="black", width=15, bd=10, anchor='w',background="blue")
lblAddress.grid(row=1, column=0)
txtAddress = Entry(LeftTop_Left, font=('calibre', 16, 'bold'), bd=2, width=24, bg="white", justify='left',textvariable=CustomerAddress)
txtAddress.grid(row=1, column=1)

lblPostcode = Label(LeftTop_Left, font=('calibre', 16, 'bold'), text="Pincode:", fg="black", width=15, bd=10,anchor='w',background="blue")
lblPostcode.grid(row=2, column=0)
txtPostcode = Entry(LeftTop_Left, font=('calibre', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                    textvariable=CustomerPostcode)
txtPostcode.grid(row=2, column=1)

lblTelephone = Label(LeftTop_Left, font=('calibre', 16, 'bold'), text="Mobile:", fg="black", width=15, bd=10,
                     anchor='w',background="blue")
lblTelephone.grid(row=3, column=0)
txtTelephone = Entry(LeftTop_Left, font=('calibre', 16, 'bold'), bd=2, width=24, bg="white", justify='left',
                     textvariable=CustomerTelephone)
txtTelephone.grid(row=3, column=1)
# Frame 3********************************************************************************************
# Variables
Modified = StringVar()
Stereo = StringVar()
AC = StringVar()
Leather_SeatCover = StringVar()
Android_Sterio = StringVar()
#******************************

Modified.set('0')
Stereo.set('0')
AC.set('0')
Leather_SeatCover.set('0')
Android_Sterio.set('0')

modified_1_0 = IntVar()
music_1_0 = IntVar()
Seatcover_1_0 = IntVar()
ac_1_0 = IntVar()
androidste_1_0 = IntVar()

lblModified = Checkbutton(LeftBottom_Left, font=('calibre', 16, 'bold'), text="Modified", fg="black", width=20, bd=10,
                          anchor='w',onvalue=1, offvalue=0, variable=modified_1_0,background="blue")
lblModified.grid(row=0, column=0)
txtModified = Entry(LeftBottom_Left, font=('calibre', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                    textvariable=Modified)
txtModified.grid(row=0, column=1)

lblStereo = Checkbutton(LeftBottom_Left, font=('calibre', 16, 'bold'), text="Music System", fg="black", width=20, bd=10,
                        anchor='w',onvalue=1, offvalue=0, variable=music_1_0,background="blue")
lblStereo.grid(row=1, column=0)
txtStereo = Entry(LeftBottom_Left, font=('calibre', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                  textvariable=Stereo)
txtStereo.grid(row=1, column=1)

lblLeather_SeatCover = Checkbutton(LeftBottom_Left, font=('calibre', 16, 'bold'), text="Leather_SeatCover Interior", fg="black", width=20,
                         bd=10, anchor='w',onvalue=1, offvalue=0, variable=Seatcover_1_0,background="blue")
lblLeather_SeatCover.grid(row=2, column=0)
txtLeather_SeatCover = Entry(LeftBottom_Left, font=('calibre', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                   textvariable=Leather_SeatCover)
txtLeather_SeatCover.grid(row=2, column=1)

ac = Checkbutton(LeftBottom_Left, font=('calibre', 16, 'bold'), text="AC", fg="black", width=20,
                            bd=10, anchor='w',onvalue=1, offvalue=0, variable=ac_1_0,background="blue")
ac.grid(row=3, column=0)
txtAC = Entry(LeftBottom_Left, font=('calibre', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
                      textvariable=AC)
txtAC.grid(row=3, column=1)

android_sterio = Checkbutton(LeftBottom_Left, font=('calibre', 16, 'bold'), text="Android Sterio", fg="black", width=20, bd=10,
                     anchor='w',onvalue=1, offvalue=0, variable=androidste_1_0,background="blue")
android_sterio.grid(row=4, column=0)
txtAndroid_Sterio = Entry(LeftBottom_Left, font=('calibre', 16, 'bold'), bd=2, width=14, bg="white", justify='left',
               textvariable=Android_Sterio)
txtAndroid_Sterio.grid(row=4, column=1)

btnTotalCost = Button(LeftBottom_Left, pady=8, bd=2, fg="black", font=('calibre', 16, 'bold'), width=13, text="Total",
                      bg="white", command=CarCost).grid(row=5, column=0)
btnTotalReceipt = Button(LeftBottom_Left, pady=8, bd=2, fg="black", font=('calibre', 16, 'bold'), width=13,
                         text="Receipt", bg="white", command=Receipt).grid(row=5, column=1)

# Frame 2***************************************************************************************
var6 = IntVar()
NameOf_Car = StringVar()
mileage = StringVar()

CostofCar = StringVar()
Car_Brand = StringVar()

CostofCar.set("0")
Car_Brand.set("0")

lblChooseCar = Label(LeftTop_Right, font=('calibre', 16, 'bold'), text="Choose a Car", fg="black", width=13, bd=14,
                     anchor='w',background="blue")
lblChooseCar.grid(row=0, column=0)
choChooseCar = ttk.Combobox(LeftTop_Right, textvariable=NameOf_Car, state='readonly', font=('calibre', 20, 'bold'), width=12,background="blue")
choChooseCar['value'] = ['', 'Swift', 'City', 'Ecosport', 'jaguar ', 'Micra', 'A4', 'M5','Land Rover Discovery']
choChooseCar.current(0)
choChooseCar.grid(row=1, column=0)

lblCostofCar = Label(LeftTop_Right, font=('calibre', 16, 'bold'), text="Cost of Car", fg="black", width=13, bd=14,
                     anchor='w',background="blue")
lblCostofCar.grid(row=2, column=0)
txtCostofCar = Entry(LeftTop_Right, font=('calibre', 16, 'bold'), bd=2, width=16, bg="white", justify='left',
                     textvariable=CostofCar)
txtCostofCar.grid(row=3, column=0)

lblMileage = Label(LeftTop_Right, font=('calibre', 16, 'bold'), text="Preferred Mileage Range", fg="black", width=13,
                       bd=14, anchor='w',background="blue")
lblMileage.grid(row=0, column=1)
choMileage = ttk.Combobox(LeftTop_Right, textvariable=mileage, state='readonly', font=('calibre', 20, 'bold'),
                              width=12,background="blue")
choMileage['value'] = ['', '100-500', '501-2000', '2001-10000', '10001 or more']
choMileage.current(0)
choMileage.grid(row=1, column=1)

lblCarBrand = Label(LeftTop_Right, font=('calibre', 16, 'bold'), text="Brand Name", fg="black", width=13, bd=14,
                      anchor='w',background="blue")
lblCarBrand.grid(row=2, column=1)
txtCarBrand = Entry(LeftTop_Right, font=('calibre', 16, 'bold'), bd=2, width=16, bg="white", justify='left',
                      textvariable=Car_Brand)
txtCarBrand.grid(row=3, column=1)

#Frame 4************************************************************************************************
VAT = StringVar()
Discount = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()

vat_y_n = IntVar()
discount_y_n = IntVar()

lblVAT = Checkbutton(LeftBottom_Right, font=('calibre', 16, 'bold'), text="VAT", fg="black", width=13, bd=12, anchor='w',
                     onvalue=1, offvalue=0, variable=vat_y_n,background="blue")
lblVAT.grid(row=0, column=0)
txtVAT = Entry(LeftBottom_Right, font=('calibre', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
               textvariable=VAT)
txtVAT.grid(row=0, column=1)

lblDiscount = Checkbutton(LeftBottom_Right, font=('calibre', 16, 'bold'), text="Discount", fg="black", width=13, bd=12,
                          anchor='w', onvalue=1, offvalue=0, variable=discount_y_n,background="blue")
lblDiscount.grid(row=1, column=0)
txtDiscount = Entry(LeftBottom_Right, font=('calibre', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
                    textvariable=Discount)
txtDiscount.grid(row=1, column=1)

lblTax = Label(LeftBottom_Right, font=('calibre', 16, 'bold'), text="Tax", fg="black", width=13, bd=12, anchor='w',background="blue")
lblTax.grid(row=2, column=0)
txtTax = Entry(LeftBottom_Right, font=('calibre', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
               textvariable=Tax)
txtTax.grid(row=2, column=1)

lblSubTotal = Label(LeftBottom_Right, font=('calibre', 16, 'bold'), text="Sub Total", fg="black", width=13, bd=12,
                    anchor='w',background="blue")
lblSubTotal.grid(row=3, column=0)
txtSubTotal = Entry(LeftBottom_Right, font=('calibre', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
                    textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1)

lblTotal = Label(LeftBottom_Right, font=('calibre', 16, 'bold'), text="Total", fg="black", width=13, bd=12, anchor='w',background="blue")
lblTotal.grid(row=4, column=0)
txtTotal = Entry(LeftBottom_Right, font=('calibre', 16, 'bold'), bd=2, width=17, bg="white", justify='left',
                 textvariable=Total)
txtTotal.grid(row=4, column=1)

btnReset = Button(LeftBottom_Right, pady=8, bd=2, fg="black", font=('calibre', 16, 'bold'), width=13, text="Reset",
                  bg="white", command=Reset).grid(row=6, column=0)
btnExit = Button(LeftBottom_Right, pady=8, bd=2, fg="black", font=('calibre', 16, 'bold'), width=13, text="Exit",
                 bg="white", command=exit).grid(row=6, column=1)

#Frame 5***************************************************************************************************
lblReceipt = Label(bottom_Right, font=('calibre', 16, 'bold'), text="Receipt:", bd=2, anchor='w',background="blue")
lblReceipt.grid(row=0, column=0)
txtReceipt = Text(bottom_Right, font=('calibre', 11, 'bold'), bd=8, width=46, height=40, bg="white")
txtReceipt.grid(row=1, column=0)

root.mainloop()
