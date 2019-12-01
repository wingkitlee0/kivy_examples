import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1
        # put the text fields in "inside"
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.first_name = TextInput(multiline=False)
        self.inside.add_widget(self.first_name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit!", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.first_name.text + " " + self.last_name.text
        print("Hello, {}!".format(name))
        self.first_name.text = ""
        self.last_name.text = ""
        self.email = ""


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()