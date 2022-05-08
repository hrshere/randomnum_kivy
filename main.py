import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('1.2.0')

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))

class HrsRandom(App):

    def build(self):#to return the ui
        return MyRoot()

#instance
hrsRandom = HrsRandom()
hrsRandom.run()
