from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from.kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class PrintMessage(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x":0.5,"center_y":0.5}

	self.kivyAppTest = Label(text="Kivy App",font_size=60,color="#c70202")
	self.window.add_widget(self.kivyAppTest)
        self.window.add_widget(Image(source="icon/kivy-icon-256.png"))

	self.intro = Label(text="This app is a test.")
        self.msg = Label(text="Here goes your message",font_size=48,color="#c70202")
	self.window.add_widget(self.intro)
        self.window.add_widget(self.msg)

        self.user = TextInput(multiline=True,padding_y=(20,20),size_hint=(1,0.35))
        self.window.add_widget(self.user)

        self.btn = Button(text="Print it!",size_hint=(1,0.3),bold=True,background_color="#c70202")
        self.btn.bind(on_press=self.callback)
        self.window.add_widget(self.btn)

        return self.window

    def callback(self,instance):
        self.msg.text = self.user.text

if __name__ == "__main__":
    PrintMessage().run()
