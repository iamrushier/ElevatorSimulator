import tkinter as tk
window=tk.Tk()
#window.geometry('500x200')
window.config(bg='blue')



#Elevator software
FLOORS=(0,1,2,3,4)
WEIGHT_LIMIT=550

#Temporary data
current_weight=500

#flags
moving=True
direction=None
up_queue=list()
down_queue=list()
cart_position=4


def update_position():
    text_0.insert('1.0','At flr'+str(cart_position))
    text_1.insert('1.0','At flr'+str(cart_position))
    text_2.insert('1.0','At flr'+str(cart_position))
    text_3.insert('1.0','At flr'+str(cart_position))
    text_4.insert('1.0','At flr'+str(cart_position))

def change_direction():
    global up_queue,down_queue,moving,direction,cart_position
    if direction is None and up_queue:
        direction='UP'
    elif direction is None and down_queue:
        direction='DOWN'
    else:direction=None
    
def start_moving():
    global up_queue,down_queue,moving,direction,cart_position
    change_direction()
    while up_queue or down_queue:
        pass
    direction=None 

#logic
def request_3_up():
    global up_queue,down_queue,moving,direction,cart_position
    if cart_position==3:
        text_3.delete('1.0','end')
        text_3.insert('1.0','Door opened')
        moving=False
        pass
    elif cart_position<3:
        pass
    elif cart_position>3:
        pass
    else:pass #Cart moving
    
def request_2_up(): 
    global up_queue,down_queue,moving,direction,cart_position
    if cart_position==2:
        text_2.delete('1.0','end')
        text_2.insert('1.0','Door opened')
        moving=False
        pass
    elif cart_position<2:
        pass
    elif cart_position>2:
        pass
    else:pass #Cart moving

def request_1_up():
    global up_queue,down_queue,moving,direction,cart_position
    if cart_position==1:
        text_1.delete('1.0','end')
        text_1.insert('1.0','Door opened')
        moving=False
        pass
    elif cart_position<1:
        pass
    elif cart_position>1:
        pass
    else:pass #Cart moving

def request_0_up():
    global up_queue,down_queue,moving,direction,cart_position
    if cart_position==0:
        text_0.delete('1.0','end')
        text_0.insert('1.0','Door opened')
        moving=False
        pass
    elif cart_position>0:
        pass
    else:pass #Cart moving

def request_4_down():
    global up_queue,down_queue,moving,direction,cart_position
    if cart_position==4:
        text_4.delete('1.0','end')
        text_4.insert('1.0','Door opened')
        moving=False
        pass
    elif cart_position<4:
        pass
    else:pass #Cart moving
    
def request_3_down():
    global up_queue,down_queue,moving,direction,cart_position
    if cart_position==3:
        text_3.delete('1.0','end')
        text_3.insert('1.0','Door opened')
        moving=False
        pass
    elif cart_position<3:
        pass
    elif cart_position>3:
        pass
    else:pass #Cart moving
    
def request_2_down():
    global up_queue,down_queue,moving,direction,cart_position
    if cart_position==2:
        text_2.delete('1.0','end')
        text_2.insert('1.0','Door opened')
        moving=False
        pass
    elif cart_position<2:
        pass
    elif cart_position>2:
        pass
    else:pass #Cart moving
    
def request_1_down():
    global up_queue,down_queue,moving,direction,cart_position
    if cart_position==1:
        text_1.delete('1.0','end')
        text_1.insert('1.0','Door opened')
        moving=False
        pass
    elif cart_position<1:
        pass
    elif cart_position>1:
        pass
    else:pass #Cart moving
        
def pressed_4():
    global up_queue,down_queue,moving,direction,cart_position
    if moving==True:pass
    else:
        if cart_position==4:
            pass
        else:
            up_queue.append(4)
            up_queue=list(set(up_queue))
            up_queue=sorted(up_queue)
        progress_text.insert('1.0','up_queue :\n  '+str(up_queue)+'\n')
        progress_text.insert('end','down_queue :\n  '+str(down_queue)+'\n')
        
def pressed_3():
    global up_queue,down_queue,moving,direction,cart_position
    if moving==True:pass
    else:
        if cart_position==3:
            pass
        elif cart_position<3:
            up_queue.append(3)
            up_queue=list(set(up_queue))
            up_queue=sorted(up_queue)
        else:
            down_queue.append(3)
            down_queue=list(set(down_queue))
            down_queue=sorted(down_queue, reverse=True)
        progress_text.insert('1.0','up_queue :\n  '+str(up_queue)+'\n')
        progress_text.insert('end','down_queue :\n  '+str(down_queue)+'\n')
        
def pressed_2():
    global up_queue,down_queue,moving,direction,cart_position
    if moving==True:pass
    else:
        if cart_position==2:
            pass
        elif cart_position<2:
            up_queue.append(2)
            up_queue=list(set(up_queue))
            up_queue=sorted(up_queue)
        else:
            down_queue.append(2)
            down_queue=list(set(down_queue))
            down_queue=sorted(down_queue, reverse=True)
        progress_text.insert('1.0','up_queue :\n  '+str(up_queue)+'\n')
        progress_text.insert('end','down_queue :\n  '+str(down_queue)+'\n')
    
def pressed_1():
    global up_queue,down_queue,moving,direction,cart_position
    if moving==True:
        progress_text.insert('end','Moving\n')
        pass
    else:
        if cart_position==1:
            pass
        elif cart_position<1:
            up_queue.append(1)
            up_queue=list(set(up_queue))
            up_queue=sorted(up_queue)
        else:
            down_queue.append(1)
            down_queue=list(set(down_queue))
            down_queue=sorted(down_queue, reverse=True)
        progress_text.insert('1.0','up_queue :\n  '+str(up_queue)+'\n')
        progress_text.insert('end','down_queue :\n  '+str(down_queue)+'\n')
        
def pressed_0():
    global up_queue,down_queue,moving,direction,cart_position
    if moving==True:pass
    else:
        if cart_position==0:
            pass
        else:
            down_queue.append(0)
            down_queue=list(set(down_queue))
            down_queue=sorted(down_queue,reverse=True)
        progress_text.insert('1.0','up_queue :\n  '+str(up_queue)+'\n')
        progress_text.insert('end','down_queue :\n  '+str(down_queue)+'\n')
    
    
frame_1=tk.Frame(window,bg='red')
frame_1.grid(row=0,column=0,padx=5,pady=5)
text_4=tk.Text(frame_1,height=5,width=6)
text_4.pack(side=tk.TOP,padx=5,pady=20)
text_3=tk.Text(frame_1,height=5,width=6)
text_3.pack(side=tk.TOP,padx=5,pady=20)
text_2=tk.Text(frame_1,height=5,width=6)
text_2.pack(side=tk.TOP,padx=5,pady=20)
text_1=tk.Text(frame_1,height=5,width=6)
text_1.pack(side=tk.TOP,padx=5,pady=20)
text_0=tk.Text(frame_1,height=5,width=6)
text_0.pack(side=tk.TOP,padx=5,pady=20)


frame_2=tk.Frame(window,bg='red')
frame_2.grid(row=0,column=1,padx=5,pady=5)
btn_4u=tk.Button(frame_2,text=' ',height=1,width=4,bg='light blue')
btn_4u.pack(side=tk.TOP,padx=5,pady=20)
btn_4d=tk.Button(frame_2,text='v',height=1,width=4,bg='light blue',command=request_4_down)
btn_4d.pack(side=tk.TOP,padx=5,pady=20)
btn_3u=tk.Button(frame_2,text='^',height=1,width=4,bg='light blue',command=request_3_up)
btn_3u.pack(side=tk.TOP,padx=5,pady=20)
btn_3d=tk.Button(frame_2,text='v',height=1,width=4,bg='light blue',command=request_3_down)
btn_3d.pack(side=tk.TOP,padx=5,pady=20)
btn_2u=tk.Button(frame_2,text='^',height=1,width=4,bg='light blue',command=request_2_up)
btn_2u.pack(side=tk.TOP,padx=5,pady=20)
btn_2d=tk.Button(frame_2,text='v',height=1,width=4,bg='light blue',command=request_2_down)
btn_2d.pack(side=tk.TOP,padx=5,pady=20)
btn_1u=tk.Button(frame_2,text='^',height=1,width=4,bg='light blue',command=request_1_up)
btn_1u.pack(side=tk.TOP,padx=5,pady=20)
btn_1d=tk.Button(frame_2,text='v',height=1,width=4,bg='light blue',command=request_1_down)
btn_1d.pack(side=tk.TOP,padx=5,pady=20)
btn_0u=tk.Button(frame_2,text='^',height=1,width=4,bg='light blue',command=request_0_up)
btn_0u.pack(side=tk.TOP,padx=5,pady=20)
btn_0d=tk.Button(frame_2,text=' ',height=1,width=4,bg='light blue')
btn_0d.pack(side=tk.TOP,padx=5,pady=20)

frame_3=tk.Frame(window,bg='red')
frame_3.grid(row=0,column=2,padx=5,pady=5)
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
btn_go=tk.Button(frame_3,text='Go',bg='yellow',command=start_moving)
btn_go.grid(row=2,column=1, padx=5,pady=5)
progress_text=tk.Text(frame_3,width=15,height=20)
progress_text.grid(row=3,column=0,columnspan=2,padx=5,pady=5)


update_position()    

window.mainloop()