import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from config import KIVYDIR
#from . import firstScreen

#class firstScreen(BoxLayout):
#		pass

class MyApp(App):

	def build(self):
		main_widget = Builder.load_file(os.path.join(KIVYDIR, "firstScreen.kv"))
		return main_widget

#if __name__ == "__main__":
MyApp().run()