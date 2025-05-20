class Enemy:
  def __init__(self, name: str, description: str, conversation: str, weakness: str):
    self.__name = name
    self.__description = description
    self.__conversation = conversation
    self.__weakness = weakness
  
  def describe_enemy(self):
    print(f"{self.__name} is here!")
    print(self.__description)
  
  def fight_enemy(self, item):
    if item == self.__weakness:
      print(f"You fend {self.__name} off with the {item}")
      return True
    else:
      print(f"{self.__name} swallows you, little wimp")
      return False

  def steal_from_enemy(self):
    print(f"You steal from {self.__name}")

  def get_conversation(self):
    return self.__conversation
  
  def get_name(self):
    return self.__name

# ---------------------------------------------
class Friend:
  __name: str
  __description: str
  __conversation: str
  
  def __init__(self, name: str, description: str, conversation: str):
    self.__name = name
    self.__description = description
    self.__conversation = conversation
  
  def describe_friend(self):
    print(f"{self.__name} is here!")
    print(self.__description)

  def get_conversation(self):
    return self.__conversation

  def get_name(self):
    return self.__name