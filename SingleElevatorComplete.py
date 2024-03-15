import tkinter as tk
import time
import threading as th
from PIL import Image,ImageTk
window=tk.Tk()
window.config(bg='blue')
FLOORS=(0,1,2,3,4)
WEIGHT_LIMIT=550
current_weight=500
door_closed=True
direction=None
up_queue=list()
down_queue=list()
cart_position=0
color='yellow' 
delay=5000
  
def update_position():
    global cart_position,direction,color,up_queue,down_queue
    for x in range(5):
        texts[x].delete('1.0','end')
        if color=='light green' and x==cart_position:
          texts[cart_position].insert('1.0','Reached')
          try:
            if direction=='UP' and up_queue:
                up_queue.remove(cart_position)
            elif direction=='DOWN' and down_queue: 
                down_queue.remove(cart_position)
          except:pass
        else:texts[x].insert('end','At flr'+str(cart_position))
    direction_text.insert('1.0','Dir('+f'at {cart_position}):'+str(direction)+'\n')
    progress_text.insert('1.0','*'*15+'\n')
    progress_text.insert('1.0','down_queue :\n  '+str(down_queue)+'\n')
    progress_text.insert('1.0','up_queue :\n  '+str(up_queue)+'\n')
    progress_text.insert('1.0','On flr  '+str(cart_position)+'\n')
    texts[cart_position].config(bg=color)
    for x in range(5):
        if x==cart_position: continue
        texts[x].config(bg='white')
    

def change_direction():
    global up_queue,down_queue,door_closed,direction,cart_position
    if direction is None:
        if up_queue and not down_queue:
            direction='UP'
        elif down_queue and not up_queue:
            direction='DOWN'
        elif up_queue and down_queue:
            if abs(cart_position-up_queue[0])>abs(cart_position-down_queue[0]):
                direction='DOWN'
            else: direction='UP'
    elif direction=='UP':
        if up_queue:
            direction='UP'
        elif not up_queue:
            direction=None
    elif direction=='DOWN':
        if down_queue:
            direction='DOWN'
        elif not down_queue:
            direction=None
    else:
        direction=None

def call_start_moving():
    change_direction()
    window.after(delay,start_moving)
    
def open_door(num):
    global cart_position,door_closed
    if cart_position==num and door_closed:
        texts[cart_position].delete('1.0','end')
        texts[cart_position].insert('1.0','Accesible')
        door_closed=False
    elif cart_position==num and not door_closed:
        texts[cart_position].delete('1.0','end')
        texts[cart_position].insert('1.0','At flr'+str(cart_position))
        door_closed=True

def fans():
    if not (up_queue or down_queue):
        fan_label.config(bg="yellow")
    else:
        fan_label.config(bg="green")

def add_to_up_queue(floor):  
    global up_queue
    up_queue.append(floor)
    up_queue=list(set(up_queue))
    up_queue=sorted(up_queue)
def add_to_down_queue(floor):   
    global down_queue
    down_queue.append(floor)
    down_queue=list(set(down_queue))
    down_queue=sorted(down_queue, reverse=True)

def process():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    change_direction()
    if up_queue or down_queue:
        if direction=='UP' and up_queue:
            change_direction()
            cart_position+=1
            if up_queue[0]==cart_position:
                delay=7000
                color='light green'
                del up_queue[0]
            else:
                delay=5000
                color='yellow'
        elif direction=='DOWN' and down_queue:
            change_direction()
            cart_position-=1
            if cart_position<0:cart_position=0;direction='UP'
            if down_queue[0]==cart_position:
                delay=7000
                color='light green'
                del down_queue[0]
            else:
                delay=5000
                color='yellow'
       # update_position()#
        start_moving()
    
def start_moving():
    fans()
    change_direction()
    update_position()
    window.after(delay,process)
    #update_position()


def request_3_up():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    open_door(3)
    change_direction()
    if cart_position<3:
        add_to_up_queue(3)
        if len(up_queue)==1:start_moving()
    elif cart_position>3:
      if direction=='DOWN' and min(down_queue)<3:
        add_to_up_queue(3)
        if len(up_queue)==1:start_moving()
      else:
        add_to_down_queue(3)
        if len(down_queue)==1:start_moving()
    else:
        if up_queue or down_queue:
            if up_queue and direction=='UP':
                cart_position-=1
                if cart_position<0:cart_position=0;direction='UP'
                add_to_up_queue(3)
            elif down_queue and direction=='DOWN':
                cart_position+=1
                add_to_down_queue(3)
            else:pass
            if color=='yellow':pass#delay=0
    update_position()
        
def request_2_up(): 
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    open_door(2)
    change_direction()
    if cart_position<2:
        add_to_up_queue(2)
        if len(up_queue)==1:start_moving()
    elif cart_position>2:
      if direction=='DOWN' and min(down_queue)<3:
        add_to_up_queue(2)
        if len(up_queue)==1:start_moving()
      else:
        add_to_down_queue(2)
        change_direction()
        if len(down_queue)==1:start_moving()
    else:
        if up_queue or down_queue:
            if up_queue and direction=='UP':
                cart_position-=1
                if cart_position<0:cart_position=0;direction='UP'
                add_to_up_queue(2)
            elif down_queue and direction=='DOWN':
                cart_position+=1
                add_to_down_queue(2)
            else:pass
            if color=='yellow':pass#delay=0
    update_position()
    
def request_1_up():
    global up_queue,down_queue,door_closed,direction,cart_position,delay,color
    open_door(1)
    change_direction()
    if cart_position<1:
        add_to_up_queue(1)
        if len(up_queue)==1:start_moving()
    elif cart_position>1:
      if direction=='DOWN' and min(down_queue)<3:
        add_to_up_queue(1)
        if len(up_queue)==1:start_moving()
      else:
        add_to_down_queue(1)
        change_direction()
        if len(down_queue)==1:start_moving()
    else:
        if up_queue or down_queue:
            if up_queue and direction=='UP':
                cart_position-=1
                if cart_position<0:cart_position=0;direction='UP';
                add_to_up_queue(1)
            elif down_queue and direction=='DOWN':
                cart_position+=1
                add_to_down_queue(1)
            else:pass
            if color=='yellow':pass#delay=0
    update_position()
    
def request_0_up():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    open_door(0)
    change_direction()
    if cart_position>0:
        add_to_down_queue(0)
        if len(down_queue)==1:start_moving()
    else:
        if down_queue:
            if down_queue and direction=='DOWN':
                cart_position+=1
                add_to_down_queue(0)
            else:pass
            if color=='yellow':pass#delay=0
    update_position()
    
def request_4_down():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    open_door(4)
    change_direction()
    if cart_position<4:
        add_to_up_queue(4)
        if len(up_queue)==1:start_moving()
    else:
        if up_queue:
            if up_queue and direction=='UP':
                cart_position-=1
                if cart_position<0:cart_position=0;direction='UP'
                add_to_up_queue(4)
            else:pass
            if color=='yellow':pass#delay=0
    update_position()
        
def request_3_down():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    open_door(3)
    change_direction()
    if cart_position<3:
      if direction=='UP' and max(up_queue)>3:
        add_to_down_queue(3)
        if len(down_queue)==1:start_moving()
      else:
        add_to_up_queue(3)
        if len(up_queue)==1:start_moving()
    elif cart_position>3:
        add_to_down_queue(3)
        if len(down_queue)==1:start_moving()
    else:
        if up_queue or down_queue:
            if up_queue and direction=='UP':
                cart_position-=1
                if cart_position<0:cart_position=0;direction='UP';pass
                add_to_up_queue(3)
            elif down_queue and direction=='DOWN':
                cart_position+=1
                add_to_down_queue(3)
            else:pass
            if color=='yellow':pass#delay=0
    update_position()
        
def request_2_down():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    open_door(2)
    change_direction()
    if cart_position<2:
      if direction=='UP' and max(up_queue)>2:
        add_to_down_queue(2)
        if len(down_queue)==1:start_moving()
      else:
        add_to_up_queue(2)
        if len(up_queue)==1:start_moving()
    elif cart_position>2:
        add_to_down_queue(2)
        if len(down_queue)==1:start_moving()
    else:
        if up_queue or down_queue:
            if up_queue and direction=='UP':
                cart_position-=1
                if cart_position<0:cart_position=0;direction='UP';pass
                add_to_up_queue(2)
            elif down_queue and direction=='DOWN':
                cart_position+=1
                add_to_down_queue(2)
            else:pass
            if color=='yellow':pass#delay=0
    update_position()
        
def request_1_down():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    open_door(1)
    change_direction()
    if cart_position<1:
      if direction=='UP' and max(up_queue)>1:
        add_to_down_queue(1)
        change_direction()
        if len(down_queue)==1:start_moving()
      else:
        add_to_up_queue(1)
        if len(up_queue)==1:start_moving()
    elif cart_position>1:
        add_to_down_queue(1)
        change_direction()
        if len(down_queue)==1:start_moving()
    else:
        if up_queue or down_queue:
            if up_queue and direction=='UP':
                cart_position-=1
                if cart_position<0:cart_position=0;direction='UP';pass
                add_to_up_queue(1)
            elif down_queue and direction=='DOWN':
                cart_position+=1
                add_to_down_queue(1)
            else:pass
            if color=='yellow':pass#delay=0
    update_position()
            
def pressed_4():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    if direction!=None and ((len(up_queue)>0 and cart_position!=up_queue[0]) or (len(down_queue)>0 and cart_position!=down_queue[0])) :return
    if cart_position==4:pass
    else:
        add_to_up_queue(4)
    update_position()#        
        
def pressed_3():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    if direction!=None and ((len(up_queue)>0 and cart_position!=up_queue[0]) or (len(down_queue)>0 and cart_position!=down_queue[0])) :return
    if cart_position==3:pass
    elif cart_position<3:
        add_to_up_queue(3)
    else:
        add_to_down_queue(3)
    update_position()#
        
def pressed_2():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    if direction!=None and ((len(up_queue)>0 and cart_position!=up_queue[0]) or (len(down_queue)>0 and cart_position!=down_queue[0])) :return
    if cart_position==2:pass
    elif cart_position<2:
        add_to_up_queue(2)
    else:
        add_to_down_queue(2)
    update_position()#
    
def pressed_1():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    if direction!=None and ((len(up_queue)>0 and cart_position!=up_queue[0]) or (len(down_queue)>0 and cart_position!=down_queue[0])) :return
    if cart_position==1:pass
    elif cart_position<1:
        add_to_up_queue(1)
    else:
        add_to_down_queue(1)
    update_position()#
    
def pressed_0():
    global up_queue,down_queue,door_closed,direction,cart_position,color,delay
    if direction!=None and ((len(up_queue)>0 and cart_position!=up_queue[0]) or (len(down_queue)>0 and cart_position!=down_queue[0])) :return
    if cart_position==0:pass
    else:
        add_to_down_queue(0)
    update_position()#    
    
frame_0=tk.Frame(window,bg='light blue')
frame_0.grid(row=0,column=0,padx=5,pady=5,sticky='ns')
y=45
label_4=tk.Label(frame_0,text='4',bg='blue',fg='yellow')
label_4.grid(row=0,column=0,padx=2,pady=y)
label_3=tk.Label(frame_0,text='3',bg='blue',fg='yellow')
label_3.grid(row=2,column=0,padx=2,pady=y)
label_2=tk.Label(frame_0,text='2',bg='blue',fg='yellow')
label_2.grid(row=4,column=0,padx=2,pady=y)
label_1=tk.Label(frame_0,text='1',bg='blue',fg='yellow')
label_1.grid(row=6,column=0,padx=2,pady=y)
label_0=tk.Label(frame_0,text='0',bg='blue',fg='yellow')
label_0.grid(row=8,column=0,padx=2,pady=y)
frame_1=tk.Frame(window,bg='red')
frame_1.grid(row=0,column=1,padx=5,pady=5)
text_4=tk.Text(frame_1,height=5,width=8)
text_4.pack(side=tk.TOP,padx=5,pady=15)
text_3=tk.Text(frame_1,height=5,width=8)
text_3.pack(side=tk.TOP,padx=5,pady=15)
text_2=tk.Text(frame_1,height=5,width=8)
text_2.pack(side=tk.TOP,padx=5,pady=15)
text_1=tk.Text(frame_1,height=5,width=8)
text_1.pack(side=tk.TOP,padx=5,pady=15)
text_0=tk.Text(frame_1,height=5,width=8)
text_0.pack(side=tk.TOP,padx=5,pady=15)
texts=(text_0,text_1,text_2,text_3,text_4)
frame_2=tk.Frame(window,bg='red')
frame_2.grid(row=0,column=2,padx=5,pady=5)
DownT=Image.open("DownT.png")
DownT=DownT.resize((30,30))
DownT=ImageTk.PhotoImage(DownT)
UpT=Image.open("UpT.png")
UpT=UpT.resize((30,30))
UpT=ImageTk.PhotoImage(UpT)
btn_4u=tk.Button(frame_2,text=' ',height=1,width=4,borderwidth=0,bg='red')
btn_4u.pack(side=tk.TOP,padx=5,pady=5)
btn_4d=tk.Button(frame_2,image=DownT,height=23,width=40,borderwidth=0,bg='red',command=request_4_down)
btn_4d.pack(side=tk.TOP,padx=5,pady=15)
btn_3u=tk.Button(frame_2,image=UpT,height=20,width=40,borderwidth=0,bg='red',command=request_3_up)
btn_3u.pack(side=tk.TOP,padx=5,pady=15)
btn_3d=tk.Button(frame_2,image=DownT,height=25,width=40,borderwidth=0,bg='red',command=request_3_down)
btn_3d.pack(side=tk.TOP,padx=5,pady=15)
btn_2u=tk.Button(frame_2,image=UpT,height=23,width=40,borderwidth=0,bg='red',command=request_2_up)
btn_2u.pack(side=tk.TOP,padx=5,pady=15)
btn_2d=tk.Button(frame_2,image=DownT,height=25,width=40,borderwidth=0,bg='red',command=request_2_down)
btn_2d.pack(side=tk.TOP,padx=5,pady=15)
btn_1u=tk.Button(frame_2,image=UpT,height=25,width=40,borderwidth=0,bg='red',command=request_1_up)
btn_1u.pack(side=tk.TOP,padx=5,pady=15)
btn_1d=tk.Button(frame_2,image=DownT,height=27,width=40,borderwidth=0,bg='red',command=request_1_down)
btn_1d.pack(side=tk.TOP,padx=5,pady=15)
btn_0u=tk.Button(frame_2,image=UpT,height=25,width=40,borderwidth=0,bg='red',command=request_0_up)
btn_0u.pack(side=tk.TOP,padx=5,pady=15)
btn_0d=tk.Button(frame_2,text=' ',height=1,width=4,borderwidth=0,bg='red')
btn_0d.pack(side=tk.TOP,padx=5,pady=10)
frame_3=tk.Frame(window,bg='red')
frame_3.grid(row=0,column=3,padx=5,pady=5)
btn_3=tk.Button(frame_3,text='3',bg='yellow',command=pressed_3)
btn_3.grid(row=0,column=0, padx=5,pady=5)
btn_4=tk.Button(frame_3,text='4',bg='yellow',command=pressed_4)
btn_4.grid(row=0,column=1, padx=5,pady=5)
btn_1=tk.Button(frame_3,text='1',bg='yellow',command=pressed_1)
btn_1.grid(row=1,column=0, padx=5,pady=5)
btn_2=tk.Button(frame_3,text='2',bg='yellow',command=pressed_2)
btn_2.grid(row=1,column=1 ,padx=5,pady=5)
btn_0=tk.Button(frame_3,text='0',bg='yellow',command=pressed_0)
btn_0.grid(row=2,column=0, padx=5,pady=5)
btn_go=tk.Button(frame_3,text='Go',bg='yellow',command=call_start_moving)
btn_go.grid(row=2,column=1, padx=5,pady=5)
progress_text=tk.Text(frame_3,width=15,height=20)
progress_text.grid(row=3,column=0,columnspan=2,padx=5,pady=5)
direction_text=tk.Text(frame_3,width=15,height=5)
direction_text.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
frame_4=tk.Frame(frame_3,bg='black')
frame_4.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
fan=Image.open("fan.png")
fan1=fan.resize((40,40))
fan1=ImageTk.PhotoImage(fan1)
fan_label=tk.Label(frame_4,bg='yellow',image=fan1,height=50,width=50)
fan_label.pack(padx=5,pady=5)
update_position()  
window.mainloop()