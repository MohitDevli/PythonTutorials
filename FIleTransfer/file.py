from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivymd.uix.button import MDRoundFlatButton
from kivymd.app import MDApp
import webbrowser
import socket
import os
from kivy.uix.label import Label
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)

script = """
ScreenManager:
    Page_One:
   
<Page_One>:
    name:'page_one'
    
    MDRoundFlatButton:
    	id:btn
        text:'Click Here'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint:0.3,0.1
		on_press:
			root.execute()
			
	Label:
		id:lbl
		text:'htllo'
		size_hint:0.5,0.5
"""


class Page_One(Screen):
    def execute(self):
    	bu=self.ids.btn
    	#os.system('python -m http.server 8000')
    	#os.popen('python -m http.server 8000').read()
    	#get=webbrowser.open_new(str(ip)+':8000')
    	l=self.ids.lbl
    	l.text='mohit'
    
sm=ScreenManager()
sm.add_widget(Page_One(name='page_one'))

class WikoPediaApp(MDApp):
    def build(self):
        script_kv=Builder.load_string(script)
        return script_kv

if __name__=='__main__':
    WikoPediaApp().run()
