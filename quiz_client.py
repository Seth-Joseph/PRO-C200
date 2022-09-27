import socket
from threading import Thread

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port =8000
client.connect((ip_address,port))
print('Client connected.')
nickname = input('Enter your name:')

def recieve():
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            if msg == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            print('Connection error.')
            client.close()
            break
    
def write():
    while True:
        msg = '{}: {}'.format(nickname,input(''))
        client.send(msg.encode('utf-8'))
        

recieveThread = Thread(target=recieve)
recieveThread.start()
writeThread = Thread(target=write)
writeThread.start()