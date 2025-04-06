from tkinter import *
from tkinter import messagebox,Canvas

root = Tk()

root.title('我的gui程序')

root.geometry('900x700+0+0')
# 500宽度  300高度   距屏幕左侧100像素 顶部200像素
canvas = Canvas(root, height=700, width=900)
oval = canvas.create_oval(300, 300, 30, 50)
oval = canvas.create_oval(700, 300, 430, 50)
oval = canvas.create_oval(300, 600, 30, 350)
oval = canvas.create_oval(700, 600, 430, 350)
oval = canvas.create_line(340, 30, 340, 650,fill='red')
oval = canvas.create_line(10, 320, 650, 320,fill='red')
#canvas.pack()
canvas.place(x=50,y=60)

bt = Button(root)
bt['text'] = '点击计算'
bt.pack()
D = DoubleVar()
L1 = DoubleVar()
L2 = DoubleVar()
Q = DoubleVar()
H = DoubleVar()
L = DoubleVar()
R = DoubleVar()

A1 = DoubleVar()
B1 = DoubleVar()
C1 = DoubleVar()
A2 = DoubleVar()
B2 = DoubleVar()
C2 = DoubleVar()
A3 = DoubleVar()
B3 = DoubleVar()
C3 = DoubleVar()
A4 = DoubleVar()
B4 = DoubleVar()
C4 = DoubleVar()
A13 = DoubleVar()
A24 = DoubleVar()
B13 = DoubleVar()
B24 = DoubleVar()
LA13 = StringVar()
LA24 = StringVar()
LB13 = StringVar()
LB24 = StringVar()
LA13.set("上下外圈")
LA24.set("左右外圈")
LB13.set("上下张口")
LB24.set("左右张口")

D_Label= Label(root,text="D",width=8,height=1,fg="black")
D_Label.place(x=50,y=30)
D_entry = Entry(root,textvariable=D,width=10)
D_entry.place(x=30,y=60)

L1_Label= Label(root,text="L1",width=8,height=1,fg="black")
L1_Label.place(x=150,y=30)
L1_entry = Entry(root,textvariable=L1,width=10)
L1_entry.place(x=130,y=60)

L2_Label= Label(root,text="L2",width=8,height=1,fg="black")
L2_Label.place(x=240,y=30)
L2_entry = Entry(root,textvariable=L2,width=10)
L2_entry.place(x=230,y=60)

Q_Label= Label(root,text="前地脚",width=8,height=1,fg="black")
Q_Label.place(x=350,y=30)
Q_entry = Label(root,textvariable=Q,width=10)
Q_entry.place(x=330,y=60)

H_Label= Label(root,text="后地脚",width=8,height=1,fg="black")
H_Label.place(x=450,y=30)
H_entry = Label(root,textvariable=H,width=10)
H_entry.place(x=430,y=60)

L_Label= Label(root,text="左移位",width=8,height=1,fg="black")
L_Label.place(x=550,y=30)
L_entry = Label(root,textvariable=L,width=10)
L_entry.place(x=530,y=60)

R_Label= Label(root,text="右移位",width=8,height=1,fg="black")
R_Label.place(x=650,y=30)
R_entry = Label(root,textvariable=R,width=10)
R_entry.place(x=630,y=60)

A1_Label= Label(root,text="A1",width=8,height=1,fg="black")
A1_Label.place(x=140,y=85)
A1_entry = Entry(root,textvariable=A1,width=10)
A1_entry.place(x=190,y=85)

B1_Label= Label(root,text="B1",width=8,height=1,fg="black")
B1_Label.place(x=90,y=200)
B1_entry = Entry(root,textvariable=B1,width=10)
B1_entry.place(x=90,y=220)

C1_Label= Label(root,text="C1",width=8,height=1,fg="black")
C1_Label.place(x=270,y=200)
C1_entry = Entry(root,textvariable=C1,width=10)
C1_entry.place(x=270,y=220)

B2_Label= Label(root,text="B2",width=8,height=1,fg="black")
B2_Label.place(x=540,y=135)
B2_entry = Entry(root,textvariable=B2,width=10)
B2_entry.place(x=590,y=135)

A2_Label= Label(root,text="A2",width=8,height=1,fg="black")
A2_Label.place(x=760,y=200)
A2_entry = Entry(root,textvariable=A2,width=10)
A2_entry.place(x=760,y=220)

C2_Label= Label(root,text="C2",width=8,height=1,fg="black")
C2_Label.place(x=540,y=315)
C2_entry = Entry(root,textvariable=C2,width=10)
C2_entry.place(x=590,y=315)

A3_Label= Label(root,text="A3",width=8,height=1,fg="black")
A3_Label.place(x=140,y=675)
A3_entry = Entry(root,textvariable=A3,width=10)
A3_entry.place(x=190,y=675)

B3_Label= Label(root,text="B3",width=8,height=1,fg="black")
B3_Label.place(x=270,y=500)
B3_entry = Entry(root,textvariable=B3,width=10)
B3_entry.place(x=270,y=520)

C3_Label= Label(root,text="C3",width=8,height=1,fg="black")
C3_Label.place(x=90,y=500)
C3_entry = Entry(root,textvariable=C3,width=10)
C3_entry.place(x=90,y=520)

C4_Label= Label(root,text="C4",width=8,height=1,fg="black")
C4_Label.place(x=540,y=435)
C4_entry = Entry(root,textvariable=C4,width=10)
C4_entry.place(x=590,y=435)

A4_Label= Label(root,text="A4",width=8,height=1,fg="black")
A4_Label.place(x=400,y=500)
A4_entry = Entry(root,textvariable=A4,width=10)
A4_entry.place(x=400,y=520)

B4_Label= Label(root,text="B4",width=8,height=1,fg="black")
B4_Label.place(x=540,y=615)
B4_entry = Entry(root,textvariable=B4,width=10)
B4_entry.place(x=590,y=615)

#A13_Label= Label(root,text="上下外圈：",width=8,height=1,fg="black")
A13_Label= Label(root,textvariable=LA13,width=8,height=1,fg="black")
A13_Label.place(x=750,y=340)
A13_value= Label(root,textvariable=A13,width=8,height=1,fg="black")
A13_value.place(x=810,y=340)
A24_Label= Label(root,textvariable=LA24,width=8,height=1,fg="black")
A24_Label.place(x=750,y=390)
A24_value= Label(root,textvariable=A24,width=8,height=1,fg="black")
A24_value.place(x=810,y=390)
B24_Label= Label(root,textvariable=LB24,width=8,height=1,fg="black")
B24_Label.place(x=750,y=440)
B24_value= Label(root,textvariable=B24,width=8,height=1,fg="black")
B24_value.place(x=810,y=440)
B13_Label= Label(root,textvariable=LB13,width=8,height=1,fg="black")
B13_Label.place(x=750,y=490)
B13_value= Label(root,textvariable=B13,width=8,height=1,fg="black")
B13_value.place(x=810,y=490)
def dianji(e):
    a13 = round((A1.get() -A3.get())/2,2);
    if(a13>0):
        LA13.set("上外圈");
    else:
        LA13.set("下外圈");
    A13.set(a13);

    a24 = round((A2.get() -A4.get())/2,2);
    if(a24>0):
        LA24.set("左外圈");
    else:
        LA24.set("右外圈");
    A24.set(a24);

    b24 = round((B2.get() +C4.get()-C2.get()-B4.get())/2,2);
    if(b24>0):
        LB24.set("上张口");
    else:
        LB24.set("下张口");
    B24.set(b24);

    b13 = round((B1.get() +C3.get()-C1.get()-B3.get())/2,2);
    if(b13>0):
        LB13.set("左张口");
    else:
        LB13.set("右张口");
    B13.set(b13);
    if(abs(b24)<0.05):
        bb24=0;
    else:
        bb24=b24;
    if(abs(b13)<0.05):
        bb13=0;
    else:
        bb13=b13;

    d=D.get();
    l1=L1.get();
    l2=L2.get();

    q = round(l1/d*bb24+a13,2);
    Q.set(q);

    h = round((l1+l2)/d*bb24+a13,2);
    H.set(h);

    l = round(l1/d*bb13+a24,2);
    L.set(l);

    r = round((l1+l2)/d*bb13+a24,2);
    R.set(r);

    
    #A24_value["text"]=(float(A2_entry.get())-float(A4_entry.get()))/2;

    #B24_value["text"]=(float(B2_entry.get())+float(C4_entry.get())-float(C2_entry.get())-float(B4_entry.get()))/2;

    #B13_value["text"]=(float(B1_entry.get())+float(C3_entry.get())-float(C1_entry.get())-float(B3_entry.get()))/2;
    


bt.bind('<Button-1>', dianji)  # 绑定点击事件
root.mainloop()  # 进入事件循环

