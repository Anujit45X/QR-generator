from kivy.app import App
from kivy.uix.boxlayout  import Boxlayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]


if __name__ == "__main__":
    app = MainApp()
    app.run()

