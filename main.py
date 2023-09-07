from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size = (500, 500)


class UnitConverter(MDApp):
    def __init__(self, **kwargs):
        super().__init__()
        self.title_label = None

    def build(self):
        self.root = MDRelativeLayout(md_bg_color=(0.2, 0.2, 0.2, 1))
        self.title = 'Unit Converter'

        self.title_label = Label(text='Unit Converter', font_size=50, pos_hint={'center_x': 0.5, 'center_y': 0.95},
                                 size_hint=(1, 1))
        self.root.add_widget(self.title_label)

        self.bmi_button = Button(text='BMI', pos_hint={'center_x': 0.28, 'center_y': 0.75}, size_hint=(0.23, 0.17),
                                 bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.bmi_button)

        self.length_button = Button(text='Length', pos_hint={'center_x': 0.68, 'center_y': 0.75},
                                    size_hint=(0.23, 0.17),
                                    bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.length_button)

        self.area_button = Button(text='Area', pos_hint={'center_x': 0.28, 'center_y': 0.50}, size_hint=(0.23, 0.17),
                                  bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.area_button)

        self.volume_button = Button(text='Volume', pos_hint={'center_x': 0.68, 'center_y': 0.50}, size_hint=(0.23, 0.17),
                                    bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.volume_button)

        self.speed_button = Button(text='Speed', pos_hint={'center_x': 0.28, 'center_y': 0.25}, size_hint=(0.23, 0.17),
                                   bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.speed_button)

        self.mass_button = Button(text='Mass', pos_hint={'center_x': 0.68, 'center_y': 0.25}, size_hint=(0.23, 0.17),
                                  bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.mass_button)

        return self.root


if __name__ == '__main__':
    UnitConverter().run()
