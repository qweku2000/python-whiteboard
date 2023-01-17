from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
import tkinter as tk


root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)

current_x = 0
current_y = 0
color = 'black'

def locate_xy(work):
    global current_x,current_y
    current_x = work.x
    current_y = work.y
    
def addline(work):
    global current_x,current_y
    canvas.create_line((current_x,current_y,work.x,work.y),width=2,fill=color) 
    current_x,current_y = work.x,work.y   
    
def show_color(new_color):    
    global color
    color = new_color
#icon

# logo = PhotoImage("./img/logo.png")
# root.iconphoto(False,logo)

color_box = PhotoImage(file="./img/color section.png")
color_box_label = Label(root,image=color_box,bg="#f2f3f5")
color_box_label.place(x=10,y=20)


eraser = PhotoImage(file="./img/eraser.png")
eraser_button = Button(root,image=eraser,bg="#f2f3f5",height=20,width=20)
eraser_button.place(x=30,y=400)


colors = Canvas(root,bg="#ffffff",width=37,height=300)
colors.place(x=30,y=60)

def display_pallete():
    id = colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('black'))
    
    id = colors.create_rectangle((10,40,30,60),fill='gray')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('gray'))
    
    id = colors.create_rectangle((10,70,30,90),fill='red')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('red'))
    
    id = colors.create_rectangle((10,100,30,120),fill='green')
    
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('green'))
    
    id = colors.create_rectangle((10,130,30,150),fill='orange')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('orange'))
    
    id = colors.create_rectangle((10,160,30,180),fill='blue')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('blue'))
    
    id = colors.create_rectangle((10,190,30,210),fill='purple')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('purple'))
    
    id = colors.create_rectangle((10,220,30,240),fill='brown')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('brown'))
    
    id = colors.create_rectangle((10,250,30,270),fill='indigo')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('indigo'))
display_pallete()    
    
    
    
    
    

canvas = Canvas(root, width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>',addline)


# slider

current_value = tk.DoubleVar()
slider = ttk.Scale(root,from=0,to=100,orient='vertical',command=slider_changed,variable=current_value)
slider.place(x=30,y=530)

# value_label



root.mainloop()





















 