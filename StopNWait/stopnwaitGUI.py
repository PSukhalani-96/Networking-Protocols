from tkinter import *
from tkinter import ttk
import subprocess
import time
import pickle
import os

canvas1 = ""
i = 2
text = ""
status = ""
text_resend = ""
f = open('b.txt','rb')
txt = ""
timeout = ""
timer = 20
send_window, receive_window = '',''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sender() :
    global txt3_canvas
    canvas.itemconfig(txt3_canvas,fill="light yellow")
    canvas.delete(txt3_canvas)
    os.system("gnome-terminal -- python3 StopNWaitsender.py")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def receiver() :
    global txt2_canvas
    canvas.itemconfig(txt2_canvas,fill="light yellow")
    canvas.delete(txt2_canvas)
    os.system("gnome-terminal -- python3 StopNWaitReceiver.py")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Exit_window() :
    exit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def animation() :
    global txt1_canvas
    canvas.itemconfig(txt1_canvas,fill="light yellow")
    canvas.delete(txt1_canvas)

    global txt4_canvas
    canvas.itemconfig(txt4_canvas,fill="light yellow")
    canvas.delete(txt4_canvas)

    canvas.create_text(300,285,text = "Sender", fill = 'black' , font = ('calibri',12))
    canvas.create_text(1000,285,text = "Receiver", fill = 'black' , font = ('calibri',12))

    rect1 = canvas.create_rectangle(280,130,320,200,fill = 'white')
    line1 = canvas.create_line(280,175,320,175)
    text1 = canvas.create_text(300,157,text="SeqNo",fill="red")
    text2 = canvas.create_text(300,188,text="Info",fill="red")
    

    canvas.create_text(300 ,210 ,text = "S(n)" ,font = ('calibri',10)) 
    canvas.create_text(370 ,220 ,text = '[Next Frame\n to send]' ,font = ('calibri',12))

    canvas.create_rectangle(280, 240, 320, 270, width = 3, fill = 'light blue')
    canvas.create_line(300 ,220 ,300, 240)
    canvas.create_line(295 ,235 ,300 ,240)
    canvas.create_line(300 ,240 ,306 ,234)
    canvas.create_text(300,255,text="SeqNo",fill="red",font = ('calibri',8))

    canvas.create_text(1000, 210, text = "R(n)" , font = ('calibri',10))
    canvas.create_text(1070 ,220 ,text = '[Next Frame\n to receive]' ,font = ('calibri',12))

    canvas.create_rectangle(980, 240, 1020, 270, width = 3, fill = 'light blue')
    canvas.create_line(1000 ,220 ,1000, 240)
    canvas.create_line(995 ,235 ,1000 ,240)
    canvas.create_line(1000 ,240 ,1006 ,234)
    canvas.create_text(1000,255,text="ACK",fill="red",font = ('calibri',8))
    
    canvas.create_rectangle(250, 300, 350, 350, width = 5, fill = 'red')
    canvas.create_rectangle(250, 350, 350, 400, width = 5, fill = 'yellow')
    canvas.create_rectangle(250, 400, 350, 450, width = 5, fill = 'red')

    canvas.create_text(200,320,text = "Network", fill = 'black' , font = ('calibri',15))
    canvas.create_text(200,375,text = "Data Link", fill = 'black' , font = ('calibri',15))
    canvas.create_text(200,425,text = "Physical", fill = 'black' , font = ('calibri',15))

    canvas.create_text(278, 430, text="Receive\n Frame", fill='black', font=('calibri',10))
    canvas.create_line(275, 385, 275, 415, fill='black')
    canvas.create_line(270, 390, 275, 385, fill='black')
    canvas.create_line(275, 385, 281, 391, fill='black')

    canvas.create_text(332, 320, text=" Get\nData", fill='black', font=('calibri',10))
    canvas.create_line(335, 335, 335, 365, fill='black')
    canvas.create_line(330, 360, 335, 365, fill='black')
    canvas.create_line(335, 365, 340, 360, fill='black')

    canvas.create_text(330, 430, text=" Send\nFrame", fill='black', font=('calibri',10))
    canvas.create_line(335, 385, 335, 415, fill='black')
    canvas.create_line(330, 410, 335, 415, fill='black')
    canvas.create_line(335, 415, 340, 410, fill='black')


    canvas.create_rectangle(950, 300, 1050, 350, width = 5, fill = 'red')
    canvas.create_rectangle(950, 350, 1050, 400, width = 5, fill = 'yellow')
    canvas.create_rectangle(950, 400, 1050, 450, width = 5, fill = 'red')

    canvas.create_text(1100,320,text = "Network", fill = 'black' , font = ('calibri',15))
    canvas.create_text(1100,375,text = "Data Link", fill = 'black' , font = ('calibri',15))
    canvas.create_text(1100,425,text = "Physical", fill = 'black' , font = ('calibri',15))

    canvas.create_text(974, 320, text="Deliver\n Data", fill='black', font=('calibri',10))
    canvas.create_line(970, 335, 970, 365, fill='black')
    canvas.create_line(965, 340, 970, 335, fill='black')
    canvas.create_line(970, 335, 976, 341, fill='black')

    canvas.create_text(975, 430, text="Receive\n Frame", fill='black', font=('calibri',10))
    canvas.create_line(970, 385, 970, 415, fill='black')
    canvas.create_line(965, 390, 970, 385, fill='black')
    canvas.create_line(970, 385, 976, 391, fill='black')

    canvas.create_text(1030, 430, text=" Send\nFrame", fill='black', font=('calibri',10))
    canvas.create_line(1035, 385, 1035, 415, fill='black')
    canvas.create_line(1030, 410, 1035, 415, fill='black')
    canvas.create_line(1035, 415, 1040, 410, fill='black')

    canvas.create_line(270, 450, 270, 500, fill = 'black')
    canvas.create_line(270, 500, 1030, 500, fill = 'black')
    canvas.create_line(1030, 500, 1030, 450, fill = 'black')

    canvas.create_line(330, 450, 330, 465, fill = 'black')
    canvas.create_line(330, 465, 970, 465, fill = 'black')
    canvas.create_line(970, 465, 970, 450, fill = 'black')

    for i in range(0,250,2) :
        y = 2
        time.sleep(0.005)
        canvas.move(rect1,0,y)
        canvas.move(line1,0,y)
        canvas.move(text1,0,y)
        canvas.move(text2,0,y)
        canvas.update()

    canvas.itemconfig(text1,fill="light yellow")
    canvas.delete(text1)
    canvas.itemconfig(text2,fill="light yellow")
    canvas.delete(text2)

    rect1 = canvas.create_rectangle(330,410,400,450,fill = 'white')
    line1 = canvas.create_line(360,410,360,450)
    text1 = canvas.create_text(380,428,text="SeqNo",fill="red")
    text2 = canvas.create_text(345,430,text="Info",fill="red")
    
    for i in range(0,600,2):
        x = 2
        time.sleep(0.025)
        canvas.move(rect1,x,0)
        canvas.move(line1,x,0)
        canvas.move(text1,x,0)
        canvas.move(text2,x,0)
        canvas.update()
    canvas.itemconfig(rect1,fill="light yellow")
    canvas.delete(rect1)
    canvas.itemconfig(line1,fill="light yellow")
    canvas.delete(line1)
    canvas.itemconfig(text1,fill="light yellow")
    canvas.delete(text1)
    canvas.itemconfig(text2,fill="light yellow")
    canvas.delete(text2)
    

    rect1 = canvas.create_rectangle(980,410,1020,480,fill = 'white')
    line1 = canvas.create_line(980,450,1020,450)
    text1 = canvas.create_text(1000,420,text="SeqNo",fill="red")
    text2 = canvas.create_text(1000,465,text="Info",fill="red")

    for i in range(0,240,2) :
        y = -2
        time.sleep(0.025)
        canvas.move(rect1,0,y)
        canvas.move(line1,0,y)
        canvas.move(text1,0,y)
        canvas.move(text2,0,y)
        canvas.update()
    canvas.itemconfig(rect1,fill="light yellow")
    canvas.delete(rect1)
    canvas.itemconfig(line1,fill="light yellow")
    canvas.delete(line1)
    canvas.itemconfig(text1,fill="light yellow")
    canvas.delete(text1)
    canvas.itemconfig(text2,fill="light yellow")
    canvas.delete(text2)

    rect2 = canvas.create_rectangle(980,375,1010,425,fill = 'white')
    text1 = canvas.create_text(995,400,text="ACK",fill='red')
    for i in range(0,50,2) :
        y = 2
        time.sleep(0.025)
        canvas.move(rect2,0,y)
        canvas.move(text1,0,y)
        canvas.update()
        
    canvas.itemconfig(rect2,fill="light yellow")
    canvas.delete(rect2)
    canvas.itemconfig(text1,fill="light yellow")
    canvas.delete(text1)

    
    rect2 = canvas.create_rectangle(960,468,1010,498,fill = 'white')
    text1 = canvas.create_text(985,483,text="ACK",fill='red')
    for i in range(0,650,2) :
        x = -2
        time.sleep(0.025)
        canvas.move(rect2,x,0)
        canvas.move(text1,x,0)
        canvas.update()
    
    canvas.itemconfig(rect1,fill="light yellow")
    canvas.delete(rect2)
    canvas.itemconfig(text1,fill="light yellow")
    canvas.delete(text1)
    
    rect2 = canvas.create_rectangle(290,410,320,460,fill = 'white')
    text1 = canvas.create_text(305,435,text="ACK",fill='red')
    for i in range(0,50,2) :
        y = -2
        time.sleep(0.025)
        canvas.move(rect2,0,y)
        canvas.move(text1,0,y)
        canvas.update()

    canvas.itemconfig(rect1,fill="light yellow")
    canvas.delete(rect2)
    canvas.itemconfig(text1,fill="light yellow")
    canvas.delete(text1)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_window() :
    global canvas1
    canvas1 = Canvas(Toplevel(root),width = 1450, height = 700, bg = "light yellow")
    canvas1.pack(expand = YES, fill = BOTH)

    canvas1.create_rectangle(400,60,500,90,fill='white')
    canvas1.create_line(450,60,450,90)
    canvas1.create_text(425,75, text="Info", fill='black', font=('calibri',10))
    canvas1.create_text(475,75, text="SeqNo", fill='black', font=('calibri',10))


    canvas1.create_rectangle(900,60,960,90,fill='white')
    canvas1.create_text(930,75,text="ACK",fill='black',font=('calibri',12))
    canvas1.create_text(1120,75,text="[ Structure Of the Acknowledgement ]",fill='black',font=('calibri',12))
    
    canvas1.create_text(610,75,text="[ Structure Of the frame ]",fill='black',font=('calibri',12))
    canvas1.create_rectangle(310,120,330,640,fill='black')
    canvas1.create_rectangle(1000,120,1020,640,fill='black')
    canvas1.create_text(250,150, text="Sender", fill='blue', font=('calibri',15))
    canvas1.create_text(1070,150, text="Receiver", fill='blue', font=('calibri',15))

    canvas1.create_rectangle(230,170,260,200,fill="white")
    canvas1.create_rectangle(1060,170,1090,200,fill="white")

    but1 = Button(canvas1,text = 'Resend Frame',command = create_windows3)
    but1.place(x = 520,y=500)

    but4 = Button(canvas1,text = 'Send Frame',command = file_reading)
    but4.place(x = 650,y=500)

    but3 = Button(canvas1,text = "Quit",command = Exit_window)
    but3.place(x = 580, y=600)



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def file_reading() :
    global status
    global i
    global f,send_window,recieve_window
    global text, timeout
    canvas1.itemconfig(text,fill="light yellow")
    canvas1.delete(text)
    canvas1.itemconfig(timeout,fill="light yellow")
    canvas1.delete(timeout)
    
    
    
    i = 2
    try :
        
        status = pickle.load(f)
        print(status)
        create_windows2()
    except :
        f.close()
        return 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def create_windows3():
    global text
    global i
    global text_resend,timeout
    canvas1.itemconfig(text,fill="light yellow")
    canvas1.delete(text)
    canvas1.itemconfig(timeout,fill="light yellow")
    canvas1.delete(timeout)
    canvas1.itemconfig(text_resend,fill="light yellow")
    canvas1.delete(text_resend)
    
    if len(status) > 0 and i >= len(status) :
        text_resend = canvas1.create_text(500,305, text="No Frame to Resend", fill='red', font=('calibri',15))
    create_windows2()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def create_windows2() :
    global canvas1
    global i
    global text,txt,timeout,send_window,receive_window
    global text_resend,timer
    
    canvas1.itemconfig(send_window,fill="light yellow")
    canvas1.delete(send_window)
    canvas1.itemconfig(receive_window,fill="light yellow")
    canvas1.delete(receive_window)

    if  i < len(status) :  
        rect = canvas1.create_rectangle(350,140,420,170,fill='white')
        line = canvas1.create_line(395,140,395,170)
            
        seqNo = status[0]
        info = status[1]
        text1 = canvas1.create_text(375,155, text=info, fill='black', font=('calibri',10))
        text2 = canvas1.create_text(405,155, text=seqNo, fill='black', font=('calibri',10))

        timer = 20
        canvas1.delete(txt)

        ack = (seqNo+1)%2
    
        send_window = canvas1.create_text(245,185, text = str(seqNo))
        receive_window = canvas1.create_text(1075,185, text = str(ack))
        
        canvas1.create_circle(150,300,30, outline = 'blue')
        txt = canvas1.create_text(150,300, text=timer, font = ('calibri',15))

        
        if status[i] == 'Frame Lost' :
            start = 18
            for j in range(0,380,2):
                x = 2
                y = 0.5
                time.sleep(0.005)
                canvas1.move(rect,x,y)
                canvas1.move(line,x,y)
                canvas1.move(text1,x,y)
                canvas1.move(text2,x,y)
                canvas1.update()
                if j == start :
                    time.sleep(0.005)
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                    start += 20

            #time.sleep(0.005)
            if timer != 0 :
                
                timer -= 1
                canvas1.delete(txt)
                txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))

            canvas1.itemconfig(rect,fill="light yellow")
            canvas1.delete(rect)
            canvas1.itemconfig(line,fill="light yellow")
            canvas1.delete(line)
            canvas1.itemconfig(text1,fill="light yellow")
            canvas1.delete(text1)
            canvas1.itemconfig(text2,fill="light yellow")
            canvas1.delete(text2)
            text = canvas1.create_text(800,300, text="FRAME LOST", fill='red', font=('calibri',15))  
            timeout = canvas1.create_text(800,350, text="TIMEOUT", fill='red', font=('calibri',15))
              
        elif status[i] == 'Acknowledgement Lost' :

            start = 58
            for j in range(0,580,2):
                x = 2
                y = 0.25
                time.sleep(0.005)
                canvas1.move(rect,x,y)
                canvas1.move(line,x,y)
                canvas1.move(text1,x,y)
                canvas1.move(text2,x,y)
                canvas1.update()

                if j == start :
                    time.sleep(0.005)
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                    start += 58
            time.sleep(0.05)        
            canvas1.itemconfig(rect,fill="light yellow")
            canvas1.delete(rect)
            canvas1.itemconfig(line,fill="light yellow")
            canvas1.delete(line)
            canvas1.itemconfig(text1,fill="light yellow")
            canvas1.delete(text1)
            canvas1.itemconfig(text2,fill="light yellow")
            canvas1.delete(text2)
            rect1 = canvas1.create_rectangle(935,205,995,235,fill='white')
            ack = (seqNo+1)%2
            txt1 = canvas1.create_text(965,220, text=ack, fill='black', font=('calibri',14))
            start = 30
            
            time.sleep(0.5)
            for j in range(0,300,2):
                x = -2
                y = 0.5
                time.sleep(0.005)
                canvas1.move(rect1,x,y)
                canvas1.move(txt1,x,y)
                canvas1.update()
                if j == start :
                    time.sleep(0.005)
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                    start += 30
                time.sleep(0.05)
                
                if j == 278 or j == 284 :
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                    
            canvas1.itemconfig(rect1,fill="light yellow")
            canvas1.delete(rect1)
            canvas1.itemconfig(txt1,fill="light yellow")
            canvas1.delete(txt1)    
            text = canvas1.create_text(600,305, text="ACKNOWLEDGEMENT LOST", fill='red', font=('calibri',13))
                

        elif status[i] == 'Timeout' :
            start = 58
            for j in range(0,580,2):
                x = 2
                y = 0.5
                time.sleep(0.005)
                canvas1.move(rect,x,y)
                canvas1.move(line,x,y)
                canvas1.move(text1,x,y)
                canvas1.move(text2,x,y)
                canvas1.update()

                if j == start :
                    time.sleep(0.005)
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                    start += 58
            time.sleep(0.5)        
            canvas1.itemconfig(rect,fill="light yellow")
            canvas1.delete(rect)
            canvas1.itemconfig(line,fill="light yellow")
            canvas1.delete(line)
            canvas1.itemconfig(text1,fill="light yellow")
            canvas1.delete(text1)
            canvas1.itemconfig(text2,fill="light yellow")
            canvas1.delete(text2)
            rect1 = canvas1.create_rectangle(935,205,995,235,fill='white')
            ack = (seqNo+1)%2
            txt1 = canvas1.create_text(965,220, text=ack, fill='black', font=('calibri',14))
            
            start = 30
            for j in range(0,300,2):
                x = -1
                y = 0.5
                time.sleep(0.005)
                canvas1.move(rect1,x,y)
                canvas1.move(txt1,x,y)
                canvas1.update()

                if j == start :
                    time.sleep(0.005)
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                    start += 30
                time.sleep(0.05)
                if j == 278 or j == 284 :
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))

            time.sleep(0.05)
            text = canvas1.create_text(600,400, text="TIMEOUT", fill='red', font=('calibri',13))
            canvas1.itemconfig(rect1,fill="light yellow")
            canvas1.delete(rect1)
            canvas1.itemconfig(txt,fill="light yellow")
            canvas1.delete(txt1) 

        elif status[i] == 'Acknowledgement Received' :
            
            start = 58
            for j in range(0,580,2):
                x = 2
                y = 0.25
                time.sleep(0.005)
                canvas1.move(rect,x,y)
                canvas1.move(line,x,y)
                canvas1.move(text1,x,y)
                canvas1.move(text2,x,y)
                canvas1.update()
                if j == start :

                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                    start += 58

            time.sleep(0.05)
            
            canvas1.itemconfig(rect,fill="light yellow")
            canvas1.delete(rect)
            canvas1.itemconfig(line,fill="light yellow")
            canvas1.delete(line)
            canvas1.itemconfig(text1,fill="light yellow")
            canvas1.delete(text1)
            canvas1.itemconfig(text2,fill="light yellow")
            canvas1.delete(text2)
            rect1 = canvas1.create_rectangle(935,205,995,235,fill='white')
            ack = (seqNo+1)%2
            txt1 = canvas1.create_text(965,220, text=ack, fill='black', font=('calibri',14))
            time.sleep(1)
            start = 58
            for j in range(0,580,2):
                x = -2
                y = 0.5
                time.sleep(0.005)
                canvas1.move(rect1,x,y)
                canvas1.move(txt1,x,y)
                canvas1.update()
                if j == start :
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                    start += 58

                if j == 278 or j == 284 :
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                    
            time.sleep(0.05)        
            canvas1.itemconfig(rect1,fill="light yellow")
            canvas1.delete(rect1)
            canvas1.itemconfig(txt,fill="light yellow")
            canvas1.delete(txt1)    
            text = canvas1.create_text(500,305, text="ACKNOWLEDGEMENT RECEIVED SUCCESSFULLY", fill='green', font=('calibri',13))
            
        i+=1


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title("Stop and Wait Protocol")
canvas = Canvas(root,width = 1450, height = 700, bg = "light yellow")
canvas.pack(expand = YES, fill = BOTH)

button1 = Button(root,text = "Activate Reciver's Site",command = receiver)
button2 = Button(root,text = "Activate Sender's Site",command = sender)
button3 = Button(root,text = "Start Animation",command = animation)
button1.place(x=200,y=50)
button2.place(x=600,y=50)
button3.place(x=1000,y=50)

button4 = Button(canvas, text = 'Request to send ',command = create_window)
button4.place(x=580,y=600)

txt1_canvas = canvas.create_text(650,150,text = "Follow the following steps",fill="black",font=('calibri',20))
txt2_canvas = canvas.create_text(600,230,text = "(I) Äctivate Receiver's Site Button, to create connection between sender and receiver ",fill='blue',font = ('calibri',20))
txt3_canvas = canvas.create_text(480,310,text = "(II) Äctivate Sender's Site Button, to send frames to receiver",fill = 'green',font = ('calibri',20))
txt4_canvas = canvas.create_text(600,390,text = "(III) Click Start Animation to understand the flow of frames in Stop and wait Protocol",font = ('calibri',20))
 
mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
