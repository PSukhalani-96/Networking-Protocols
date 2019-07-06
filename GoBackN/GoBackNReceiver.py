import socket
import pickle
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RECEIVER_ADDR = ('localhost', 8025)
SENDER_ADDR = ('localhost', 8000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(RECEIVER_ADDR)

def receiver() :

    print(f'\33]0;GoBackN Receiver\a', end = '', flush = True)
    while True :
        pkt,addr = sock.recvfrom(1024)
        pkt = pickle.loads(pkt)
        packet = []
        m = int(pkt[0])
        frame_send_at_instance = int(pkt[1])
        arr1 = pkt[2]
        rw = int(pkt[3])
        f = int(pkt[4])
        f1 = int(pkt[5])

        if f != 5 :
            for i in range(frame_send_at_instance) :
                if rw == int(arr1[i]) :
                    print("--------------------------------------------------------------------------------")
                    print("Frame ",arr1[i]," is received correctly.")
                    rw = (rw+1)%m
                    print("--------------------------------------------------------------------------------")
                else :
                    print("--------------------------------------------------------------------------------")
                    print("Duplicate Frame ",arr1[i]," is discarded")
                    print("--------------------------------------------------------------------------------")
                    
            a1 = random.randint(0,14)
            packet.extend([rw,a1])
            sock.sendto(pickle.dumps(packet),addr)

        else :
            for i in range(f1) :
                if rw == int(arr1[i]) :
                    print("--------------------------------------------------------------------------------")
                    print("Frame ",arr1[i]," is received correctly.")
                    rw = (rw + 1)%m
                    print("--------------------------------------------------------------------------------")

                else :
                    print("--------------------------------------------------------------------------------")
                    print("Duplicate Frame ",arr1[i]," is discarded.")
                    print("--------------------------------------------------------------------------------")

            packet.extend([rw,f1])
            sock.sendto(pickle.dumps(packet),addr)


receiver()
sock.close()
