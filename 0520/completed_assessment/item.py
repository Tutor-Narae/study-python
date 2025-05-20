class Item:
  def __init__(self, name: str, description: str):
    self.__name = name
    self.__description = description
  
  def describe_item(self):
    print(f"The [{self.__name}] is here - {self.__description}")

  def get_name(self):
    return self.__name
