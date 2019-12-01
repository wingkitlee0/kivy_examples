import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def btn(self):
        print("Hello {} {}!".format(self.first_name.text, self.last_name.text))



class Ex2App(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    Ex2App().run()