import questionary


class TextInputer:
    def __init__(self, prompt):
        self.prompt = prompt

    def show(self):
        input_text = questionary.text(self.prompt).ask()
        return input_text
