import socket

print('Your ip-Addresh is: ',socket.gethostbyname(socket.gethostname()))
port=int(input('Enter port no. :  '))
name=input('Enter your name.')
host=socket.gethostbyname(socket.gethostname())
s=socket.socket()

def binding():
    try:
        
        global port
        global host
        global conn
        global addr
        s.bind((host,port))
        s.listen(0)
        conn,addr=s.accept() 
    
    except socket.error as err:
        print('Error while creating connections, error is:\n\n',err)
        
def messageing():
    s.send(str.encode(name))
        
        
if __name__=='__main__':
    binding()
    messageing()
        
