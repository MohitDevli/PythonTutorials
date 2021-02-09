from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField, MDTextFieldRound
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton
from kivy.uix.textinput import TextInput
import threading
from kivy.core.window import Window
Window.size=(800,600)

import socket

kv="""
ScreenManager
    StartPage:
    MsgPlatform:

<StartPage>:
    name:'start'
    
    TextInput:
        text:root.ip()
        readonly:True
        size_hint:0.3,0.05
        pos_hint:{'center_x':0.5,'center_y':0.6}
        
    MDTextField:
        id:port
        hint_text:'Enter port no.'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:0.3
        max_text_length:4
        helper_text_mode:"on_error"
        helper_text:'   Port no. must be 4 digit.'
    
    
    MDFillRoundFlatButton:
        text:'Start'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_release:
            root.start()
            root.manager.transition.direction='left'
            root.manager.transition.duration= 0.2
            root.manager.current='msgplatform'
            
            

<MsgPlatform>:
    name:'msgplatform'
    
    MDTextFieldRound:
        id:host_msg
        hint_text:"Message.."
        mode:"rectangle"
        pos_hint:{'center_x':0.5,'center_y':0.05}
        size_hint:0.8,0.05
        multiline:True
        color_active:10,10,10,1
    
    MDIconButton:
        icon:'send.jpg'
        pos_hint:{'center_x':0.95,'center_y':0.05}
        size_hint:0.04,0.03
        on_release:
            root.send_host_msg()

"""

host= socket.gethostbyname(str(socket.gethostname()))
s=socket.socket()
print(host)
data=""


class recvThread(object):
    
    def __init__(self):
        thread = threading.Thread(target=self.recv, args=())
        thread.daemon = True
        thread.start()    
    
    def recv(self):
        while True:
            global data
            global conn
            data=str(conn.recv(5000),'utf-8')
            print(data)
        


class StartPage(Screen):
    def ip(self):
        ip=host+str("      --This is your ip")
        return ip
    
    def start(self):
        port_w=self.ids.port
        port=port_w.text
        
        try:
            print("Conectting.........")
            s.bind((host,int(port)))
            s.listen(0)
            
            global conn
            global addr
            conn,addr=s.accept()            
            print('connect')
            print(conn,addr )
            
        except socket.error as err:
            print(err)
            
   
    
class MsgPlatform(Screen):
    
    def on_pre_enter(self):
        recvThread()    
    
    def send_host_msg(self):
        host_msg=str(self.ids.host_msg.text)
        global conn
        conn.send(str.encode(host_msg))
        

          
   

           
sm=ScreenManager()
sm.add_widget(StartPage(name='start'))
sm.add_widget(MsgPlatform(name="msgplatform"))

class MainApp(MDApp):
    def build(self):
        script=Builder.load_string(kv)
        return script

MainApp().run()