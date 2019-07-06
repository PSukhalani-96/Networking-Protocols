import socket
import random
import pickle
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RECEIVER_ADDR = ('localhost', 8025)
SENDER_ADDR = ('localhost', 8000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(SENDER_ADDR)

#----------------------------------------------------------

tot_frames = 16
n = 3
m = pow(2,n)
t = 0
frame_send_at_instance = m // 2
sw = 0
rw = 0
arr1 = []
arr = []
size = 0

for i in range(tot_frames) :
    arr.append(t)
    t = (t+1) % m
#print(arr)
#----------------------------------------------------------

tkinter_status = []
def sender() :
    global m
    global sw,size
    global rw
    global frame_send_at_instance
    global arr,total_frames
    global arr1

    #------------------------------------------------------------
    file = open("l.txt","ab")
    file.seek(0)
    file.truncate(0)
    #-------------------------------------------------------------
    
    ch = 'y'
    print(f'\33]0;GoBackN Sender\a', end = '', flush = True)
    
    while ch == 'y' and size < tot_frames :
        
        tkinter_status = []
        arr1 = []
        packet = []
        j = 0

        if tot_frames - size < 4 :
            frame_send_at_instance = tot_frames - size
            
        for i in range(sw,(sw+frame_send_at_instance)) :
            arr1.append(arr[i])
            j += 1
            tkinter_status.append(arr[i])
        
        print("--------------------------------------------------------------------------------")
        for i in range(j) :
            print("Frame  ",arr1[i]," is sent")
        print("--------------------------------------------------------------------------------")
            
        f = random.randint(0,9)
        f1 = random.randint(0,frame_send_at_instance-1)
        
        packet.extend([m,frame_send_at_instance,arr1,rw,f,f1])
        sock.sendto(pickle.dumps(packet),('localhost',8025))

        if f != 5 :
            
            ack,_ = sock.recvfrom(1024)
            ack = pickle.loads(ack)
            rw = int(ack[0])
            a1 = int(ack[1])
            if a1 >= 0 and a1 <= 3 :
                for k in range(len(arr)) :
                    if arr1[k] != arr1[a1] :
                        print("--------------------------------------------------------------------------------")
                        print("Acknowledgement of Frame",arr1[k]," is recieved")
                        
                    else :
                        break
                print("--------------------------------------------------------------------------------")
                print("Acknowledgement of Frame ",arr1[a1]," is lost")
                print("--------------------------------------------------------------------------------")
                tkinter_status.append(["Acknowledgement Lost",arr1[a1]])
                temp = (sw + frame_send_at_instance) % m
                comp = 0
                if (temp == 0) :
                    comp = 7

                if int(arr1[a1]) == comp or int(arr1[a1]) == temp-1:
                    sw = (sw + 3) % m
                    size += 3

                else :
                    sw = ( sw + frame_send_at_instance) % m
                    size += 4
            else :
                sw = ( sw + frame_send_at_instance) % m
                print("--------------------------------------------------------------------------------")
                print("All Four Frames are Acknowledged")
                print("--------------------------------------------------------------------------------")
                size += 4
                tkinter_status.append(["Acknowledgement Received","All"])

        else :
            ack,_ = sock.recvfrom(1024)
            ack = pickle.loads(ack)
            rw = int(ack[0])
            f1 = int(ack[1])
            ld = random.randint(0,1)

            if ld == 0 :
                print("--------------------------------------------------------------------------------")
                print("Frame ",arr1[f1]," is damaged.")
                tkinter_status.append(["Frame Damaged",arr1[f1]])
                print("--------------------------------------------------------------------------------")
            else :
                print("--------------------------------------------------------------------------------")
                print("Frame ",arr1[f1]," is lost")
                tkinter_status.append(["Frame Lost",arr1[f1]])
                print("--------------------------------------------------------------------------------")
                    
            for i in range(f1+1,frame_send_at_instance) :
                print("Frame ",arr1[i]," is discarded")
            print("--------------------------------------------------------------------------------")
            print("-------------TIMEOUT-------------")
            tkinter_status.append(["Timeout","All"])
            sw = arr1[f1]

        pickle.dump(tkinter_status,file)
        ch = input('Send Again(y/n) : ')
        if ch != 'y':
            break
    file.close()
    time.sleep(2)
sender()
sock.close()
