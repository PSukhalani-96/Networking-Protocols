import pickle
import sys
import socket
import random
import time
RECEIVER_ADDR = ('localhost',8025)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(RECEIVER_ADDR) 


def receive() :
    
    print(f'\33]0;StopNWait Reciever\a', end = '', flush = True)
    
    while True:
        pkt,addr = sock.recvfrom(1024)
        a_data =  pickle.loads(pkt)
        seq_no = a_data[0]
        rand = a_data[2]    
        
        if rand == 4 :
            print('Frame Received with seqNo: ',seq_no)
            pkt = (int(seq_no)+1) % 2
            print('Acknowlegment ',pkt,' sent')
            sock.sendto(bytes(str(pkt),'utf-8'),('localhost',8000))
            print('------------------------------------------------------------------')
            #break
                
        elif rand == 3 :
            print('Frame Received with seqNo: ',seq_no)
            pkt = 'Acknowledgement Lost'
            sock.sendto(bytes(str(pkt),'utf-8'),('localhost',8000))
            print('------------------------------------------------------------------')
           

        elif rand == 1 or rand == 2 :
            print('No Frame Received')
            print('------------------------------------------------------------------')

        else :
            break
    #sock.close()
    #time.sleep(10)

receive()   
sock.close()