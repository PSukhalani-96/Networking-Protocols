from tkinter import *
from tkinter import ttk
import time
import pickle
import os

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

canvas1 = ""
i = 2
text = ""
status = ""
text_resend = ""
f = open('l.txt','rb')
windows1 = ''
windowr2 = ''
text_data1 = ''
text_data2 = ''
text_data3 = ''
text_data4 = ''
text_data5 = ''
text_data6 = ''
text_data7 = ''
timer = 20
txt = ''
frames = []
done = False
prev_seq = 0
size = 0
duplicate = []


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sender() :
    global txt3_canvas
    canvas.itemconfig(txt3_canvas,fill="light yellow")
    canvas.delete(txt3_canvas)
    os.system("gnome-terminal -- python3 GoBackNSender.py")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def receiver() :
    global txt2_canvas
    canvas.itemconfig(txt2_canvas,fill="light yellow")
    canvas.delete(txt2_canvas)
    os.system("gnome-terminal -- python3 GoBackNReceiver.py")
    
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
    global windows1,windowr2
    global frames
    
    canvas1 = Canvas(Toplevel(root),width = 1450, height = 700, bg = "light yellow")
    canvas1.pack(expand = YES, fill = BOTH)

    canvas1.create_rectangle(400,60,500,90,fill='white')
    canvas1.create_text(450,75, text="SeqNo", fill='black', font=('calibri',13))


    canvas1.create_rectangle(900,60,960,90,fill='white')
    canvas1.create_text(930,75,text="ACK",fill='black',font=('calibri',12))
    canvas1.create_text(1120,75,text="[ Structure Of the Acknowledgement ]",fill='black',font=('calibri',12))
    
    canvas1.create_text(610,75,text="[ Structure Of the frame ]",fill='black',font=('calibri',12))
    canvas1.create_rectangle(300,120,320,640,fill='black')
    canvas1.create_rectangle(1000,120,1020,640,fill='black')
    canvas1.create_text(250,150, text="Sender", fill='blue', font=('calibri',15))
    canvas1.create_text(1070,150, text="Receiver", fill='blue', font=('calibri',15))

    windows1 = canvas1.create_rectangle(40,190,100,240,fill = "white")
    canvas1.create_rectangle(40,200,280,230,fill = "white")
    
    windowr2 = canvas1.create_rectangle(1040,190,1055,240,fill = "white")
    canvas1.create_rectangle(1040,200,1280,230,fill = "white")
    

    canvas1.create_text(48,215,text = "0",font = ('calibri',8))
    for i in range(1,16) :
        canvas1.create_line(40+(15*i),200,40+(15*i),230)
        content = i % 8
        canvas1.create_text(48+(15*i),215,text = str(content),font = ('calibri',8))    

    canvas1.create_text(1048,215,text = "0",font = ('calibri',8))
    for i in range(1,16) :
        canvas1.create_line(1040+(15*i),200,1040+(15*i),230)
        content = i % 8
        canvas1.create_text(1048 + (15*i),215,text = str(content), font = ('calibri',8))
       

    but4 = Button(canvas1,text = 'Send Frame',command = file_reading)
    but4.place(x = 540,y=600)

    but3 = Button(canvas1,text = "Quit",command = Exit_window)
    but3.place(x = 690, y=600)



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def file_reading() :
    global status
    global i
    global f
    global text,duplicate
    global text_data1,text_data2,text_data3,text_data4,text_data5,text_data6,text_data7
    canvas1.itemconfig(text,fill="light yellow")
    canvas1.delete(text)
    
    
    canvas1.itemconfig(text_data1,fill="light yellow")
    canvas1.delete(text_data1)
    canvas1.itemconfig(text_data2,fill="light yellow")
    canvas1.delete(text_data2)
    canvas1.itemconfig(text_data3,fill="light yellow")
    canvas1.delete(text_data3)
    canvas1.itemconfig(text_data4,fill="light yellow")
    canvas1.delete(text_data4)
    canvas1.itemconfig(text_data5,fill="light yellow")
    canvas1.delete(text_data5)
    canvas1.itemconfig(text_data6,fill="light yellow")
    canvas1.delete(text_data6)
    canvas1.itemconfig(text_data7,fill="light yellow")
    canvas1.delete(text_data7)
    i = 4
    try :
        global duplicate
        status = pickle.load(f)
        print(status)
        create_windows2()
    except :
        
        f.close()
        return 



    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def create_windows2() :
    global canvas1
    global i
    global text_data1,text_data2,text_data3,text_data4,text_data5,text_data6,text_data7
    global windows1,windowr2
    global size,timer,txt
    global prev_seq

    seq0, seq1, seq2, seq3 = '','','',''
    seq_No = []
    
    if (16 - size >= 4 ) :
        seq0 = status[0]
        seq1 = status[1]
        seq2 = status[2]
        seq3 = status[3]
        

    elif ( 16 - size < 4 ) :

        
        length = 0
        
        if status[len(status)-1][0] == 'Timeout' :
            length = len(status) - 2
        else :
            length = len(status) - 1
        
        for i in range(length) :
            seq_No.append(status[i])
        for i in range(length,4) :
            seq_No.append(10)
                
        seq0 = seq_No[0]
        seq1 = seq_No[1]
        seq2 = seq_No[2]
        seq3 = seq_No[3]

        i = length
    
    timer = 20
    canvas1.delete(txt)
    
    
    rect1 = canvas1.create_rectangle(340,140,390,170,fill = 'white')
    rect2 = canvas1.create_rectangle(340,180,390,210,fill = 'white')
    rect3 = canvas1.create_rectangle(340,220,390,250,fill = 'white')
    rect4 = canvas1.create_rectangle(340,260,390,290,fill = 'white')
    
    text1 = canvas1.create_text(365,155, text=seq0, fill='black', font=('calibri',10))
    text2 = canvas1.create_text(365,195, text=seq1, fill='black', font=('calibri',10))
    text3 = canvas1.create_text(365,235, text=seq2, fill='black', font=('calibri',10))
    text4 = canvas1.create_text(365,275, text=seq3, fill='black', font=('calibri',10))

    prev_seq = int(seq0)

    canvas1.create_circle(150,300,30, outline = 'blue')
    txt = canvas1.create_text(150,300, text=timer, font = ('calibri',15))
    
    global duplicate
    if i < len(status) :

        if status[i][0] == 'Acknowledgement Lost' :
            rect_value = status[i][1]
            duplicate = []
            for j in range(0,600,2) :
                y = 0.5
                x = 2
                
                time.sleep(0.05)
                canvas1.move(rect1,x,y)
                canvas1.move(rect2,x,y)
                canvas1.move(rect3,x,y)
                canvas1.move(rect4,x,y)
                canvas1.move(text1,x,y)
                canvas1.move(text2,x,y)
                canvas1.move(text3,x,y)
                canvas1.move(text4,x,y)
                canvas1.update()

                if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590 :
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))

                

            for  j in range(4) :
                if size < 16 :
                    time.sleep(0.05)
                    canvas1.move(windowr2,15,0)
                    canvas1.update() 
            
            
            for j in range(0,600,2) :
                y = 0.5
                x = -2
                x1 = -0.5
                if rect_value == seq0 :
                    time.sleep(0.05)
                    canvas1.move(rect1,x1,y)
                    canvas1.move(rect2,x,y)
                    canvas1.move(rect3,x,y)
                    canvas1.move(rect4,x,y)
                    canvas1.move(text1,x1,y)
                    canvas1.move(text2,x,y)
                    canvas1.move(text3,x,y)
                    canvas1.move(text4,x,y)
                    canvas1.update()
                    
                elif rect_value == seq1 :
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(rect2,x1,y)
                    canvas1.move(rect3,x,y)
                    canvas1.move(rect4,x,y)
                    canvas1.move(text1,x,y)
                    canvas1.move(text2,x1,y)
                    canvas1.move(text3,x,y)
                    canvas1.move(text4,x,y)
                    canvas1.update()
                    
                elif rect_value == seq2 :
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(rect2,x,y)
                    canvas1.move(rect3,x1,y)
                    canvas1.move(rect4,x,y)
                    canvas1.move(text1,x,y)
                    canvas1.move(text2,x,y)
                    canvas1.move(text3,x1,y)
                    canvas1.move(text4,x,y)
                    canvas1.update()
                    
                else :
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(rect2,x,y)
                    canvas1.move(rect3,x,y)
                    canvas1.move(rect4,x1,y)
                    canvas1.move(text1,x,y)
                    canvas1.move(text2,x,y)
                    canvas1.move(text3,x,y)
                    canvas1.move(text4,x1,y)
                    canvas1.update()
                    

                if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))

            print("The value of rect is : ", rect_value)
            print("Value of seq0 : ", seq0)
            print("Value of seq1 : ", seq1)
            print("Value of seq2 : ", seq2)
            print("Value of seq3 : ", seq3)
            
            if rect_value == seq2 or rect_value == seq1 or rect_value == seq0:
                time.sleep(0.05)
                canvas1.move(windows1,60,0)
                canvas1.update()
                duplicate.extend([seq3])
                text_data2 = canvas1.create_text(530,450, text = "Frames will not be resent...as Acknowledgement of Frame  "+str(seq2)+" is received.", fill = 'green', font=('calibri',14))
                # text_data2 = canvas1.create_text(530,450, text = "Frames from sequence number "+str(rect_value)+" will be resend", fill = 'green', font=('calibri',14))
                size += 4
            
            elif rect_value == seq3 :
                time.sleep(0.05)
                canvas1.move(windows1,45,0)
                canvas1.update()
                size += 3
                # text_data2 = canvas1.create_text(530,450, text = "Frames from sequence number "+str(rect_value)+" will be resend", fill = 'green', font=('calibri',14))
            
            text_data1 = canvas1.create_text(500,350, text = "Acknowledgement of frame "+str(rect_value)+" is lost", fill = 'green', font=('calibri',14))      
            # text_data2 = canvas1.create_text(530,450, text = "Frames from sequence number "+str(rect_value)+" will be resend", fill = 'green', font=('calibri',14))
            i += 1
            
        elif status[i][0] == 'Acknowledgement Received' :
            timer = 20
            for j in range(0,600,2) :
                y = 0.5
                x = 2
                
                time.sleep(0.05)
                canvas1.move(rect1,x,y)
                canvas1.move(rect2,x,y)
                canvas1.move(rect3,x,y)
                canvas1.move(rect4,x,y)
                canvas1.move(text1,x,y)
                canvas1.move(text2,x,y)
                canvas1.move(text3,x,y)
                canvas1.move(text4,x,y)
                canvas1.update()

                if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))

            
            for  j in range(4-len(duplicate)) :
                time.sleep(0.05)
                canvas1.move(windowr2,15,0)
                canvas1.update()
                
            
                                   
            for j in range(0,600,2) :
                y = 0.5
                x = -2
                
                time.sleep(0.05)
                canvas1.move(rect1,x,y)
                canvas1.move(rect2,x,y)
                canvas1.move(rect3,x,y)
                canvas1.move(rect4,x,y)
                canvas1.move(text1,x,y)
                canvas1.move(text2,x,y)
                canvas1.move(text3,x,y)
                canvas1.move(text4,x,y)
                canvas1.update()

                if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))


            size += 4 
            
            for  j in range(4) :
                time.sleep(0.05)
                canvas1.move(windows1,15,0)
                canvas1.update() 
            
                
            text_data3 = canvas1.create_text(500,400, text = "All Frames Acknowledged successfully", fill = 'green', font=('calibri',14))
            i += 1
            duplicate = []

        elif status[i][0] == 'Frame Damaged' and status[i+1][0] == 'Timeout' :
            rect_value = int(status[i][1])
            print(rect_value)
            timer = 20
            for j in range(0,600,2) :
                x = 2
                y = 0.5
                time.sleep(0.05)
                canvas1.move(rect1,x,y)
                canvas1.move(rect2,x,y)
                canvas1.move(rect3,x,y)
                canvas1.move(rect4,x,y)
                canvas1.move(text1,x,y)
                canvas1.move(text2,x,y)
                canvas1.move(text3,x,y)
                canvas1.move(text4,x,y)
                canvas1.update()

                if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))


            if rect_value == seq0:
                canvas1.itemconfig(rect1,fill="light yellow")
                canvas1.delete(rect1)
                canvas1.itemconfig(text1,fill="light yellow")
                canvas1.delete(text1)
                canvas1.itemconfig(rect2,fill="light yellow")
                canvas1.delete(rect2)
                canvas1.itemconfig(text2,fill="light yellow")
                canvas1.delete(text2)
                canvas1.itemconfig(rect3,fill="light yellow")
                canvas1.delete(rect3)
                canvas1.itemconfig(text3,fill="light yellow")
                canvas1.delete(text3)
                canvas1.itemconfig(rect4,fill="light yellow")
                canvas1.delete(rect4)
                canvas1.itemconfig(text4,fill="light yellow")
                canvas1.delete(text4)
                #
                canvas1.itemconfig(text_data4,fill="light yellow")
                canvas1.delete(text_data4)
                canvas1.itemconfig(text_data5,fill="light yellow")
                canvas1.delete(text_data5)

            elif rect_value == seq1:
                time.sleep(0.05)
                canvas1.move(windowr2,15,0)
                canvas1.update()  

                canvas1.itemconfig(rect2,fill="light yellow")
                canvas1.delete(rect2)
                canvas1.itemconfig(text2,fill="light yellow")
                canvas1.delete(text2)
                canvas1.itemconfig(rect3,fill="light yellow")
                canvas1.delete(rect3)
                canvas1.itemconfig(text3,fill="light yellow")
                canvas1.delete(text3)
                canvas1.itemconfig(rect4,fill="light yellow")
                canvas1.delete(rect4)
                canvas1.itemconfig(text4,fill="light yellow")
                canvas1.delete(text4)
                canvas1.itemconfig(text_data4,fill="light yellow")
                canvas1.delete(text_data4)
                canvas1.itemconfig(text_data5,fill="light yellow")
                canvas1.delete(text_data5)
                for j in range(0,600,2) :
                    x = -2
                    y = 0.5
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(text1,x,y)
                    canvas1.update()
                    if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                        timer -= 1
                        canvas1.delete(txt)
                        txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))


                time.sleep(0.05)
                canvas1.move(windows1,15,0)
                canvas1.update()
                size += 1
                
            elif rect_value == seq2:
                time.sleep(0.05)
                canvas1.move(windowr2,30,0)
                canvas1.update() 
                canvas1.itemconfig(rect3,fill="light yellow")
                canvas1.delete(rect3)
                canvas1.itemconfig(text3,fill="light yellow")
                canvas1.delete(text3)
                canvas1.itemconfig(rect4,fill="light yellow")
                canvas1.delete(rect4)
                canvas1.itemconfig(text4,fill="light yellow")
                canvas1.delete(text4)
                canvas1.itemconfig(text_data4,fill="light yellow")
                canvas1.delete(text_data4)
                canvas1.itemconfig(text_data5,fill="light yellow")
                canvas1.delete(text_data5)
                for j in range(0,600,2) :
                    x = -2
                    y = 0.5
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(text1,x,y)
                    canvas1.move(rect2,x,y)
                    canvas1.move(text2,x,y)
                    canvas1.update()

                    if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                        timer -= 1
                        canvas1.delete(txt)
                        txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                        
                time.sleep(0.05)
                canvas1.move(windows1,30,0)
                canvas1.update()
                size += 2
                
            else :
                time.sleep(0.05)
                canvas1.move(windowr2,45,0)
                canvas1.update() 
                canvas1.itemconfig(rect4,fill="light yellow")
                canvas1.delete(rect4)
                canvas1.itemconfig(text4,fill="light yellow")
                canvas1.delete(text4)
                canvas1.itemconfig(text_data4,fill="light yellow")
                canvas1.delete(text_data4)
                canvas1.itemconfig(text_data5,fill="light yellow")
                canvas1.delete(text_data5)
                for j in range(0,600,2) :
                    x = -2
                    y = 0.5
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(text1,x,y)
                    canvas1.move(rect2,x,y)
                    canvas1.move(text2,x,y)
                    canvas1.move(rect3,x,y)
                    canvas1.move(text3,x,y)
                    canvas1.update()
                    if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                        timer -= 1
                        canvas1.delete(txt)
                        txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                time.sleep(0.05)
                canvas1.move(windows1,45,0)
                canvas1.update()
                size += 3
                    
            text_data7 = canvas1.create_text(500,400, text = "Frames "+str(rect_value)+" is Damaged.", fill = 'green', font=('calibri',14))
            text_data6 = canvas1.create_text(600,440, text = "TIMEOUT", fill = 'red', font=('calibri',12))
            i += 2

        elif status[i][0] == 'Frame Lost' and status[i+1][0] == 'Timeout' :
            rect_value = int(status[i][1])
            for j in range(0,600,2) :
                y = 0.5
                x = 2
                x1 = 0.5
                if rect_value == int(seq0) :
                    time.sleep(0.05)
                    canvas1.move(rect1,x1,y)
                    canvas1.move(rect2,x,y)
                    canvas1.move(rect3,x,y)
                    canvas1.move(rect4,x,y)
                    canvas1.move(text1,x1,y)
                    canvas1.move(text2,x,y)
                    canvas1.move(text3,x,y)
                    canvas1.move(text4,x,y)
                    canvas1.update()

                elif rect_value == int(seq1) :
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(rect2,x1,y)
                    canvas1.move(rect3,x,y)
                    canvas1.move(rect4,x,y)
                    canvas1.move(text1,x,y)
                    canvas1.move(text2,x1,y)
                    canvas1.move(text3,x,y)
                    canvas1.move(text4,x,y)
                    canvas1.update()

                elif rect_value == int(seq2) :
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(rect2,x,y)
                    canvas1.move(rect3,x1,y)
                    canvas1.move(rect4,x,y)
                    canvas1.move(text1,x,y)
                    canvas1.move(text2,x,y)
                    canvas1.move(text3,x1,y)
                    canvas1.move(text4,x,y)
                    canvas1.update()

                    
                else :
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(rect2,x,y)
                    canvas1.move(rect3,x,y)
                    canvas1.move(rect4,x1,y)
                    canvas1.move(text1,x,y)
                    canvas1.move(text2,x,y)
                    canvas1.move(text3,x,y)
                    canvas1.move(text4,x1,y)
                    canvas1.update()

                if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                    timer -= 1
                    canvas1.delete(txt)
                    txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
   
            if rect_value == int(seq1) :
                time.sleep(0.05)
                canvas1.move(windowr2,15,0)
                canvas1.update()
            elif rect_value == int(seq2):
                time.sleep(0.05)
                canvas1.move(windowr2,30,0)
                canvas1.update()
            elif rect_value == int(seq3) : 
                time.sleep(0.05)
                canvas1.move(windowr2,45,0)
                canvas1.update()

            text_data4 = canvas1.create_text(500,380, text="FRAME" + str(rect_value) + " LOST", fill='red', font=('calibri',15))
            string = "All frame starting from " + str(rect_value) + " are discarded"
            text_data5 = canvas1.create_text(600,410, text = string, fill = 'red', font=('calibri',12))
            time.sleep(2)
            
            i += 2
            
            if rect_value == seq0:
                
                canvas1.itemconfig(rect1,fill="light yellow")
                canvas1.delete(rect1)
                canvas1.itemconfig(text1,fill="light yellow")
                canvas1.delete(text1)
                canvas1.itemconfig(rect2,fill="light yellow")
                canvas1.delete(rect2)
                canvas1.itemconfig(text2,fill="light yellow")
                canvas1.delete(text2)
                canvas1.itemconfig(rect3,fill="light yellow")
                canvas1.delete(rect3)
                canvas1.itemconfig(text3,fill="light yellow")
                canvas1.delete(text3)
                canvas1.itemconfig(rect4,fill="light yellow")
                canvas1.delete(rect4)
                canvas1.itemconfig(text4,fill="light yellow")
                canvas1.delete(text4)
                #
                canvas1.itemconfig(text_data4,fill="light yellow")
                canvas1.delete(text_data4)
                canvas1.itemconfig(text_data5,fill="light yellow")
                canvas1.delete(text_data5)

                for j in range(0,600,2) :
                    if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
                        time.sleep(0.05)
                        timer -= 1
                        canvas1.delete(txt)
                        txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
                
            elif rect_value == seq1:


                canvas1.itemconfig(rect2,fill="light yellow")
                canvas1.delete(rect2)
                canvas1.itemconfig(text2,fill="light yellow")
                canvas1.delete(text2)
                canvas1.itemconfig(rect3,fill="light yellow")
                canvas1.delete(rect3)
                canvas1.itemconfig(text3,fill="light yellow")
                canvas1.delete(text3)
                canvas1.itemconfig(rect4,fill="light yellow")
                canvas1.delete(rect4)
                canvas1.itemconfig(text4,fill="light yellow")
                canvas1.delete(text4)
                canvas1.itemconfig(text_data4,fill="light yellow")
                canvas1.delete(text_data4)
                canvas1.itemconfig(text_data5,fill="light yellow")
                canvas1.delete(text_data5)
                for j in range(0,600,2) :
                    x = -2
                    y = 0.5
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(text1,x,y)
                    canvas1.update()

                    if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                        timer -= 1
                        canvas1.delete(txt)
                        txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))


                time.sleep(0.05)
                canvas1.move(windows1,15,0)
                canvas1.update()
                size += 1
                
            elif rect_value == seq2:
                
                canvas1.itemconfig(rect3,fill="light yellow")
                canvas1.delete(rect3)
                canvas1.itemconfig(text3,fill="light yellow")
                canvas1.delete(text3)
                canvas1.itemconfig(rect4,fill="light yellow")
                canvas1.delete(rect4)
                canvas1.itemconfig(text4,fill="light yellow")
                canvas1.delete(text4)
                canvas1.itemconfig(text_data4,fill="light yellow")
                canvas1.delete(text_data4)
                canvas1.itemconfig(text_data5,fill="light yellow")
                canvas1.delete(text_data5)
                for j in range(0,600,2) :
                    x = -2
                    y = 0.5
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(text1,x,y)
                    canvas1.move(rect2,x,y)
                    canvas1.move(text2,x,y)
                    canvas1.update()

                    if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                        timer -= 1
                        canvas1.delete(txt)
                        txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))


                time.sleep(0.05)
                canvas1.move(windows1,30,0)
                canvas1.update()
                size += 2
                
            else :
               
                canvas1.itemconfig(rect4,fill="light yellow")
                canvas1.delete(rect4)
                canvas1.itemconfig(text4,fill="light yellow")
                canvas1.delete(text4)
                canvas1.itemconfig(text_data4,fill="light yellow")
                canvas1.delete(text_data4)
                canvas1.itemconfig(text_data5,fill="light yellow")
                canvas1.delete(text_data5)
                for j in range(0,600,2) :
                    x = -2
                    y = 0.5
                    time.sleep(0.05)
                    canvas1.move(rect1,x,y)
                    canvas1.move(text1,x,y)
                    canvas1.move(rect2,x,y)
                    canvas1.move(text2,x,y)
                    canvas1.move(rect3,x,y)
                    canvas1.move(text3,x,y)
                    canvas1.update()

                    if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
                        timer -= 1
                        canvas1.delete(txt)
                        txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))


                time.sleep(0.05)
                canvas1.move(windows1,45,0)
                canvas1.update()
                size += 3
                
            text_data7 = canvas1.create_text(500,380, text = "Frames "+ str(rect_value)+" Lost", fill = 'green', font=('calibri',14))
            




        canvas.itemconfig(rect1,fill="light yellow")       
        canvas1.delete(rect1)
        canvas.itemconfig(rect2,fill="light yellow")       
        canvas1.delete(rect2)
        canvas.itemconfig(rect3,fill="light yellow")       
        canvas1.delete(rect3)
        canvas.itemconfig(rect4,fill="light yellow")       
        canvas1.delete(rect4)
        canvas.itemconfig(text1,fill="light yellow")       
        canvas1.delete(text1)
        canvas.itemconfig(text2,fill="light yellow")       
        canvas1.delete(text2)
        canvas.itemconfig(text3,fill="light yellow")       
        canvas1.delete(text3)
        canvas.itemconfig(text4,fill="light yellow")       
        canvas1.delete(text4)


    if size > 16 :
        canvas1.itemconfig(windows1, fill = 'light yellow')
        canvas1.delete(windows1)
        canvas1.itemconfig(windowr2, fill = 'light yellow')
        canvas1.delete(windowr2)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title("GO Back N Protocol")
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
