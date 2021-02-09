from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextField, MDTextFieldRound
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton,MDRectangleFlatButton
import sys
import socket
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, IRightBody
import threading
import multiprocessing 
from kivy.core.window import Window
Window.size=(800,600)
import time
from kivy.uix.label import Label
from kivy.clock import mainthread, MultiprocessingEvent
from kivy.clock import Clock
from kivy.properties import ObjectProperty

kv="""


ScreenManager
    LoginPage:
    MsgPlatform:

<LoginPage>:
    name:'login'
    
        
    MDTextField:
        id:ip
        hint_text:'Enter ip-Addresh'
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:0.3
        
    MDTextField:
        id:port
        hint_text:'Enter port'
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:0.3
    
    MDFillRoundFlatButton:
        text:'Join'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_release:
            root.login()
            root.manager.transition.direction='left'
            root.manager.transition.duration= 0.2
            root.manager.current='msgplatform'
  
            
<MsgPlatform>:
    name:'msgplatform'
    
    ScrollView:
        MDList:
            id:container
  
    
    MDTextFieldRound:
        id:cli_msg
        hint_text:"Message.."
        mode:"rectangle"
        pos_hint:{'center_x':0.5,'center_y':0.05}
        size_hint:0.8,0.05
        multiline:False
        color_active:10,10,10,1
        on_text_validate:
            root.send_msg()
            root.clear_msg()
        
    
    MDIconButton:
        icon:'send.jpg'
        pos_hint:{'center_x':0.95,'center_y':0.05}
        size_hint:0.04,0.03
        on_release:
            root.send_msg()
            root.clear_msg()
             
   
        
"""


s=socket.socket()
data=''


class recvThread(object):
   
    def __init__(self):
        thread = threading.Thread(target=self.recv, args=())
        thread.daemon = True
        thread.start()    
        
              
    
   
    def recv(self):
        while True:
            global data
            data=str(s.recv(5000),'utf-8')     
            if str(data)!='':
                sm.get_screen('msgplatform').ids.container.add_widget(OneLineListItem(text=str(data)))  
               # Clock.schedule_once(lambda dt: MsgPlatform().recv(),1)


class LoginPage(Screen):
   
    def login(self):
                
        host=str(self.ids.ip.text)
        port=int(self.ids.port.text)
        
        s.connect((host,port))
        
       
        
class MsgPlatform(Screen):
    
    def p(self):
        print('recv')
    
   
    def on_pre_enter(self):
        recvThread()
    '''
    def recv(self):
        self.recvMsg()
    
    
    def recvMsg(self):
        cont=self.ids.container
        global data 
        print(data)
        cont.add_widget(OneLineListItem(text=str(data)))                
        
       ''' 

    def send_msg(self):
        cont=self.ids.container
        if str(self.ids.cli_msg.text)!="":
            cont.add_widget(OneLineListItem(text=str(self.ids.cli_msg.text)))  
        
        cli_msg=str(self.ids.cli_msg.text)
        s.send(str.encode(cli_msg))
        
        cli_msg=""
    
    def clear_msg(self):
        msg=self.ids.cli_msg
        msg.text=""
    
    
    
    
    
sm=ScreenManager()
sm.add_widget(LoginPage(name='login'))
sm.add_widget(MsgPlatform(name="msgplatform"))


class MainApp(MDApp):
    recv_msg = ObjectProperty()
    def build(self):
        script=Builder.load_string(kv)
        return script
    
if __name__=='__main__':
    MainApp().run()
   
    
    