import time

from cave import Cave
from character import Friend, Enemy
from item import Item
from mini_game import Mini_game

#Create caves
cavern = Cave("cavern"," A damp and dirty cave.")
grotto = Cave("Grotto", " A small cave with ancient graffiti.")
dungeon = Cave("Dungeon", " A large cave with a rack")
# new caves
burrow = Cave("burrow", "A deep cave with lots of bugs")
hollow = Cave("hollow", "A small and deep cave under the ground")

# Link the caves
cavern.link_caves(grotto, 'west')
cavern.link_caves(dungeon, 'north')
dungeon.link_caves(grotto, 'east')

# link the new caves
burrow.link_caves(dungeon, 'north')
burrow.link_caves(hollow, 'east')

# Create characters
harry = Enemy("Harry", "A smelly Wumpus", "Hangry…Hanggrry", "vegemite")
josephine = Friend("Josephine",  "A friendly bat", "Gidday.",)

# new characters
edric = Enemy("Edric", "A huge Wunpus", "Bored..I'm so bored!", "ball")
alban = Friend("Alban", "A friendly bat", "Hi, how are ya? I’m so hungry :( ")

# Place characters
dungeon.set_character(harry)
grotto.set_character(josephine)

# place character
burrow.set_character(edric)
hollow.set_character(alban)
# Create items
vegemite = Item("vegemite", "A Wumpuses worst nightmare")
torch = Item("torch", "A light for the end of the tunnel")
# new items
bread = Item("bread", "A best combo with vegemite")
ball = Item("ball", "A big ball to attract the Wumpuses")

# Place items
grotto.set_item(vegemite)
dungeon.set_item(torch)

# place items
burrow.set_item(bread)
hollow.set_item(ball)

# --------------------------------------------------------

# game state
bag = []
current_cave = cavern
dead = False
import random

# game loop
print("\n" * 50)

title_lines = [
  "  ______     _                             __   _   _            _    _                                 ",
  "  | ___ \\   | |                           / _| | | | |          | |  | |                                ",
  "  | |_/ /___| |_ _   _ _ __ _ __     ___ | |_  | |_| |__   ___  | |  | |_   _ _ __ ___  _ __  _   _ ___ ",
  "  |    / _ \\| __| | | | '__| '_ \\   / _ \\|  _| | __| '_ \\ / _ \\ | |/\\| | | | | '_ ` _ \\| '_ \\| | | / __|",
  "  | |\\ \\  __| |_| |_| | |  | | | | | (_) | |   | |_| | | |  __/ \\  /\\  | |_| | | | | | | |_) | |_| \\__ \\",
  "  \\_| \\_\\___|\\__|\\__,_|_|  |_| |_|  \\___/|_|    \\__|_| |_|\\___|  \\/  \\/ \\__,_|_| |_| |_| .__/ \\__,_|___/",
  "                                                                                      | |               ",
  "                                                                                      |_|               ",
  "    The Torch of Truth                                                                                  "
]

for line in title_lines:
  print(line)
  time.sleep(0.5)

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
      print(f"[{character.get_name()} says]: {character.get_conversation()}")

  elif command == "fight":
    character = current_cave.get_character()
    if character and isinstance(character, Enemy):
      print("What will you fight with?")
      
      fight_with = input()
      if fight_with in bag:
      
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

  elif command == "pat":
    character = current_cave.get_character()
    if character and isinstance(character, Friend):
      print(f"{character.get_name()} pats you back!")
    else:
      print("There is no one here to pat :(")
    
  elif command == "take":
    item = current_cave.get_item()

    if item:
      print(f"You put the {item.get_name()} in your bag")
      
      bag.append(item.get_name())
      current_cave.set_item(None)
  # mini game(new features)
  elif command == "play":
    play_mini_game = input("Do you want to play a minigame? (yes/no)")

    if play_mini_game.lower() == "yes":
      mini_game = Mini_game()
      is_win = mini_game.play()

      if is_win:
        dead = True
      else:
        print("미니게임에서 졌지만 실제 게임은 플레이")
    else:
        print("Select again, please")
        dead = False


