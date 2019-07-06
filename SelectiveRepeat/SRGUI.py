from tkinter import *
from tkinter import ttk
import time
import pickle
import os

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

canvas1 = ""
i = 2
text = ""
status = ""
windows1, windowr2 = '' , ''
text_data1 , text_data2 = '' , ''
text_data5 = ''
text_data3 , text_data4 = '' , ''
rect1,rect2,rect3,rect4 = '','','',''
text1,text2,text3,text4 = '','','',''
txt = ''
timer = 20
size1,size2 = 0,0
f = open('the.txt','rb')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def transmission() :
    global txt1_canvas
    canvas.itemconfig(txt1_canvas,fill="light yellow")
    canvas.delete(txt1_canvas)
    # os.startfile('SR.py')
    os.system("gnome-terminal -- python3 SR.py")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def Exit_window() :
    exit()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def animation() :
    global txt2_canvas
    
    canvas.itemconfig(txt2_canvas,fill="light yellow")
    canvas.delete(txt2_canvas)

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
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_window() :
    global canvas1
    global windows1,windowr2    
    
    canvas1 = Canvas(Toplevel(root),width = 1450, height = 700, bg = "light yellow")
    canvas1.pack(expand = YES, fill = BOTH)

    canvas1.create_rectangle(400,60,500,90,fill='white')
    canvas1.create_text(450,75, text="SeqNo", fill='black', font=('calibri',13))


    canvas1.create_rectangle(900,60,960,90,fill='white')
    canvas1.create_text(930,75,text="ACK",fill='black',font=('calibri',12))
    canvas1.create_text(1120,75,text="[ Structure Of the Acknowledgement ]",fill='black',font=('calibri',12))
    
    canvas1.create_text(610,75,text="[ Structure Of the frame ]",fill='black',font=('calibri',12))
    canvas1.create_rectangle(320,120,340,640,fill='black')
    canvas1.create_rectangle(990,120,1010,640,fill='black')
    canvas1.create_text(250,150, text="Sender", fill='blue', font=('calibri',15))
    canvas1.create_text(1070,150, text="Receiver", fill='blue', font=('calibri',15))

    windows1 = canvas1.create_rectangle(40,190,100,240,fill = "white")
    canvas1.create_rectangle(40,200,280,230,fill = "white")
    
    windowr2 = canvas1.create_rectangle(1040,190,1100,240,fill = "white")
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
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def file_reading() :
    global status,i,f
    global text_data1,text_data2,text_data3,text_data4,text_data5,text_data6,text_data7
    global rect1,rect2,rect3,rect4,text1,text2,text3,text4

    canvas1.itemconfig(rect1,fill="light yellow")
    canvas1.delete(rect1)
    canvas1.itemconfig(rect2,fill="light yellow")
    canvas1.delete(rect2)
    canvas1.itemconfig(rect3,fill="light yellow")
    canvas1.delete(rect3)
    canvas1.itemconfig(rect4,fill="light yellow")
    canvas1.delete(rect4)

    canvas1.itemconfig(text1,fill="light yellow")
    canvas1.delete(text1)
    canvas1.itemconfig(text2,fill="light yellow")
    canvas1.delete(text2)
    canvas1.itemconfig(text3,fill="light yellow")
    canvas1.delete(text3)
    canvas1.itemconfig(text4,fill="light yellow")
    canvas1.delete(text4)

    canvas1.itemconfig(text_data1,fill="light yellow")
    canvas1.delete(text_data1)
    
    canvas1.itemconfig(text_data3,fill="light yellow")
    canvas1.delete(text_data3)

    canvas1.itemconfig(text_data4,fill="light yellow")
    canvas1.delete(text_data4)

    canvas1.itemconfig(text_data5,fill="light yellow")
    canvas1.delete(text_data5)

    canvas1.itemconfig(text_data2,fill="light yellow")
    canvas1.delete(text_data2)
    i = 4

    try :
        
        status = pickle.load(f)
        
        if len(status) < 8 :
            print(status)
            create_windows3()
        else :
            print(status)
            create_windows2()
    except :
        f.close()
        return 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_windows3() :
    global canvas1,i
    global text_data1,text_data2,text_data3,text_data4,text_data5,text_data6,text_data7
    global windows1,windowr2
    global rect1,rect2,rect3,rect4,rect4,text1,text2,text3,text4,txt,timer
    global size1 , size2
    
    j = 0
    seq_No = []
    for i in range(len(status)//2) :
        seq_No.append(status[i])

    rect1 = ''
    rect2 = ''
    rect3 = ''

    timer = 20
    canvas1.delete(txt)

    if len(status) == 2 :
        rect1 = canvas1.create_rectangle(340,140,390,170,fill = 'white')
        text1 = canvas1.create_text(365,155, text=str(seq_No[j]), fill='black', font=('calibri',10))

    elif len(status) == 4 :
        rect1 = canvas1.create_rectangle(340,140,390,170,fill = 'white')
        text1 = canvas1.create_text(365,155, text=str(seq_No[j]), fill='black', font=('calibri',10))
        j += 1
        rect2 = canvas1.create_rectangle(340,180,390,210,fill = 'white')
        text2 = canvas1.create_text(365,195, text=str(seq_No[j]), fill='black', font=('calibri',10))

    elif len(status) == 6 :
        rect1 = canvas1.create_rectangle(340,140,390,170,fill = 'white')
        text1 = canvas1.create_text(365,155, text=str(seq_No[j]), fill='black', font=('calibri',10))
        j += 1
        rect2 = canvas1.create_rectangle(340,180,390,210,fill = 'white')
        text2 = canvas1.create_text(365,195, text=str(seq_No[j]), fill='black', font=('calibri',10))
        j += 1
        rect3 = canvas1.create_rectangle(340,220,390,250,fill = 'white')
        text3 = canvas1.create_text(365,235, text=seq2, fill='black', font=('calibri',10))

    seq = []
    non_seq = []
    for i in range(len(status)//2,len(status)) :
        if status[i][0] == 'Frame Lost' :
            seq.append(status[i][1])
        else :
            non_seq.append(status[i][1])
            
    for j in range(0,600,2):
        if seq_No[0] in seq :
            time.sleep(0.0025)
            canvas1.move(rect1,0.5,0.5)
            canvas1.move(text1,0.5,0.5)
            canvas1.update()
            
        if len(status) > 2 and seq_No[1] in seq :
            time.sleep(0.0025)
            canvas1.move(rect2,0.5,0.5)
            canvas1.move(text2,0.5,0.5)
            canvas1.update()
            
        if len(status) > 4 and seq_No[2] in seq :
            time.sleep(0.0025)
            canvas1.move(rect3,0.5,0.5)
            canvas1.move(text3,0.5,0.5)
            canvas1.update()
            

        if seq_No[0] in non_seq :
            time.sleep(0.0025)
            canvas1.move(rect1,2,0.5)
            canvas1.move(text1,2,0.5)
            canvas1.update()
            
        if len(status) > 2 and seq_No[1] in non_seq :
            time.sleep(0.0025)
            canvas1.move(rect2,2,0.5)
            canvas1.move(text2,2,0.5)
            canvas1.update()
            
        if len(status) > 4 and seq_No[2] in non_seq :
            time.sleep(0.0025)
            canvas1.move(rect3,2,0.5)
            canvas1.move(text3,2,0.5)
            canvas1.update()

        if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
            timer -= 1
            canvas1.delete(txt)
            txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))

            
    string1 = ''
    for i in range(len(seq)) :
        string1 += str(seq[i])
        if i < len(seq) - 1 :
            string1 += ','

    if len(seq) > 0 :
        text_data1 = canvas1.create_text(700,300,text="Frame " + string1 + " Lost",fill='red',font=('calibri',15))
    
    ack_lost = []
    ack_rcvd = []
    frame_dam = []

    for i in range(len(status)//2,len(status)) :
        if status[i][0] == "Acknowledgement Lost" and i != len(status) - 1 :
            ack_lost.append(status[i][1])
        elif status[i][0] == "Acknowledgement Received":
            ack_rcvd.append(status[i][1])
        elif status[i][0] == "Frame Damaged" :
            frame_dam.append(status[i][1])

    length = len(status) - 1
    if status[length][0] == "Acknowledgement Lost" :
        ack_rcvd.append(status[7][1])


    
    location = 0
    for i in range(len(status)//2,len(status)) :
        if status[i][0] == "Acknowledgement Received" or status[i][0] == "Acknowledgement Lost" :
            size2 += 1
            location = int(status[i][1])
        else :
            break
    
    location = location % 4
    
    
    for j in range(location,4) :
        if status[i][0] == "Acknowledgement Received" or status[i][0] == "Acknowledgement Lost" :
            canvas1.move(windowr2,15,0)
            canvas1.update()
            size2 += 1

    if seq_No[0] in seq :
        time.sleep(2)
        canvas1.itemconfig(rect1,fill="light yellow")
        canvas1.delete(rect1)
        canvas1.itemconfig(text1,fill="light yellow")
        canvas1.delete(text1)
        
    if len(seq) > 2 and seq_No[1] in seq :
        time.sleep(2)
        canvas1.itemconfig(rect2,fill="light yellow")
        canvas1.delete(rect2)
        canvas1.itemconfig(text2,fill="light yellow")
        canvas1.delete(text2)
        
    if len(seq) > 4  and seq_No[2] in seq :
        time.sleep(2)
        canvas1.itemconfig(rect3,fill="light yellow")
        canvas1.delete(rect3)
        canvas1.itemconfig(text3,fill="light yellow")
        canvas1.delete(text3)


    string1 = ''
    for i in range(len(frame_dam)) :
        string1 += str(frame_dam[i])
        if i < len(frame_dam) - 1 :
            string1 += ','
    
    
    if len(frame_dam) > 0 :
        text_data2 = canvas1.create_text(1120,300,text="Frames " + string1 + " are damaged.",fill='Red',font=('calibri',14))
       

    string2 = ''
    for i in range(len(ack_lost)) :
        string2 += str(ack_lost[i])
        if i < len(ack_lost) - 1 :
            string1 += ','
    
    
    for j in range(0,600,2) :
        
        if seq_No[0] in ack_lost :
            time.sleep(0.0025)
            canvas1.move(rect1,-0.5,0.5)
            canvas1.move(text1,-0.5,0.5)
            canvas1.update()
            time.sleep(0.05)
            

        if len(status) > 2 and seq_No[1] in ack_lost :
            time.sleep(0.0025)
            canvas1.move(rect2,-0.5,0.5)
            canvas1.move(text2,-0.5,0.5)
            canvas1.update()
            time.sleep(0.05)
            

        if len(status) > 4 and seq_No[2] in ack_lost :
            time.sleep(0.0025)
            canvas1.move(rect3,-0.5,0.5)
            canvas1.move(text3,-0.5,0.5)
            canvas1.update()
        
        if seq_No[0] in ack_rcvd :
            time.sleep(0.0025)
            canvas1.move(rect1,-2,0.5)
            canvas1.move(text1,-2,0.5)
            canvas1.update()
            
        if len(status) > 2 and seq_No[1] in ack_rcvd :
            time.sleep(0.0025)
            canvas1.move(rect2,-2,0.5)
            canvas1.move(text2,-2,0.5)
            canvas1.update()
            
        if len(status) > 4 and seq_No[2] in ack_rcvd :
            time.sleep(0.0025)
            canvas1.move(rect3,-2,0.5)
            canvas1.move(text3,-2,0.5)
            canvas1.update()

        if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590 :
        
            timer -= 1
            canvas1.delete(txt)
            txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))


    if len(ack_lost) > 0 :
        text_data3 = canvas1.create_text(700,390,text="Acknowledgement of Frames "+ string2 +" is Lost.",fill='red',font=('calibri',15))
     
    string1 = ''
    for i in range(len(ack_rcvd)) :
        string1 += str(ack_rcvd[i])
        if i < len(ack_rcvd) - 1 :
            string1 += ','
    
    if len(ack_rcvd) > 0 :
        text_data4 = canvas1.create_text(150,390,text="Acknowledgement of Frames "+ string1 + " received.",fill='Green',font=('calibri',12))
        
    
    for i in range(len(status)//2,len(status)) :
        if status[i][0] == "Acknowledgement Received" or status[i][0] == "Acknowledgement Lost" :
            size1 += 1
            location = int(status[i][1])
        else :
            break
        
    location = location % 4
    print(location)

    for j in range(location,4) :
        if status[i][0] == "Acknowledgement Received" or status[i][0] == "Acknowledgement Lost" :
            canvas1.move(windows1,15,0)
            canvas1.update()
            size1 += 1

    if size1 >= 16 :
        canvas1.itemconfig(windows1, fill = 'light yellow')
        canvas1.delete(windows1)

    if size2 >= 16 :
        canvas1.itemconfig(windowr2, fill = 'light yellow')
        canvas1.delete(windowr2)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_windows2() :
    global canvas1,i
    global text_data1,text_data2,text_data3,text_data4,text_data5,text_data6,text_data7
    global windows1,windowr2
    global rect1,rect2,rect3,rect4,rect4,text1,text2,text3,text4,timer,txt
    global size1, size2
    
    seq0 = status[0]
    seq1 = status[1]
    seq2 = status[2]
    seq3 = status[3]

    seq = []
    non_seq = []
    for i in range(4,8) :
        if status[i][0] == 'Frame Lost' :
            seq.append(status[i][1])
        else :
            non_seq.append(status[i][1])

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


    canvas1.create_circle(150,300,30, outline = 'blue')
    txt = canvas1.create_text(150,300, text=timer, font = ('calibri',15))   
    
    
    for j in range(0,600,2) :

        if seq0 in seq :
            time.sleep(0.0025)
            canvas1.move(rect1,0.5,0.5)
            canvas1.move(text1,0.5,0.5)
            canvas1.update()
        if seq1 in seq :
            time.sleep(0.0025)
            canvas1.move(rect2,0.5,0.5)
            canvas1.move(text2,0.5,0.5)
            canvas1.update()
        if seq2 in seq :
            time.sleep(0.0025)
            canvas1.move(rect3,0.5,0.5)
            canvas1.move(text3,0.5,0.5)
            canvas1.update()
        if seq3 in seq :
            time.sleep(0.0025)
            canvas1.move(rect4,0.5,0.5)
            canvas1.move(text4,0.5,0.5)
            canvas1.update()
            
        if seq0 in non_seq :
            time.sleep(0.0025)
            canvas1.move(rect1,2,0.5)
            canvas1.move(text1,2,0.5)
            canvas1.update()
        if seq1 in non_seq :
            time.sleep(0.0025)
            canvas1.move(rect2,2,0.5)
            canvas1.move(text2,2,0.5)
            canvas1.update()
        if seq2 in non_seq :
            time.sleep(0.0025)
            canvas1.move(rect3,2,0.5)
            canvas1.move(text3,2,0.5)
            canvas1.update()
        if seq3 in non_seq :
            time.sleep(0.0025)
            canvas1.move(rect4,2,0.5)
            canvas1.move(text4,2,0.5)
            canvas1.update()

        if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590:
        
            timer -= 1
            canvas1.delete(txt)
            txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
        

    string1 = ''
    for i in range(len(seq)) :
        string1 += str(seq[i])
        if i < len(seq) - 1 :
            string1 += ','
    
    if len(seq) > 0 :
        text_data1 = canvas1.create_text(700,300,text="Frame " + string1 + " Lost",fill='red',font=('calibri',15))
        text_data5 = canvas1.create_text(1155,350,text="Negative Acknowledgement of Frame"+ string1 + " is sent",fill='Red',font=('calibri',12))
        
    ack_lost = []
    ack_rcvd = []
    frame_dam = []

    for i in range(4,8) :
        if status[i][0] == "Acknowledgement Lost" and i != 7 :
            ack_lost.append(status[i][1])
        elif status[i][0] == "Acknowledgement Received":
            ack_rcvd.append(status[i][1])
        elif status[i][0] == "Frame Damaged" :
            frame_dam.append(status[i][1])

    if status[7][0] == "Acknowledgement Lost" :
        ack_rcvd.append(status[7][1])

    for i in range(4,8) :
        if status[i][0] == "Acknowledgement Received" or status[i][0] == "Acknowledgement Lost" :
            canvas1.move(windowr2,15,0)
            canvas1.update()
            size2 += 1
        else :
            break
    

    
    if seq0 in seq :
        time.sleep(2)
        canvas1.itemconfig(rect1,fill="light yellow")
        canvas1.delete(rect1)
        canvas1.itemconfig(text1,fill="light yellow")
        canvas1.delete(text1)
        
    if seq1 in seq :
        time.sleep(2)
        canvas1.itemconfig(rect2,fill="light yellow")
        canvas1.delete(rect2)
        canvas1.itemconfig(text2,fill="light yellow")
        canvas1.delete(text2)
        
    if seq2 in seq :
        time.sleep(2)
        canvas1.itemconfig(rect3,fill="light yellow")
        canvas1.delete(rect3)
        canvas1.itemconfig(text3,fill="light yellow")
        canvas1.delete(text3)
        
    if seq3 in seq :
        time.sleep(2)
        canvas1.itemconfig(rect4,fill="light yellow")
        canvas1.delete(rect4)
        canvas1.itemconfig(text4,fill="light yellow")
        canvas1.delete(text4)
        
    
    string1 = ''
    for i in range(len(frame_dam)) :
        string1 += str(frame_dam[i])
        if i < len(frame_dam) - 1 :
            string1 += ','
    
    
    if len(frame_dam) > 0 :
        text_data2 = canvas1.create_text(1120,300,text="Frames " + string1 + " are damaged.",fill='Red',font=('calibri',14))
        text_data5 = canvas1.create_text(1155,350,text="Negative Acknowledgement of Frame"+ string1 + " is sent",fill='Red',font=('calibri',12))
        
    string2 = ''
    for i in range(len(ack_lost)) :
        string2 += str(ack_lost[i])
        if i < len(ack_lost) - 1 :
            string1 += ','
    
    if len(frame_dam) > 0 :
        time.sleep(2)
        canvas1.itemconfig(text_data1,fill="light yellow")
        canvas1.delete(text_data1)
    
    for j in range(0,600,2) :
        if seq0 in ack_lost :
            time.sleep(0.0025)
            canvas1.move(rect1,-0.5,0.5)
            canvas1.move(text1,-0.5,0.5)
            canvas1.update()
            time.sleep(0.05)
            

        if seq1 in ack_lost :
            time.sleep(0.0025)
            canvas1.move(rect2,-0.5,0.5)
            canvas1.move(text2,-0.5,0.5)
            canvas1.update()
            time.sleep(0.05)
            

        if seq2 in ack_lost :
            time.sleep(0.0025)
            canvas1.move(rect3,-0.5,0.5)
            canvas1.move(text3,-0.5,0.5)
            canvas1.update()
            
        if seq3 in ack_lost :
            time.sleep(0.0025)
            canvas1.move(rect4,-0.5,0.5)
            canvas1.move(text4,-0.5,0.5)
            canvas1.update()

        if seq0 in ack_rcvd :
            time.sleep(0.0025)
            canvas1.move(rect1,-2,0.5)
            canvas1.move(text1,-2,0.5)
            canvas1.update()

        if seq1 in ack_rcvd :
            time.sleep(0.0025)
            canvas1.move(rect2,-2,0.5)
            canvas1.move(text2,-2,0.5)
            canvas1.update()

        if seq2 in ack_rcvd :
            time.sleep(0.0025)
            canvas1.move(rect3,-2,0.5)
            canvas1.move(text3,-2,0.5)
            canvas1.update()

        if seq3 in ack_rcvd :
            time.sleep(0.0025)
            canvas1.move(rect4,-2,0.5)
            canvas1.move(text4,-2,0.5)
            canvas1.update()

        if j == 60 or j == 120 or j == 180 or j == 240 or j == 300 or j == 360 or j == 420 or j == 480 or j == 540 or j == 590 :
        
            timer -= 1
            canvas1.delete(txt)
            txt = canvas1.create_text(150, 300, text=timer, font = ('calibri',15))
        
    if len(ack_lost) > 0 :
        text_data3 = canvas1.create_text(700,390,text="Acknowledgement of Frames "+ string2 +" is Lost.",fill='red',font=('calibri',15))
        

    string1 = ''
    for i in range(len(ack_rcvd)) :
        string1 += str(ack_rcvd[i])
        if i < len(ack_rcvd) - 1 :
            string1 += ','
    
    if len(ack_rcvd) > 0 :
        text_data4 = canvas1.create_text(150,390,text="Acknowledgement of Frames "+ string1 + " received.",fill='Green',font=('calibri',12))

    for i in range(4,8) :
        if status[i][0] == "Acknowledgement Received" or status[i][0] == "Acknowledgement Lost" :
            canvas1.move(windows1,15,0)
            canvas1.update()
            size1 += 1
        else :
            break

    if size1 >= 16 :
        canvas1.itemconfig(windows1, fill = 'light yellow')
        canvas1.delete(windows1)

    if size2 >= 16 :
        canvas1.itemconfig(windowr2, fill = 'light yellow')
        canvas1.delete(windowr2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

root = Tk()
root.title("Selective Repeat Protocol")
canvas = Canvas(root,width = 1450, height = 700, bg = "light yellow")
canvas.pack(expand = YES, fill = BOTH)

button1 = Button(root,text = "Start Transmission",command = transmission)
button2 = Button(root,text = "Start Animation",command = animation)
button1.place(x=400,y=50)
button2.place(x=900,y=50)

button3 = Button(canvas, text = 'Display Flow of Control',command = create_window)
button3.place(x=580,y=600)

txt1_canvas = canvas.create_text(650,230,text = "(I). Click Start Transmission Button, to transfer data between sender and receiver ",fill='blue',font = ('calibri',20))
txt2_canvas = canvas.create_text(660,320,text = "(II). Click Start Animation to understand the flow of frames in Stop and wait Protocol",font = ('calibri',20))
 
mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

        
