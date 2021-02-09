from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRoundFlatButton
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
script="""
ScreenManager:
	screen:
	
<screen>:
	name:'scrn'
	MDRoundFlatButton:
		id:btn
        text:'Click to start Your Journey'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint:0.3,0.1
        on_press:
            root.button()
    Label:
    	text:'mohit'
"""

class screen(Screen):
	def button(self):
		bu=self.ids.btn
		

sm=ScreenManager()
sm.add_widget(screen(name='scrn'))

class TranferFilesApp(MDApp):
	def build(self):
		kv=Builder.load_string(script)
		return kv
		
TranferFilesApp().run()
