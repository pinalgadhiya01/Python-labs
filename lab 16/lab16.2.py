from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.input = TextInput(hint_text="Type something", multiline=False)
        self.output = Label(text="")
        btn = Button(text="Show Text")
        btn.bind(on_press=self.show_text)

        self.layout.add_widget(self.input)
        self.layout.add_widget(btn)
        self.layout.add_widget(self.output)
        return self.layout

    def show_text(self, instance):
        self.output.text = f"You typed: {self.input.text}"

if __name__ == "__main__":
    TextInputApp().run()
