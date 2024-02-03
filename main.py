from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import *


class Interface(BoxLayout):
    def addition1(self):
        self.ids.label1.text = str(randint(1, 20))
        self.ids.label2.text = "+"
        self.ids.label3.text = str(randint(1, 20))

    def subtraction1(self):
        a = randint(5, 15)
        self.ids.label1.text = str(randint(a, 20))
        self.ids.label2.text = "-"
        self.ids.label3.text = str(randint(1, a))

    def multiplication1(self):
        self.ids.label1.text = str(randint(1, 8))
        self.ids.label2.text = "*"
        self.ids.label3.text = str(randint(1, 8))

    def division1(self):
        data1 = self.ids.label3.text = str(randint(1, 3))
        self.ids.label2.text = "/"
        self.ids.label1.text = str(int(data1) * randint(1, 3))

    def addition2(self):
        self.ids.label1.text = str(randint(10, 200))
        self.ids.label2.text = "+"
        self.ids.label3.text = str(randint(10, 200))

    def subtraction2(self):
        a = randint(50, 150)
        self.ids.label1.text = str(randint(a, 200))
        self.ids.label2.text = "-"
        self.ids.label3.text = str(randint(10, a))

    def multiplication2(self):
        self.ids.label1.text = str(randint(10, 20))
        self.ids.label2.text = "*"
        self.ids.label3.text = str(randint(10, 20))

    def division2(self):
        data1 = self.ids.label3.text = str(randint(10, 20))
        self.ids.label2.text = "/"
        self.ids.label1.text = str(int(data1) * randint(10, 20))

    def addition3(self):
        self.ids.label1.text = str(randint(100, 2000))
        self.ids.label2.text = "+"
        self.ids.label3.text = str(randint(100, 2000))

    def subtraction3(self):
        a = randint(500, 1500)
        self.ids.label1.text = str(randint(a, 2000))
        self.ids.label2.text = "-"
        self.ids.label3.text = str(randint(100, a))

    def multiplication3(self):
        self.ids.label1.text = str(randint(15, 50))
        self.ids.label2.text = "*"
        self.ids.label3.text = str(randint(15, 50))

    def division3(self):
        data1 = self.ids.label3.text = str(randint(15, 50))
        self.ids.label2.text = "/"
        self.ids.label1.text = str(int(data1) * randint(15, 50))


    def check(self):
        try:
            if self.ids.label2.text == "+":
                if int(self.ids.textInput.text) == int(int(self.ids.label1.text) + int(self.ids.label3.text)):
                    self.ids.label2.text = "Correct!"
                    self.ids.textInput.text = self.ids.label1.text = self.ids.label3.text = ""
                else:
                    self.ids.label2.text = "Incorrect"
                    self.ids.textInput.text = self.ids.label1.text = self.ids.label3.text = ""
            elif self.ids.label2.text == "-":
                if int(self.ids.textInput.text) == int(int(self.ids.label1.text) - int(self.ids.label3.text)):
                    self.ids.label2.text = "Correct!"
                    self.ids.textInput.text = self.ids.label1.text = self.ids.label3.text = ""
                else:
                    self.ids.label2.text = "Incorrect"
                    self.ids.textInput.text = self.ids.label1.text = self.ids.label3.text = ""
            elif self.ids.label2.text == "*":
                if int(self.ids.textInput.text) == int(int(self.ids.label1.text) * int(self.ids.label3.text)):
                        self.ids.label2.text = "Correct!"
                        self.ids.textInput.text = self.ids.label1.text = self.ids.label3.text = ""
                else:
                        self.ids.label2.text = "Incorrect"
                        self.ids.textInput.text = self.ids.label1.text = self.ids.label3.text = ""
            else:
                if int(self.ids.textInput.text) == int(int(self.ids.label1.text) / int(self.ids.label3.text)):
                    self.ids.label2.text = "Correct!"
                    self.ids.textInput.text = self.ids.label1.text = self.ids.label3.text = ""
                else:
                    self.ids.label2.text = "Incorrect"
                    self.ids.textInput.text = self.ids.label1.text = self.ids.label3.text = ""
        except:
            self.ids.label2.text = "Error"
            self.ids.label1.text = self.ids.label3.text = ""


class MqgApp(App):
    pass


MqgApp().run()
