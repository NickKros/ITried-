from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

FS = """
firstScreen:
	orientation: "vertical"

	Label:
		font_size: "30sp"
		text: root.data_label
		on_text: app.process()

	TextInput:
		id: inp
		multiline: False
		padding_y: (5, 5)
		size_hint: (1, 0.5)

	Button:
		text: "classic"
		bold: True
		background_color: '#00FFCE'
		size_hint: (1, 0.5)
		on_press: root.testback()
"""

class firstScreen(BoxLayout):

	data_label = StringProperty("Картошка")

	def testback(self):
		self.data_label = self.ids.inp.text


class MyApp(App):

	def process(self):
		text = self.root.ids.inp.text
	
	def build(self):
		return Builder.load_string(FS)

if __name__ == "__main__":
	MyApp().run()