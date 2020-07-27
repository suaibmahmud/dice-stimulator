from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
import random

Window.size = (300, 400)

class Dice(GridLayout):

    # to display the dice & dice number
    def stimulator(self):

        self.num = random.randint(1, 6)
        # randint(from, to)
        # it takes only integers

        if self.num == 1:
            self.d_out.text = '-----------\n|           |\n|    0    |\n|           |\n-----------'
            self.d_out_2.text += '|1|  '

        if self.num == 2:
            self.d_out.text = '-----------\n|           |\n|   0 0   |\n|           |\n-----------'
            self.d_out_2.text += '|2|  '

        if self.num == 3:
            self.d_out.text = '-----------\n|    0    |\n|    0    |\n|    0    |\n-----------'
            self.d_out_2.text += '|3|  '

        if self.num == 4:
            self.d_out.text = '-----------\n|   0 0   |\n|           |\n|   0 0   |\n-----------'
            self.d_out_2.text += '|4|  '

        if self.num == 5:
            self.d_out.text = '-----------\n|   0 0   |\n|    0    |\n|   0 0   |\n-----------'
            self.d_out_2.text += '|5|  '

        if self.num == 6:
            self.d_out.text = '-----------\n|   0 0   |\n|   0 0   |\n|   0 0   |\n-----------'
            self.d_out_2.text += '|6|  '

    # clean all textinput fields
    def clean(self):
        self.d_out.text = ''
        self.d_out_2.text = ''

class DiceStimulator(App):
    def build(self):
        return Dice()

DiceStimulator().run()
