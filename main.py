import math

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class EntropyCalculatorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        self.input = TextInput(
            multiline=False, halign="right", readonly="True", font_size=30
        )
        main_layout.add_widget(self.input)

        self.output = TextInput(
            multiline=False, halign="right", readonly="True", font_size=30
        )
        main_layout.add_widget(self.output)

        buttons = [
            ["1", "2", "3", "0"],
            ["4", "5", "6", "."],
            ["7", "8", "9", "/"],
            ["Space", "Calculate", "Clear", "Backspace"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout

    def on_button_press(self, instance):
        current_text = self.input.text
        button_text = instance.text

        if button_text == "Clear":
            self.input.text = ""
        elif button_text == "Space":
            text = current_text.split(' ')[-1]
            if text != '':
                self.input.text = current_text + " "
        elif button_text == "Calculate":
            self.calculate(current_text)
        elif button_text == "Backspace":
            self.input.text = current_text[:-1]
        elif button_text == '.':
            text = current_text.split(' ')[-1]
            if text != '' and text[-1].isdigit():
                self.input.text = current_text + "."
        elif button_text == '/':
            text = current_text.split(' ')[-1]
            if text != '' and text[-1].isdigit():
                self.input.text = current_text + "/"
        else:
            new_text = current_text + button_text
            self.input.text = new_text

    def calculate(self, expression):
        text = ""
        string_probabilities = expression.strip().split(' ')
        probabilities = []
        for index, string_probability in enumerate(string_probabilities):
            probabilities.append(eval(string_probability))
            prob = probabilities[-1]
            text += "n(" + str(round(prob, 4)) + ")"
            if index != len(string_probabilities)-1:
                text += " + "

        entropy = EntropyCalculator(probabilities)
        h = entropy.calculate()
        text += "\nH = " + str(round(h, 4))
        self.output.text = text


class EntropyCalculator:
    def __init__(self, probabilities):
        self.probabilities = probabilities

    def calculate(self):
        result = 0
        for prob in self.probabilities:
            result += prob * math.log2(prob)

        return -result


if __name__ == '__main__':
    app = EntropyCalculatorApp()
    app.run()
