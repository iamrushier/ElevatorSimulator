'from tkinter import *
from PIL import Image,ImageTk
window=Tk()
window.config(bg='blue')
window.geometry('960x750')

#Elevator 1
door_closed_1=True
direction_1=None
up_queue_1=list()
down_queue_1=list()
cart_position_1=0
color_1='yellow' 
delay_1=5000

#Elevator 2
door_closed_2=True
direction_2=None
up_queue_2=list()
down_queue_2=list()
cart_position_2=0
color_2='yellow' 
delay_2=5000

def update_position_1():
    global cart_position_1,direction_1,color_1,up_queue_1,down_queue_1
    for x in range(5):
        texts_1[x].delete('1.0','end')
        if color_1=='light green' and x==cart_position_1:
          texts_1[cart_position_1].insert('1.0','Reached')
          try:
            if direction_1=='UP' and up_queue_1:
                up_queue_1.remove(cart_position_1)
            elif direction_1=='DOWN' and down_queue_1: 
                down_queue_1.remove(cart_position_1)
          except:pass
        else:texts_1[x].insert('end','At flr'+str(cart_position_1))
    direction_1_text_1.insert('1.0','Dir('+f'at {cart_position_1}):'+str(direction_1)+'\n')
    progress_text_1.insert('1.0','*'*15+'\n')
    progress_text_1.insert('1.0','down_queue_1 :\n  '+str(down_queue_1)+'\n')
    progress_text_1.insert('1.0','up_queue_1 :\n  '+str(up_queue_1)+'\n')
    progress_text_1.insert('1.0','On flr  '+str(cart_position_1)+'\n')
    texts_1[cart_position_1].config(bg=color_1)
    for x in range(5):
        if x==cart_position_1: continue
        texts_1[x].config(bg='white')
def change_direction_1():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1
    if direction_1 is None:
        if up_queue_1 and not down_queue_1:
            direction_1='UP'
        elif down_queue_1 and not up_queue_1:
            direction_1='DOWN'
        elif up_queue_1 and down_queue_1:
            if abs(cart_position_1-up_queue_1[0])>abs(cart_position_1-down_queue_1[0]):
                direction_1='DOWN'
            else: direction_1='UP'
    elif direction_1=='UP':
        if up_queue_1:
            direction_1='UP'
        elif not up_queue_1:
            direction_1=None
    elif direction_1=='DOWN':
        if down_queue_1:
            direction_1='DOWN'
        elif not down_queue_1:
            direction_1=None
    else:
        direction_1=None
def call_start_moving_1_():
    change_direction_1()
    window.after(delay_1,start_moving_1_)

def fans1():
    if not (up_queue_1 or down_queue_1):
        fanlabel1.config(bg="yellow")
    else:
        fanlabel1.config(bg="green")
def add_to_up_queue_1(floor):  
    global up_queue_1
    up_queue_1.append(floor)
    up_queue_1=list(set(up_queue_1))
    up_queue_1=sorted(up_queue_1)
def add_to_down_queue_1(floor):   
    global down_queue_1
    down_queue_1.append(floor)
    down_queue_1=list(set(down_queue_1))
    down_queue_1=sorted(down_queue_1, reverse=True)

def process_1():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    change_direction_1()
    if up_queue_1 or down_queue_1:
        if direction_1=='UP' and up_queue_1:
            change_direction_1()
            cart_position_1+=1
            if up_queue_1[0]==cart_position_1:
                delay_1=7000
                color_1='light green'
                del up_queue_1[0]
            else:
                delay_1=5000
                color_1='yellow'
        elif direction_1=='DOWN' and down_queue_1:
            change_direction_1()
            cart_position_1-=1
            if cart_position_1<0:cart_position_1=0;direction_1='UP'
            if down_queue_1[0]==cart_position_1:
                delay_1=7000
                color_1='light green'
                del down_queue_1[0]
            else:
                delay_1=5000
                color_1='yellow'
        start_moving_1_()
def start_moving_1_():
    fans1()
    change_direction_1()
    update_position_1()
    window.after(delay_1,process_1)

####

def r_3_up_first():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    change_direction_1()
    if cart_position_1<3:
        add_to_up_queue_1(3)
        if len(up_queue_1)==1:start_moving_1_()
    elif cart_position_1>3:
      if direction_1=='DOWN' and min(down_queue_1)<3:
        add_to_up_queue_1(3)
        if len(up_queue_1)==1:start_moving_1_()
      else:
        add_to_down_queue_1(3)
        if len(down_queue_1)==1:start_moving_1_()
    else:
        if up_queue_1 or down_queue_1:
            if up_queue_1 and direction_1=='UP':
                cart_position_1-=1
                if cart_position_1<0:cart_position_1=0;direction_1='UP'
                add_to_up_queue_1(3)
            elif down_queue_1 and direction_1=='DOWN':
                cart_position_1+=1
                add_to_down_queue_1(3)
            else:pass
            if color_1=='yellow':pass#delay_1=0
    update_position_1()  
def r_3_up_second():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    change_direction_2()
    if cart_position_2<3:
        add_to_up_queue_2(3)
        if len(up_queue_2)==1:start_moving_2_()
    elif cart_position_2>3:
      if direction_2=='DOWN' and min(down_queue_2)<3:
        add_to_up_queue_2(3)
        if len(up_queue_2)==1:start_moving_2_()
      else:
        add_to_down_queue_2(3)
        if len(down_queue_2)==1:start_moving_2_()
    else:
        if up_queue_2 or down_queue_2:
            if up_queue_2 and direction_2=='UP':
                cart_position_2-=1
                if cart_position_1<0:cart_position_1=0;direction_1='UP'
                add_to_up_queue_2(3)
            elif down_queue_2 and direction_2=='DOWN':
                cart_position_2+=1
                add_to_down_queue_2(3)
            else:pass
            if color_2=='yellow':pass#delay_1=0
    update_position_2()

def request_3_up():
    r_3_up_first()
    r_3_up_second()
    pass


def r_2_up_first():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    change_direction_1()
    if cart_position_1<2:
        add_to_up_queue_1(2)
        if len(up_queue_1)==1:start_moving_1_()
    elif cart_position_1>2:
      if direction_1=='DOWN' and min(down_queue_1)<3:
        add_to_up_queue_1(2)
        if len(up_queue_1)==1:start_moving_1_()
      else:
        add_to_down_queue_1(2)
        change_direction_1()
        if len(down_queue_1)==1:start_moving_1_()
    else:
        if up_queue_1 or down_queue_1:
            if up_queue_1 and direction_1=='UP':
                cart_position_1-=1
                if cart_position_1<0:cart_position_1=0;direction_1='UP'
                add_to_up_queue_1(2)
            elif down_queue_1 and direction_1=='DOWN':
                cart_position_1+=1
                add_to_down_queue_1(2)
            else:pass
            if color_1=='yellow':pass#delay_1=0
    update_position_1()

def r_2_up_second():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    change_direction_2()
    if cart_position_2<2:
        add_to_up_queue_2(2)
        if len(up_queue_2)==1:start_moving_2_()
    elif cart_position_2>2:
      if direction_2=='DOWN' and min(down_queue_2)<3:
        add_to_up_queue_2(2)
        if len(up_queue_2)==1:start_moving_2_()
      else:
        add_to_down_queue_2(2)
        change_direction_2()
        if len(down_queue_2)==1:start_moving_2_()
    else:
        if up_queue_2 or down_queue_2:
            if up_queue_2 and direction_2=='UP':
                cart_position_2-=1
                if cart_position_2<0:cart_position_2=0;direction_2='UP'
                add_to_up_queue_2(2)
            elif down_queue_2 and direction_2=='DOWN':
                cart_position_2+=1
                add_to_down_queue_2(2)
            else:pass
            if color_2=='yellow':pass#delay_1=0
    update_position_2()

def request_2_up(): 
    r_2_up_first()
    r_2_up_second()
    pass

def r_1_up_first():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,delay_1,color_1
    change_direction_1()
    if cart_position_1<1:
        add_to_up_queue_1(1)
        if len(up_queue_1)==1:start_moving_1_()
    elif cart_position_1>1:
      if direction_1=='DOWN' and min(down_queue_1)<3:
        add_to_up_queue_1(1)
        if len(up_queue_1)==1:start_moving_1_()
      else:
        add_to_down_queue_1(1)
        change_direction_1()
        if len(down_queue_1)==1:start_moving_1_()
    else:
        if up_queue_1 or down_queue_1:
            if up_queue_1 and direction_1=='UP':
                cart_position_1-=1
                if cart_position_1<0:cart_position_1=0;direction_1='UP';
                add_to_up_queue_1(1)
            elif down_queue_1 and direction_1=='DOWN':
                cart_position_1+=1
                add_to_down_queue_1(1)
            else:pass
            if color_1=='yellow':pass#delay_1=0
    update_position_1()

def r_1_up_second():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,delay_2,color_2
    change_direction_2()
    if cart_position_2<1:
        add_to_up_queue_2(1)
        if len(up_queue_2)==1:start_moving_2_()
    elif cart_position_2>1:
      if direction_2=='DOWN' and min(down_queue_2)<3:
        add_to_up_queue_2(1)
        if len(up_queue_2)==1:start_moving_2_()
      else:
        add_to_down_queue_2(1)
        change_direction_2()
        if len(down_queue_2)==1:start_moving_2_()
    else:
        if up_queue_2 or down_queue_2:
            if up_queue_2 and direction_2=='UP':
                cart_position_2-=1
                if cart_position_2<0:cart_position_2=0;direction_2='UP';
                add_to_up_queue_2(1)
            elif down_queue_2 and direction_2=='DOWN':
                cart_position_2+=1
                add_to_down_queue_2(1)
            else:pass
            if color_2=='yellow':pass#delay_1=0
    update_position_2()

def request_1_up():
    r_1_up_first()
    r_1_up_second()
    pass

def r_0_up_first():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    change_direction_1()
    if cart_position_1>0:
        add_to_down_queue_1(0)
        if len(down_queue_1)==1:start_moving_1_()
    else:
        if down_queue_1:
            if down_queue_1 and direction_1=='DOWN':
                cart_position_1+=1
                add_to_down_queue_1(0)
            else:pass
            if color_1=='yellow':pass#delay_1=0
    update_position_1()

def r_0_up_second():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    change_direction_2()
    if cart_position_2>0:
        add_to_down_queue_2(0)
        if len(down_queue_2)==1:start_moving_2_()
    else:
        if down_queue_2:
            if down_queue_2 and direction_2=='DOWN':
                cart_position_2+=1
                add_to_down_queue_2(0)
            else:pass
            if color_2=='yellow':pass#delay_2=0
    update_position_2()

def request_0_up():
    r_0_up_first()
    r_0_up_second()
    pass

def r_4_down_first():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    change_direction_1()
    if cart_position_1<4:
        add_to_up_queue_1(4)
        if len(up_queue_1)==1:start_moving_1_()
    else:
        if up_queue_1:
            if up_queue_1 and direction_1=='UP':
                cart_position_1-=1
                if cart_position_1<0:cart_position_1=0;direction_1='UP'
                add_to_up_queue_1(4)
            else:pass
            if color_1=='yellow':pass#delay_1=0
    update_position_1()    
def r_4_down_second():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    change_direction_2()
    if cart_position_2<4:
        add_to_up_queue_2(4)
        if len(up_queue_2)==1:start_moving_2_()
    else:
        if up_queue_2:
            if up_queue_2 and direction_2=='UP':
                cart_position_2-=1
                if cart_position_2<0:cart_position_2=0;direction_2='UP'
                add_to_up_queue_2(4)
            else:pass
            if color_2=='yellow':pass#delay_1=0
    update_position_2()   

def request_4_down():
    r_4_down_first()
    r_4_down_second()
    pass
 
def r_3_down_first():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    change_direction_1()
    if cart_position_1<3:
      if direction_1=='UP' and max(up_queue_1)>3:
        add_to_down_queue_1(3)
        if len(down_queue_1)==1:start_moving_1_()
      else:
        add_to_up_queue_1(3)
        if len(up_queue_1)==1:start_moving_1_()
    elif cart_position_1>3:
        add_to_down_queue_1(3)
        if len(down_queue_1)==1:start_moving_1_()
    else:
        if up_queue_1 or down_queue_1:
            if up_queue_1 and direction_1=='UP':
                cart_position_1-=1
                if cart_position_1<0:cart_position_1=0;direction_1='UP';pass
                add_to_up_queue_1(3)
            elif down_queue_1 and direction_1=='DOWN':
                cart_position_1+=1
                add_to_down_queue_1(3)
            else:pass
            if color_1=='yellow':pass#delay_1=0
    update_position_1()
    
def r_3_down_second():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    change_direction_2()
    if cart_position_2<3:
      if direction_2=='UP' and max(up_queue_2)>3:
        add_to_down_queue_2(3)
        if len(down_queue_2)==1:start_moving_2_()
      else:
        add_to_up_queue_2(3)
        if len(up_queue_2)==1:start_moving_2_()
    elif cart_position_2>3:
        add_to_down_queue_2(3)
        if len(down_queue_2)==1:start_moving_2_()
    else:
        if up_queue_2 or down_queue_2:
            if up_queue_2 and direction_2=='UP':
                cart_position_2-=1
                if cart_position_2<0:cart_position_2=0;direction_2='UP';pass
                add_to_up_queue_2(3)
            elif down_queue_2 and direction_2=='DOWN':
                cart_position_2+=1
                add_to_down_queue_2(3)
            else:pass
            if color_2=='yellow':pass#delay_1=0
    update_position_2()

def request_3_down():
    r_3_down_first()
    r_3_down_second()
    pass
    
def r_2_down_first():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    change_direction_1()
    if cart_position_1<2:
      if direction_1=='UP' and max(up_queue_1)>2:
        add_to_down_queue_1(2)
        if len(down_queue_1)==1:start_moving_1_()
      else:
        add_to_up_queue_1(2)
        if len(up_queue_1)==1:start_moving_1_()
    elif cart_position_1>2:
        add_to_down_queue_1(2)
        if len(down_queue_1)==1:start_moving_1_()
    else:
        if up_queue_1 or down_queue_1:
            if up_queue_1 and direction_1=='UP':
                cart_position_1-=1
                if cart_position_1<0:cart_position_1=0;direction_1='UP';pass
                add_to_up_queue_1(2)
            elif down_queue_1 and direction_1=='DOWN':
                cart_position_1+=1
                add_to_down_queue_1(2)
            else:pass
            if color_1=='yellow':pass#delay_1=0
    update_position_1()    
    
def r_2_down_second():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    #open_door_1(2)
    change_direction_2()
    if cart_position_2<2:
      if direction_2=='UP' and max(up_queue_2)>2:
        add_to_down_queue_2(2)
        if len(down_queue_2)==1:start_moving_2_()
      else:
        add_to_up_queue_2(2)
        if len(up_queue_2)==1:start_moving_2_()
    elif cart_position_2>2:
        add_to_down_queue_2(2)
        if len(down_queue_2)==1:start_moving_2_()
    else:
        if up_queue_2 or down_queue_2:
            if up_queue_2 and direction_2=='UP':
                cart_position_2-=1
                if cart_position_2<0:cart_position_2=0;direction_2='UP';pass
                add_to_up_queue_2(2)
            elif down_queue_2 and direction_2=='DOWN':
                cart_position_2+=1
                add_to_down_queue_2(2)
            else:pass
            if color_2=='yellow':pass#delay_1=0
    update_position_2()    
    
def request_2_down():
    r_2_down_first()
    r_2_down_second()
    pass    
    
def r_1_down_first():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    #open_door_1(1)
    change_direction_1()
    if cart_position_1<1:
      if direction_1=='UP' and max(up_queue_1)>1:
        add_to_down_queue_1(1)
        change_direction_1()
        if len(down_queue_1)==1:start_moving_1_()
      else:
        add_to_up_queue_1(1)
        if len(up_queue_1)==1:start_moving_1_()
    elif cart_position_1>1:
        add_to_down_queue_1(1)
        change_direction_1()
        if len(down_queue_1)==1:start_moving_1_()
    else:
        if up_queue_1 or down_queue_1:
            if up_queue_1 and direction_1=='UP':
                cart_position_1-=1
                if cart_position_1<0:cart_position_1=0;direction_1='UP';pass
                add_to_up_queue_1(1)
            elif down_queue_1 and direction_1=='DOWN':
                cart_position_1+=1
                add_to_down_queue_1(1)
            else:pass
            if color_1=='yellow':pass#delay_1=0
    update_position_1()

def r_1_down_second():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    #open_door_1(1)
    change_direction_2()
    if cart_position_2<1:
      if direction_2=='UP' and max(up_queue_2)>1:
        add_to_down_queue_2(1)
        change_direction_2()
        if len(down_queue_2)==1:start_moving_2_()
      else:
        add_to_up_queue_2(1)
        if len(up_queue_2)==1:start_moving_2_()
    elif cart_position_2>1:
        add_to_down_queue_2(1)
        change_direction_2()
        if len(down_queue_2)==1:start_moving_2_()
    else:
        if up_queue_2 or down_queue_2:
            if up_queue_2 and direction_2=='UP':
                cart_position_2-=1
                if cart_position_2<0:cart_position_2=0;direction_2='UP';pass
                add_to_up_queue_2(1)
            elif down_queue_2 and direction_2=='DOWN':
                cart_position_2+=1
                add_to_down_queue_2(1)
            else:pass
            if color_2=='yellow':pass#delay_1=0
    update_position_2()

def request_1_down():
    r_1_down_first()
    r_1_down_second()
#######

def pressed_1_4():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    if direction_1!=None and texts_1[cart_position_1].cget('background')!='light green' :return
    if cart_position_1==4:pass
    else:
        add_to_up_queue_1(4)
    update_position_1()#             
def pressed_1_3():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    if direction_1!=None and texts_1[cart_position_1].cget('background')!='light green' :return
    if cart_position_1==3:pass
    elif cart_position_1<3:
        add_to_up_queue_1(3)
    else:
        add_to_down_queue_1(3)
    update_position_1()#      
def pressed_1_2():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    if direction_1!=None and texts_1[cart_position_1].cget('background')!='light green' :return
    if cart_position_1==2:pass
    elif cart_position_1<2:
        add_to_up_queue_1(2)
    else:
        add_to_down_queue_1(2)
    update_position_1()# 
def pressed_1_1():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    if direction_1!=None and texts_1[cart_position_1].cget('background')!='light green' :return
    if cart_position_1==1:pass
    elif cart_position_1<1:
        add_to_up_queue_1(1)
    else:
        add_to_down_queue_1(1)
    update_position_1()#  
def pressed_1_0():
    global up_queue_1,down_queue_1,door_closed_1,direction_1,cart_position_1,color_1,delay_1
    if direction_1!=None and texts_1[cart_position_1].cget('background')!='light green' :return
    if cart_position_1==0:pass
    else:
        add_to_down_queue_1(0)
    update_position_1()#  

#ELEVATOR 1
#Arrow images
DownT=Image.open("DownT.png")
DownT=DownT.resize((35,35))
DownT=ImageTk.PhotoImage(DownT)
UpT=Image.open("UpT.png")
UpT=UpT.resize((35,35))
UpT=ImageTk.PhotoImage(UpT)
#Fan Images
fan=Image.open("fan.png")
fan=fan.resize((70,70))
fan=ImageTk.PhotoImage(fan)
elevator1=Label(window,bg='ivory',text='Elevator 1',font="jokerman",foreground='black',background='#FFF29C')
elevator1.place(x=90,y=15,height=35,width=150)
elevator2=Label(window,bg='ivory',text='Elevator 2',font="jokerman",foreground='black',background='#FFF29C')
elevator2.place(x=710,y=15,height=35,width=150)
#starting from left side of screen
#frame0
frame0=Frame(window,bg='red')
frame0.place(x=10,y=65,height=650,width=150)
btn3=Button(frame0,bg='yellow',text='3',command=pressed_1_3)
btn3.place(x=20,y=5,height=35,width=25)
btn4=Button(frame0,bg='yellow',text='4',command=pressed_1_4)
btn4.place(x=100,y=5,height=35,width=25)
btn2=Button(frame0,bg='yellow',text='2',command=pressed_1_2)
btn2.place(x=20,y=50,height=35,width=25)
btn1=Button(frame0,bg='yellow',text='1',command=pressed_1_1)
btn1.place(x=100,y=50,height=35,width=25)
btn0=Button(frame0,bg='yellow',text='0',command=pressed_1_0)
btn0.place(x=20,y=100,height=35,width=25)
btngo=Button(frame0,bg='yellow',text='GO',command=start_moving_1_)
btngo.place(x=100,y=100,height=35,width=25)
progress_text_1=Text(frame0,bg='Ivory')
progress_text_1.place(x=10,y=150,height=250,width=125)
direction_1_text_1=Text(frame0,bg='Ivory')
direction_1_text_1.place(x=10,y=420,height=120,width=125)
fanlabel1=Label(frame0,image=fan)
fanlabel1.place(x=35,y=560,height=80,width=80)
#frame1
frame1=Frame(window,bg='red')
frame1.place(x=180,y=65,height=650,width=150)
text4=Text(frame1,bg='silver',font='callibri 12')
text4.place(x=10,y=25,height=100,width=130)
text3=Text(frame1,bg='silver',font='callibri 12')
text3.place(x=10,y=145,height=100,width=130)
text2=Text(frame1,bg='silver',font='callibri 12')
text2.place(x=10,y=265,height=100,width=130)
text1=Text(frame1,bg='silver',font='callibri 12')
text1.place(x=10,y=385,height=100,width=130)
text0=Text(frame1,bg='silver',font='callibri 12')
text0.place(x=10,y=505,height=100,width=130)

texts_1=(text0,text1,text2,text3,text4)

#frame2
frame2=Frame(window,bg='lightblue')
frame2.place(x=360,y=65,height=650,width=40)
label4=Label(frame2,bg='blue',text='4',font='callibri 20 bold',foreground='white')
label4.place(x=5,y=50,height=50,width=30)
label3=Label(frame2,bg='blue',text='3',font='callibri 20 bold',foreground='white')
label3.place(x=5,y=170,height=50,width=30)
label2=Label(frame2,bg='blue',text='2',font='callibri 20 bold',foreground='white')
label2.place(x=5,y=290,height=50,width=30)
label1=Label(frame2,bg='blue',text='1',font='callibri 20 bold',foreground='white')
label1.place(x=5,y=410,height=50,width=30)
label0=Label(frame2,bg='blue',text='0',font='callibri 20 bold',foreground='white')
label0.place(x=5,y=530,height=50,width=30)
#frame3
frame3=Frame(window,bg='red')
frame3.place(x=430,y=65,height=650,width=100)
btn4=Button(frame3,bg='#7e7e7e',image=DownT,command=request_4_down)
btn4.place(x=25,y=50,height=50,width=50)
btn3_1=Button(frame3,bg="#7e7e7e",image=UpT,command=request_3_up)
btn3_1.place(x=25,y=145,height=50,width=50)
btn3_2=Button(frame3,bg='#7e7e7e',image=DownT,command=request_3_down)
btn3_2.place(x=25,y=205,height=50,width=50)
btn2_1=Button(frame3,bg="#7e7e7e",image=UpT,command=request_2_up)
btn2_1.place(x=25,y=265,height=50,width=50)
btn2_2=Button(frame3,bg='#7e7e7e',image=DownT,command=request_2_down)
btn2_2.place(x=25,y=325,height=50,width=50)
btn1_1=Button(frame3,bg="#7e7e7e",image=UpT,command=request_1_up)
btn1_1.place(x=25,y=385,height=50,width=50)
btn1_2=Button(frame3,bg='#7e7e7e',image=DownT,command=request_1_down)
btn1_2.place(x=25,y=445,height=50,width=50)
btn0=Button(frame3,bg='#7e7e7e',image=UpT,command=request_0_up)
btn0.place(x=25,y=535,height=50,width=50)




#ELEVATOR 2
def update_position_2():
    global cart_position_2,direction_2,color_2,up_queue_2,down_queue_2
    for x in range(5):
        texts_2[x].delete('1.0','end')
        if color_2=='light green' and x==cart_position_2:
          texts_2[cart_position_2].insert('1.0','Reached')
          try:
            if direction_2=='UP' and up_queue_2:
                up_queue_2.remove(cart_position_2)
            elif direction_2=='DOWN' and down_queue_2: 
                down_queue_2.remove(cart_position_2)
          except:pass
        else:texts_2[x].insert('end','At flr'+str(cart_position_2))
    direction_2_text_2.insert('1.0','Dir('+f'at {cart_position_2}):'+str(direction_2)+'\n')
    progress_text_2.insert('1.0','*'*15+'\n')
    progress_text_2.insert('1.0','down_queue_2 :\n  '+str(down_queue_2)+'\n')
    progress_text_2.insert('1.0','up_queue_2 :\n  '+str(up_queue_2)+'\n')
    progress_text_2.insert('1.0','On flr  '+str(cart_position_2)+'\n')
    texts_2[cart_position_2].config(bg=color_2)
    for x in range(5):
        if x==cart_position_2: continue
        texts_2[x].config(bg='white')
def change_direction_2():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2
    if direction_2 is None:
        if up_queue_2 and not down_queue_2:
            direction_2='UP'
        elif down_queue_2 and not up_queue_2:
            direction_2='DOWN'
        elif up_queue_2 and down_queue_2:
            if abs(cart_position_2-up_queue_2[0])>abs(cart_position_2-down_queue_2[0]):
                direction_2='DOWN'
            else: direction_2='UP'
    elif direction_2=='UP':
        if up_queue_2:
            direction_2='UP'
        elif not up_queue_2:
            direction_2=None
    elif direction_2=='DOWN':
        if down_queue_2:
            direction_2='DOWN'
        elif not down_queue_2:
            direction_2=None
    else:
        direction_2=None

def call_start_moving_2_():
    change_direction_2()
    window.after(delay_2,start_moving_2_)

def fans2():
    if not (up_queue_2 or down_queue_2):
        fanlabel2.config(bg="yellow")
    else:
        fanlabel2.config(bg="green")
def add_to_up_queue_2(floor):  
    global up_queue_2
    up_queue_2.append(floor)
    up_queue_2=list(set(up_queue_2))
    up_queue_2=sorted(up_queue_2)
def add_to_down_queue_2(floor):   
    global down_queue_2
    down_queue_2.append(floor)
    down_queue_2=list(set(down_queue_2))
    down_queue_2=sorted(down_queue_2, reverse=True)

def process_2():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    change_direction_2()
    if up_queue_2 or down_queue_2:
        if direction_2=='UP' and up_queue_2:
            change_direction_2()
            cart_position_2+=1
            if up_queue_2[0]==cart_position_2:
                delay_2=7000
                color_2='light green'
                del up_queue_2[0]
            else:
                delay_2=5000
                color_2='yellow'
        elif direction_2=='DOWN' and down_queue_2:
            change_direction_2()
            cart_position_2-=1
            if cart_position_2<0:cart_position_2=0;direction_2='UP'
            if down_queue_2[0]==cart_position_2:
                delay_2=7000
                color_2='light green'
                del down_queue_2[0]
            else:
                delay_2=5000
                color_2='yellow'
        start_moving_2_()
def start_moving_2_():
    fans2()
    change_direction_2()
    update_position_2()
    window.after(delay_2,process_2)
def pressed_2_4():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    if direction_2!=None and texts_2[cart_position_2].cget('background')!='light green' :return
    if cart_position_2==4:pass
    else:
        add_to_up_queue_2(4)
    update_position_2()#             
def pressed_2_3():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    if direction_2!=None and texts_2[cart_position_2].cget('background')!='light green' :return
    if cart_position_2==3:pass
    elif cart_position_2<3:
        add_to_up_queue_2(3)
    else:
        add_to_down_queue_2(3)
    update_position_2()#      
def pressed_2_2():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    if direction_2!=None and texts_2[cart_position_2].cget('background')!='light green' :return
    if cart_position_2==2:pass
    elif cart_position_2<2:
        add_to_up_queue_2(2)
    else:
        add_to_down_queue_2(2)
    update_position_2()# 
def pressed_2_1():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    if direction_2!=None and texts_2[cart_position_2].cget('background')!='light green' :return
    if cart_position_2==1:pass
    elif cart_position_2<1:
        add_to_up_queue_2(1)
    else:
        add_to_down_queue_2(1)
    update_position_2()#  
def pressed_2_0():
    global up_queue_2,down_queue_2,door_closed_2,direction_2,cart_position_2,color_2,delay_2
    if direction_2!=None and texts_2[cart_position_2].cget('background')!='light green' :return
    if cart_position_2==0:pass
    else:
        add_to_down_queue_2(0)
    update_position_2()#  


#frame4
frame4=Frame(window,bg='lightblue')
frame4.place(x=560,y=65,height=650,width=40)
label2_4=Label(frame4,bg='blue',text='4',font='callibri 20 bold',foreground='white')
label2_4.place(x=5,y=50,height=50,width=30)
label2_3=Label(frame4,bg='blue',text='3',font='callibri 20 bold',foreground='white')
label2_3.place(x=5,y=170,height=50,width=30)
label2_2=Label(frame4,bg='blue',text='2',font='callibri 20 bold',foreground='white')
label2_2.place(x=5,y=290,height=50,width=30)
label2_1=Label(frame4,bg='blue',text='1',font='callibri 20 bold',foreground='white')
label2_1.place(x=5,y=410,height=50,width=30)
label2_0=Label(frame4,bg='blue',text='0',font='callibri 20 bold',foreground='white')
label2_0.place(x=5,y=530,height=50,width=30)
#frame5
frame5=Frame(window,bg='red')
frame5.place(x=630,y=65,height=650,widt=150)
text2_4=Text(frame5,bg='silver',font='callibri 12')
text2_4.place(x=10,y=25,height=100,width=130)
text2_3=Text(frame5,bg='silver',font='callibri 12')
text2_3.place(x=10,y=145,height=100,width=130)
text2_2=Text(frame5,bg='silver',font='callibri 12')
text2_2.place(x=10,y=265,height=100,width=130)
text2_1=Text(frame5,bg='silver',font='callibri 12')
text2_1.place(x=10,y=385,height=100,width=130)
text2_0=Text(frame5,bg='silver',font='callibri 12')
text2_0.place(x=10,y=505,height=100,width=130)
texts_2=(text2_0,text2_1,text2_2,text2_3,text2_4)
#frame6
frame6=Frame(window,bg='red')
frame6.place(x=800,y=65,height=650,width=150)
btn2_3=Button(frame6,bg='yellow',text='3',command=pressed_2_3)
btn2_3.place(x=20,y=5,height=35,width=25)
btn2_4=Button(frame6,bg='yellow',text='4',command=pressed_2_4)
btn2_4.place(x=100,y=5,height=35,width=25)
btn2_2=Button(frame6,bg='yellow',text='2',command=pressed_2_2)
btn2_2.place(x=20,y=50,height=35,width=25)
btn2_1=Button(frame6,bg='yellow',text='1',command=pressed_2_1)
btn2_1.place(x=100,y=50,height=35,width=25)
btn2_0=Button(frame6,bg='yellow',text='0',command=pressed_2_0)
btn2_0.place(x=20,y=100,height=35,width=25)
btn2_go=Button(frame6,bg='yellow',text='GO',command=start_moving_2_)
btn2_go.place(x=100,y=100,height=35,width=25)
progress_text_2=Text(frame6,bg='Ivory')
progress_text_2.place(x=10,y=150,height=250,width=125)
direction_2_text_2=Text(frame6,bg='Ivory')
direction_2_text_2.place(x=10,y=420,height=120,width=125)
fanlabel2=Label(frame6,image=fan)
fanlabel2.place(x=35,y=560,height=80,width=80)


update_position_1()  
update_position_2()  
window.mainloop()