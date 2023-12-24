from Option import Option


class Menu:
  def __init__(self, name: str, prompt: str, options: [Option]):
    self.name = name
    self.prompt = prompt
    self.options = options

  def menu_prompt(self) -> str:
    """
    Display the available options and their results and prompt the user for which
    option they will take.
    :return:        The text to be executed in the calling function.
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
    Find the last action in the menu.
    :return:    The text of the very last action in the options list.
    """
    return self.options[len(self.options) - 1].get_action()
