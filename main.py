from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

KV = """
MyBL:
	orientation: "vertical"

	Label:
		font_size: "30sp"
		text: root.label_text

	TextInput:
		multiline: False
		size_hint: (1, 0.5)

	Button:
		text: "classic"
		bold: True
		background_color: '#00FFCE'
		size_hint: (1, 0.5)
"""

class MyBL(BoxLayout):
	
	label_text = StringProperty("Что-то")


class MyApp(App):

	def build(self):
		return Builder.load_string(KV)
		'''
		main_widget = Builder.load_string(KV)
		return main_widget'''

if __name__ == "__main__":
	MyApp().run()