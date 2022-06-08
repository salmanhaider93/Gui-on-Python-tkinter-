from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image


root = Tk()
root.geometry("980x750")
root.iconbitmap('c:/Users/shaier/PycharmProjects/Swift_Gui/shearwater.ico')


# Create label
root.title('Swift Testing')
l = Label(root, text="Swift Pressure Testing", font='Helvetica 18 bold' ).place(x=5, y=0)

###swift Image
swift_image_open =  Image.open("Swift.png")
swift_image_resize =  swift_image_open.resize((200,170),Image.ANTIALIAS)
swift_image= ImageTk.PhotoImage(swift_image_resize)
my_label = Label(image=swift_image).place(x=700,y=0)

#def start():
#    mylabel_start =  Label(root, text = "testing in progress")
#    mylabel_start.pack()

#def stop():
#    mylabel_stop = Label(root, text="testing has stop")
#    mylabel_stop.pack()

# Star button
#photo = PhotoImage(file = 'C:/Users/shaier/PycharmProjects/Swift_Gui/startbutton.png')

# Resizing image to fit on button
#photoimage = photo.subsample(3, 3)

###### select duct that will be under test

DUT_select_frame = LabelFrame(root, text="SELECT DUT",font = 'Helvetica 10 bold',padx=7,pady=7)
DUT_select_frame.place(x=450, y=30)

DUT_Select_All = Checkbutton(DUT_select_frame, text = "SELECT ALL",onvalue=1,offvalue=0).grid(row= 0, column=0)

DUT1 = Checkbutton(DUT_select_frame, text = "DUT1",onvalue=1,offvalue=0).grid(row= 1, column=0)
DUT2 = Checkbutton(DUT_select_frame, text = "DUT2",onvalue=1,offvalue=0).grid(row= 2, column=0 )
DUT3 = Checkbutton(DUT_select_frame, text = "DUT3",onvalue=1,offvalue=0).grid(row= 3, column=0 )
DUT4 = Checkbutton(DUT_select_frame, text = "DUT4",onvalue=1,offvalue=0).grid(row= 1, column=1 )
DUT5= Checkbutton(DUT_select_frame, text = "DUT5",onvalue=1,offvalue=0).grid(row= 2, column=1 )
DUT6 = Checkbutton(DUT_select_frame, text = "DUT6",onvalue=1,offvalue=0).grid(row= 3, column=1 )



#startbutton = Button(root, image = photoimage).place(x=10, y=40)
Startbutton =  Button(root, text= "Start Testing", font = 'Helvetica 10 bold', bg = "green", padx=10, pady = 10).place(x=10, y=40)


#Stop button
stopbutton = Button(root, text = "Stop Testing", font = 'Helvetica 10 bold' , bg ="red", padx = 10, pady = 10).place(x=140, y=40)


# progressbar

Pd_lebel= Label(root, text="Testing Progress", font=13).place(x=0, y=100)

pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=350
)
pb.place(x=15, y=130)


#Units stauts

#unit 1
unit1 = Label(root, text="DUT 1", font=14).place(x=0, y=180)
pass_fail_unit1 = Label(root, text="Pass/Fail").place(x=0, y=210)

# sc_unit1 = Button(root, text = "Screening test", bg = "white", padx = 5, pady = 5).place(x=65, y=200)
# hp_unit1 = Button(root, text = "HP test", bg = "white",padx = 5, pady = 5).place(x=175, y=200)

# #Create a canvas object
# canvas= Canvas(root, width= 100, height= 20, bg = a)
# #Add a text in Canvas
# canvas.create_text(50, 10, text="HELLO WORLD", fill="black", font=('Helvetica 8 bold'))
# canvas.place(x=0,y=0)

sc_unit1= Canvas(root, width= 100, height= 25, bg = 'Green')
sc_unit1.create_text(50, 12, text="Screening test", fill="black", font=('Helvetica 8 bold'))
sc_unit1.place(x=65, y=205)


hp_unit1= Canvas(root, width= 100, height= 25, bg = 'Red')
hp_unit1.create_text(50, 12, text="HP test", fill="black", font=('Helvetica 8 bold'))
hp_unit1.place(x=175, y=205)



serial_number_unit1 =  Label(root, text="SN").place(x=0, y=240)
Serial_number_display_unit1 = Text(height = 1, width = 15).place(x=65, y=240)

PSI_number_unit1 =  Label(root, text="PSI").place(x=0, y=270)
PSI_number_display_unit1 = Text(height = 1, width = 15).place(x=65, y=270)

Status_message_unit1=  Label(root ,text="DUT 1 Testing Status").place(x=0, y=300)
Status_message_display_unit1 = Text(height = 2, width = 30).place(x=5, y=320)


#unit 2
unit2 = Label(root, text="DUT 2", font=14).place(x=0, y=380)
pass_fail_unit2 = Label(root, text="Pass/Fail").place(x=0, y=410)

sc_unit2 = Button(root, text = "Screening test", bg = "white",padx = 5, pady = 5).place(x=65, y=400)
hp_unit2 = Button(root, text = "HP test", bg = "white",padx = 5, pady = 5).place(x=175, y=400)

serial_number_unit2 =  Label(root, text="SN").place(x=0, y=440)
Serial_number_display_unit2 = Text(height = 1, width = 15).place(x=65, y=440)

PSI_number_unit2 =  Label(root, text="PSI").place(x=0, y=470)
PSI_number_display_unit1 = Text(height = 1, width = 15).place(x=65, y=470)

Status_message_unit2 =  Label(root, text="DUT 2 Testing Status").place(x=0, y=500)
Status_message_display_unit2 = Text(height = 2, width = 30).place(x=5, y=520)


#unit 3
unit3 = Label(root, text="DUT 3", font=14).place(x=350, y=180)
pass_fail_unit3 = Label(root, text="Pass/Fail").place(x=350, y=210)

sc_unit3 = Button(root, text = "Screening test", bg = "white",padx = 5, pady = 5).place(x=415, y=200)
hp_unit2 = Button(root, text = "HP test", bg = "white",padx = 5, pady = 5).place(x=525, y=200)

serial_number_unit3 =  Label(root, text="SN").place(x=350, y=240)
Serial_number_display_unit3 = Text(height = 1, width = 15).place(x=415, y=240)

PSI_number_unit3 =  Label(root, text="PSI").place(x=350, y=270)
PSI_number_display_unit3 = Text(height = 1, width = 15).place(x=415, y=270)

Status_message_unit3=  Label(root, text="DUT 3 Testing Status").place(x=350, y=300)
Status_message_display_unit3 = Text(height = 2, width = 30).place(x=355, y=320)

#unit 4
unit4 = Label(root, text="DUT 4", font=14).place(x=350, y=380)
pass_fail_unit4 = Label(root, text="Pass/Fail").place(x=350, y=410)

sc_unit4 = Button(root, text = "Screening test", bg = "white",padx = 5, pady = 5).place(x=415, y=400)
hp_unit4 = Button(root, text = "HP test", bg = "white",padx = 5, pady = 5).place(x=525, y=400)

serial_number_unit4 =  Label(root, text="SN").place(x=350, y=440)
Serial_number_display_unit4 = Text(height = 1, width = 15).place(x=415, y=440)

PSI_number_unit4 =  Label(root, text="PSI").place(x=350, y=470)
PSI_number_display_unit4 = Text(height = 1, width = 15).place(x=415, y=470)

Status_message_unit4 =  Label(root, text="DUT 4 Testing Status").place(x=350, y=500)
Status_message_display_unit4 = Text(height = 2, width = 30).place(x=355, y=520)

#unit 5
unit3 = Label(root, text="DUT 5", font=14).place(x=700, y=180)
pass_fail_unit5 = Label(root, text="Pass/Fail").place(x=700, y=210)

sc_unit5 = Button(root, text = "Screening test", bg = "white",padx = 5, pady = 5).place(x=765, y=200)
hp_unit5 = Button(root, text = "HP test", bg = "white",padx = 5, pady = 5).place(x=875, y=200)

serial_number_unit5 =  Label(root, text="SN").place(x=700, y=240)
Serial_number_display_unit5 = Text(height = 1, width = 15).place(x=765, y=240)

PSI_number_unit5 =  Label(root, text="PSI").place(x=700, y=270)
PSI_number_display_unit5 = Text(height = 1, width = 15).place(x=765, y=270)

Status_message_unit5=  Label(root, text="DUT 5 Testing Status").place(x=700, y=300)
Status_message_display_unit5 = Text(height = 2, width = 30).place(x=705, y=320)

#unit 6
unit4 = Label(root, text="DUT 6", font=14).place(x=700, y=380)
pass_fail_unit4 = Label(root, text="Pass/Fail").place(x=700, y=410)

sc_unit4 = Button(root, text = "Screening test", bg = "white",padx = 5, pady = 5).place(x=765, y=400)
hp_unit4 = Button(root, text = "HP test", bg = "white",padx = 5, pady = 5).place(x=875, y=400)

serial_number_unit4 =  Label(root, text="SN").place(x=700, y=440)
Serial_number_display_unit4 = Text(height = 1, width = 15).place(x=765, y=440)

PSI_number_unit4 =  Label(root, text="PSI").place(x=700, y=470)
PSI_number_display_unit4 = Text(height = 1, width = 15).place(x=765, y=470)

Status_message_unit4 =  Label(root, text="DUT 6 Testing Status").place(x=700, y=500)
Status_message_display_unit4 = Text(height = 2, width = 30).place(x=705, y=520)



####status mmessage
Status_lebel= Label(root, text="Test Status", font=13).place(x=0, y=580)
status_text = Text(height = 5, width = 70).place(x=5, y=610)


root.mainloop()
