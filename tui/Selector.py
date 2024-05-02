import questionary


class Selector:
    def __init__(self, prompt, options):
        self.prompt = prompt
        self.options = options

    def show(self):
        selected_option = questionary.select(self.prompt, choices=self.options).ask()
        return self.options.index(selected_option)
