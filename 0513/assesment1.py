#------------------------
class Cave:
  __name: str
  __description: str
  __linked_caves: dict
  __character: 'Enemy | Friend'
  __item: 'Item'

  def __init__(self, name: str, description: str):
    self.__name = name
    self.__description = description
    self.__linked_caves = {}
    self.__character = None
    self.__item = None

  def get_name(self):
    return self.__name
  
  def get_description(self):
    return self.__description
  
  # def set_description(self, description):
  #   self.__description = description

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
    self.item = item

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
  
class Enemy:
  def __init__(self, name, description, conversation, weakness):
    self.name = name
    self.description = description
    self.conversation = conversation
    self.weakness = weakness
  
  def describe_enemy(self):
    print(f"{self.name} is here!")
    print(self.description)
  
  def fight_enemy(self, item):
    if item == self.weakness:
      print(f"You fend {self.name} off with the {item}")
      return True
    else:
      print(f"{self.name} swallows you, little wimp")
      return False

  def steal_from_enemy(self):
    print(f"You steal from {self.name}")

class Friend:
  def __init__(self, name, description, conversation):
    self.name = name
    self.description = description
    self.conversation = conversation
  
  def describe_friend(self):
    print(f"{self.name} is here!")
    print(self.name)
#------------------------
class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def describe_item(self):
    print(f"The [{self.name}] is here - {self.description}")

#Create caves
cavern = Cave("cavern"," A damp and dirty cave.")
grotto = Cave("Grotto", " A small cave with ancient graffiti.")
dungeon = Cave("Dungeon", " A large cave with a rack")

# link the caves
cavern.link_caves(grotto, 'west')
cavern.link_caves(dungeon, 'north')
dungeon.link_caves(grotto, 'east')

harry = Enemy("Harry", "A smelly Wumpus", "Hangry…Hanggrry", "vegemite")
josephine = Friend("Josephine", "A friendly bat", "Gidday.")

# Place characters
dungeon.set_character(harry)
grotto.set_character(josephine)

# Create items
vegemite = Item("vegemite", "A Wumpuses worst nightmare")
torch = Item("torch", "A light for the end of the tunnel")

grotto.set_item(vegemite)
dungeon.set_item(torch)



# game state
bag = []
current_cave = cavern
dead = False

# game loop
while not dead:
  print("\n")
  current_cave.describe_cave()

  character = current_cave.get_character()
  if character:
    if isinstance(character, Enemy):
      character.describe_enemy()
    elif isinstance(character, Friend):
      character.describe_friend()

  item = current_cave.get_item()
  if item:
    item.describe_item()

  command = input(">")

  if command in ['north', 'south', 'east', 'west']:
    current_cave = current_cave.move_cave(command)

  elif command == "talk":
    character = current_cave.get_character()
    if character and isinstance(character, Enemy | Friend):
      print(f"[{character.name} says]: {character.conversation}")

  elif command == "fight":
    character = current_cave.get_character()
    if character and isinstance(character, Enemy):
      print("What will you fight with?")
      
      fight_with = input()
      if fight_with in bag:
        # 
        if character.fight_enemy(fight_with):
          print("Bravo, hero you won the fight!")
          current_cave.set_character(None)
          
          if len(bag) == 0:
            print("Congratulations, you have survived another adventure!")
            
          dead = True
                
        else:
          print("Scurry home, you lost the fight.")
          print("That's the end of the game")
          dead = True
      else:
          print(f"You don't have a {fight_with}")
    else:
        print("There is no one here to fight with")
# 
  elif command == "pat":
    character = current_cave.get_character()
    if character and isinstance(character, Friend):
      print(f"{character.name} pats you back!")
    else:
      print("There is no one here to pat :(")
    
  elif command == "take":
    item = current_cave.get_item()

    if item:
      print(f"You put the {item.name} in your bag")
      
      bag.append(item.name)
      current_cave.set_item(None)
