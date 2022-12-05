from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
	def build(self):
		return Button(text = "Hello, world", 
			on_press=self.func,
			on_release=self.func1)

	def func(self, instance):
		instance.text = "Пошел нахуй"
	def func1(self, instance):
		instance.text = "Все равно пошел нахуй"

if __name__ == "__main__":
	MyApp().run()