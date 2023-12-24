class Option:
    def __init__(self, prompt: str, action: str):
        """
        An option from a menu.
        :param prompt: Text that tells the user what that selection will do.
        :param action: Code that will be run in response to the choice from the menu selection.
        """
        self.prompt = prompt
        self.action = action

    def get_prompt(self):
        return self.prompt

    def get_action(self):
        return self.action

    def __str__(self):
        return f"prompt {self.prompt} calls for {self.action}"
