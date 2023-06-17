import tkinter as tk
from PIL import Image,ImageTk
import tkinter.font as font

window=tk.Tk()
window.geometry("800x550")
window.resizable(False,False)
# define font
myFont = font.Font(size=20)
mainframe=tk.Frame(window,bg='Red')
mainframe.pack(padx=5,pady=5,fill='y',expand=True)

#Left frame
frame_1=tk.Frame(mainframe,bg='Blue')
frame_1.grid(row=0,column=0,padx=5,pady=5)
inputtxt = tk.Text(frame_1, height = 30, width = 25,   bg = "light blue")
inputtxt.pack(side=tk.TOP,padx=5,pady=5)

#Middle frame
frame_2=tk.Frame(mainframe,bg='Blue')
frame_2.grid(row=0,column=1,padx=5,pady=5,)
#Top at middle
frame_a=tk.Frame(frame_2)
frame_a.pack(side=tk.TOP)
frame_left=tk.Frame(frame_a,)
frame_left.pack(side=tk.LEFT)
frame_left_up=tk.Frame(frame_left,)
frame_left_up.pack(side=tk.TOP)
frame_left_down=tk.Frame(frame_left,)
frame_left_down.pack(side=tk.BOTTOM)
weight_label=tk.Label(frame_left_up,text="550 kg",width=5,height=2,bg='green')
weight_label.pack(side=tk.LEFT,padx=5,pady=5,fill='both')
count_label=tk.Label(frame_left_up,text="6",width=5,height=2,bg='green')
count_label.pack(side=tk.RIGHT,padx=5,pady=5,fill='both')
floor_label=tk.Label(frame_left_down,text="2",width=3,height=1,bg='green',fg='Yellow',font="Helvetica 50")
floor_label.pack(side=tk.BOTTOM,padx=5,pady=5)
frame_right=tk.Frame(frame_a,)
frame_right.pack(side=tk.RIGHT)
up_arrow_img=Image.open('RedUparrow.png')
up_arrow_img=up_arrow_img.resize((70,70))
up_arrow_img=ImageTk.PhotoImage(up_arrow_img)
down_arrow_img=Image.open('RedDownarrow.png')
down_arrow_img=down_arrow_img.resize((70,70))
down_arrow_img=ImageTk.PhotoImage(down_arrow_img)
arrow_label=tk.Label(frame_right,height=135,width=85,bg='yellow',image=up_arrow_img)
arrow_label.pack(fill='both',padx=5,pady=5)
#bottom at middle
frame_b=tk.Frame(frame_2)
frame_b.pack(side=tk.TOP,pady=20)
b1 = tk.Button(frame_b, text="3",height=3,width=8)
#b1['font'] = myFont
# Displaying the button b1
b1.grid(row=0, column=0,padx=5,pady=5)
b2 = tk.Button(frame_b, text="4",height=3,width=8)
#b2['font'] = myFont
b2.grid(row=0, column=1,padx=5,pady=5)
b3 = tk.Button(frame_b, text="F",height=3,width=8)
#b3['font'] = myFont
b3.grid(row=0, column=2,padx=5,pady=5)
b4 = tk.Button(frame_b, text="1",height=3,width=8)
#b4['font'] = myFont
b4.grid(row=1, column=0,padx=5,pady=5)
b5 = tk.Button(frame_b, text="2",height=3,width=8)
#b5['font'] = myFont
b5.grid(row=1, column=1,padx=5,pady=5)
b6 = tk.Button(frame_b, text="!",height=3,width=8)
#b6['font'] = myFont
b6.grid(row=1, column=2,padx=5,pady=5)
b7 = tk.Button(frame_b, text="G",height=3,width=8)
#b7['font'] = myFont
b7.grid(row=2, column=1,padx=5,pady=5)


#Right frame
frame_3=tk.Frame(mainframe,bg='green')
frame_3.grid(row=0,column=2,padx=5,pady=5,)

frame=tk.Frame(frame_3,bg="red")
frame.pack(side=tk.TOP,padx=5,pady=15)

#displaylabel
display_lbl=tk.Label(frame,text="r",font=("Calibri 12 bold"),bg="white",fg="black",width=4,height=3)
display_lbl.pack(side=tk.LEFT)
up_arrow_img=Image.open("RedUparrow.png")
up_arrow_img=up_arrow_img.resize((70,70))
up_arrow_img=ImageTk.PhotoImage(up_arrow_img)

arrow_label1=tk.Label(frame,bg='yellow',image=up_arrow_img)
arrow_label1.pack(side=tk.LEFT)

# down arrow image
down_arrow_img=Image.open("RedDownarrow.png")
down_arrow_img=down_arrow_img.resize((70,70))
down_arrow_img=ImageTk.PhotoImage(down_arrow_img)

arrow_label2=tk.Label(frame,bg='yellow',image=down_arrow_img)
arrow_label2.pack(side=tk.LEFT)

frame_d= tk.Frame(frame_3,bg='yellow')
frame_d.pack(side=tk.TOP,padx=5,pady=5)



frame1=tk.Frame(frame_d,bg='lightblue')
frame1.grid(row=0,column=0)
label11=tk.Label(frame1,text='1',font='Callibri 25 bold',bg='lightblue')
label11.pack(side=tk.LEFT)
image=Image.open("RedUparrow.png")
image11=image.resize((60,60))
image11=ImageTk.PhotoImage(image11) 
btn11=tk.Button(frame1,image=image11,bg='lightblue',bd=0,activebackground='black')
btn11.pack(side=tk.LEFT)
image=Image.open("RedDownarrow.png")
image12=image.resize((60,60))
image12=ImageTk.PhotoImage(image12)
btn12=tk.Button(frame1,image=image12,bg='lightblue',bd=0,activebackground='black')
btn12.pack(side=tk.LEFT)


frame2=tk.Frame(frame_d,bg='lightblue')
frame2.grid(row=0,column=1)
label21=tk.Label(frame2,text='2',font='Callibri 25 bold',bg='lightblue')
label21.pack(side=tk.LEFT)
image=Image.open("RedUparrow.png")
image21=image.resize((60,60))
image21=ImageTk.PhotoImage(image21) 
btn21=tk.Button(frame2,image=image21,bg='lightblue',bd=0,activebackground='black')
btn21.pack(side=tk.LEFT)
image=Image.open("RedDownarrow.png")
image22=image.resize((60,60))
image22=ImageTk.PhotoImage(image22)
btn22=tk.Button(frame2,image=image22,bg='lightblue',bd=0,activebackground='black')
btn22.pack(side=tk.LEFT)


frame3=tk.Frame(frame_d,bg='lightblue')
frame3.grid(row=1,column=0)
label31=tk.Label(frame3,text='3',font='Callibri 25 bold',bg='lightblue')
label31.pack(side=tk.LEFT)
image=Image.open("RedUparrow.png")
image31=image.resize((60,60))
image31=ImageTk.PhotoImage(image31) 
btn31=tk.Button(frame3,image=image31,bg='lightblue',bd=0,activebackground='black')
btn31.pack(side=tk.LEFT)
image=Image.open("RedDownarrow.png")
image32=image.resize((60,60))
image32=ImageTk.PhotoImage(image32)
btn32=tk.Button(frame3,image=image32,bg='lightblue',bd=0,activebackground='black')
btn32.pack(side=tk.LEFT)


frame4=tk.Frame(frame_d,bg='lightblue')
frame4.grid(row=1,column=1)
label41=tk.Label(frame4,text='4',font='Callibri 25 bold',bg='lightblue')
label41.pack(side=tk.LEFT)
image=Image.open("RedUparrow.png")
image41=image.resize((60,60))
image41=ImageTk.PhotoImage(image41) 
btn41=tk.Button(frame4,image=image41,bg='lightblue',bd=0,activebackground='black')
btn41.pack(side=tk.LEFT)
image=Image.open("RedDownarrow.png")
image42=image.resize((60,60))
image42=ImageTk.PhotoImage(image42)
btn42=tk.Button(frame4,image=image42,bg='lightblue',bd=0,activebackground='black')
btn42.pack(side=tk.LEFT)

frame5=tk.Frame(frame_d,bg='lightblue')
frame5.grid(row=2,column=0)
label51=tk.Label(frame5,text='G',font='Callibri 25 bold',bg='lightblue')
label51.pack(side=tk.LEFT)
image=Image.open("RedUparrow.png")
image51=image.resize((60,60))
image51=ImageTk.PhotoImage(image51) 
btn51=tk.Button(frame5,image=image51,bg='lightblue',bd=0,activebackground='black')
btn51.pack(side=tk.LEFT)
image=Image.open("RedDownarrow.png")
image52=image.resize((60,60))
image52=ImageTk.PhotoImage(image52)
btn52=tk.Button(frame5,image=image52,bg='lightblue',bd=0,activebackground='black')
btn52.pack(side=tk.LEFT)


window.mainloop()