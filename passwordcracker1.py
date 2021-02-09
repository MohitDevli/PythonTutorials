from wireless import Wireless
import random


wireless = Wireless()
name=input("enter the name of network(ssid)")

data_1=[1,2,3,4,5,6,7,8,9,0,'!','@','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#conn=wireless.connect(ssid=name, password=random.choice(tuple(data_1)))




for i in range(0,1):
    while not True:
        data_2=str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) 
        print(data_2)
        while print(wireless.connect(ssid=name, password=data_2))==True:
            pass_ac=random.choice(data_2)
            print(pass_ac)
            

#Hit and trial
"""
while True:
    data_2=str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) 
    print(data_2)
    while print(wireless.connect(ssid=name, password=data_2))==True:
        pass_ac=random.choice(tuple(data_2))
        print(pass_ac)
        data_2=str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10)) +str(random.randint(0,10))  +str(random.randint(0,10)) +str(random.randint(0,10))
        print(data_2)
        """
