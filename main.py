from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from conversion_factor import unit_dict

Window.size = (500, 500)


class UnitConverter(MDApp):
    def __init__(self, **kwargs):
        super().__init__()
        self.unit_dict = unit_dict
        self.title_label = None

    def remove_widgets(self):
        self.root.remove_widget(self.bmi_button)
        self.root.remove_widget(self.length_button)
        self.root.remove_widget(self.area_button)
        self.root.remove_widget(self.volume_button)
        self.root.remove_widget(self.speed_button)
        self.root.remove_widget(self.mass_button)

    def reset_layout(self, instance):
        # Clear all the widgets from the root
        self.root.clear_widgets()

        # Add back the original widgets
        self.title_label = Label(text='Unit Converter', font_size=50, pos_hint={'center_x': 0.5, 'center_y': 0.95},
                                 size_hint=(1, 1))
        self.root.add_widget(self.title_label)

        self.bmi_button = Button(text='BMI', pos_hint={'center_x': 0.28, 'center_y': 0.75}, size_hint=(0.23, 0.17),
                                 bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1),
                                 on_press=self.bmi_converter)
        self.root.add_widget(self.bmi_button)

        self.length_button = Button(text='Length', pos_hint={'center_x': 0.68, 'center_y': 0.75},
                                    size_hint=(0.23, 0.17),
                                    bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.length_button)

        self.area_button = Button(text='Area', pos_hint={'center_x': 0.28, 'center_y': 0.50}, size_hint=(0.23, 0.17),
                                  bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.area_button)

        self.volume_button = Button(text='Volume', pos_hint={'center_x': 0.68, 'center_y': 0.50},
                                    size_hint=(0.23, 0.17),
                                    bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.volume_button)

        self.speed_button = Button(text='Speed', pos_hint={'center_x': 0.28, 'center_y': 0.25}, size_hint=(0.23, 0.17),
                                   bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.speed_button)

        self.mass_button = Button(text='Mass', pos_hint={'center_x': 0.68, 'center_y': 0.25}, size_hint=(0.23, 0.17),
                                  bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.mass_button)

    def calculate_bmi(self, instance):
        self.height = float(self.height_input.text)
        self.weight = float(self.weight_input.text)
        self.bmi = self.weight / (self.height ** 2)
        self.bmi = round(self.bmi * 10000, 2)
        self.bmi_label = Label(text=f'BMI: {self.bmi}', pos_hint={'center_x': 0.5, 'center_y': 0.15},
                               size_hint=(0.5, 0.1), font_size=50, bold=True, color=(1, 0, 0))
        self.root.add_widget(self.bmi_label)

    def bmi_converter(self, instance):
        self.remove_widgets()
        self.title_label.text = 'BMI Converter'
        self.back_button = Button(text='Back', pos_hint={'center_x': 0.2, 'center_y': 0.85}, size_hint=(0.2, 0.1),
                                  bold=True, font_size=30, background_color=(1, 0, 0), on_press=self.reset_layout)
        self.root.add_widget(self.back_button)
        self.height_label = Label(text='Height:', pos_hint={'center_x': 0.2, 'center_y': 0.75}, size_hint=(0.3, 0.1),
                                  font_size=50, bold=True, color=(1, 0, 0))
        self.root.add_widget(self.height_label)
        self.height_input = TextInput(hint_text='Height', pos_hint={'center_x': 0.55, 'center_y': 0.75},
                                      size_hint=(0.5, 0.1))
        self.root.add_widget(self.height_input)

        self.weight_label = Label(text='Weight:', pos_hint={'center_x': 0.2, 'center_y': 0.55}, size_hint=(0.3, 0.1),
                                  font_size=50, bold=True, color=(1, 0, 0))
        self.root.add_widget(self.weight_label)
        self.weight_input = TextInput(hint_text='Weight', pos_hint={'center_x': 0.55, 'center_y': 0.55},
                                      size_hint=(0.5, 0.1))
        self.root.add_widget(self.weight_input)

        self.calculate_button = Button(text='Calculate', pos_hint={'center_x': 0.5, 'center_y': 0.35},
                                       size_hint=(0.5, 0.1), bold=True, font_size=30,
                                       background_color=(0.2, 0.2, 0.2, 1), on_press=self.calculate_bmi)
        self.root.add_widget(self.calculate_button)

    def build(self):
        self.root = MDRelativeLayout(md_bg_color=(0.2, 0.2, 0.2, 1))
        self.title = 'Unit Converter'

        self.title_label = Label(text='Unit Converter', font_size=50, pos_hint={'center_x': 0.5, 'center_y': 0.95},
                                 size_hint=(1, 1))
        self.root.add_widget(self.title_label)

        self.bmi_button = Button(text='BMI', pos_hint={'center_x': 0.28, 'center_y': 0.75}, size_hint=(0.23, 0.17),
                                 bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1),
                                 on_press=self.bmi_converter)
        self.root.add_widget(self.bmi_button)

        self.length_button = Button(text='Length', pos_hint={'center_x': 0.68, 'center_y': 0.75},
                                    size_hint=(0.23, 0.17),
                                    bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.length_button)

        self.area_button = Button(text='Area', pos_hint={'center_x': 0.28, 'center_y': 0.50}, size_hint=(0.23, 0.17),
                                  bold=True, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
        self.root.add_widget(self.area_button)

        self.volume_button = Button(text='Volume', pos_hint={'center_x': 0.68, 'center_y': 0.50},
                                    size_hint=(0.23, 0.17),
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
