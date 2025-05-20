from character import Enemy, Friend
from item import Item

class Cave:
  def __init__(self, name: str, description: str):
    self.__name= name
    self.__description = description
    self.__linked_caves = {}
    self.__character = None
    self.__item = None
  
  def get_name(self):
    return self.__name
  
  def get_description(self):
    return self.__description

  def get_linked_caves(self):
    return self.__linked_caves
  
  def set_linked_caves(self, direction: str, cave: 'Cave'):
    self.__linked_caves[direction] = cave

  def get_character(self):
    return self.__character
  
  def set_character(self, character: 'Enemy | Friend'):
    self.__character = character

  def get_item(self):
    return self.__item

  def set_item(self, item: 'Item'):
    self.__item = item
  
  def link_caves(self, cave: 'Cave', direction: str):
    direction_opposites = {
      'north': 'south',
      'south': 'north',
      'east': 'west',
      'west': 'east'
    }
    self.__linked_caves[direction] = cave
    cave.set_linked_caves(direction_opposites[direction], self)
    
  def describe_cave(self):
    print(self.__description)
    for direction, cave in self.__linked_caves.items():
      print(f"The {cave.get_name()} is {direction}")

  def move_cave(self, direction: str):
    if direction in self.__linked_caves:
      return self.__linked_caves[direction]
    else:
      print("You can't go that way")
      return self
