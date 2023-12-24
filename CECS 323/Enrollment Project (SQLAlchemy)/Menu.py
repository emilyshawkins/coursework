from Option import Option


class Menu:
    """
    Has a list of options that have a prompt and action. When the option is selected the corresponding action will
    happen.
    """

    def __init__(self, name: str, prompt: str, options: [Option]):
        self.name = name
        self.prompt = prompt
        self.options = options

    def menu_prompt(self) -> str:
        """
        Display all options, results, and prompts the user for an option.
        :return: The text that will execute in the calling function.
        """
        results: bool = False
        final: int = -1
        n_options: int = len(self.options)

        while not results:
            print(self.prompt)
            index: int = 0
            for option in self.options:
                index += 1
                print("%3d - %s" % (index, option.get_prompt()))

            try:
                final = int(input('-->'))
                if final < 1 or final > n_options:
                    print("Choice is out of range, try again.")
                    results = False
                else:
                    results = True
            except ValueError:
                print("Not a valid integer, try again.")

        return self.options[final - 1].get_action()

    def last_action(self):
        """
        Finds the last action in the menu, which is the option that will exit from the menu.
        :return: The text of the very last action in the options list.
        """
        return self.options[len(self.options) - 1].get_action()
