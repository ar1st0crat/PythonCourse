from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyDumbScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(MyDumbScreen, self).__init__(**kwargs)
        my_user_input = TextInput()
        self.add_widget(my_user_input)

        my_output = Label()
        self.add_widget(my_output)

        def callback(instance, value):
            my_output.text = value + "!"
            
        my_user_input.bind(text=callback)


class MyApp(App):

    def build(self):
        return MyDumbScreen()


if __name__ == '__main__':
    MyApp().run()
