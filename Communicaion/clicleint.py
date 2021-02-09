import socket

host=input('Enter ip:  ')
port=int(input('Enter port no. :  '))
name=input('Enter your name.')

s=socket.socket()
host_name=str(s.recv(5000),'utf-8') 


def connecting():
    s.connect((host,port))


def Messaging():
    msg=input(host_name,':>  ')
    
    
if __name__=='__main__':
    connecting()
    Messaging()