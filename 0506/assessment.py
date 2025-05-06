# function to create a cave
def create_cave(name, description):
  return {
    'name': name,
    'description': description,
    'linked_caves': {},
    'character': {},
    'item': None
  }
# link caves together
def link_caves(cave1, cave2, direction):
  cave1['linked_caves'][direction] = cave2
  cave2['linked_caves'][direction_opposites[direction]] = cave1
    

def set_description(cave, description):
  cave['description'] = description
    
  
def get_name(cave):
  return cave['name']

def get_description(cave):
  return cave['description']

def set_character(cave, character):
  cave['character'] = character

def get_character(cave):
  return cave['character']

def set_item(cave, item):
  cave['item'] = item

def get_item(cave):
  return cave['item']

# describe the cave and show connected paths
def describe_cave(cave):
  print(get_description(cave))
  for direction in cave['linked_caves']:
    linked_cave = cave['linked_caves'][direction]
    print(f"The {get_name(linked_cave)} is {direction}")

# move to a different cave
def move_cave(current_cave, direction):
  if direction in current_cave['linked_caves']:
    return current_cave['linked_caves'][direction]
  else:
    print("You can't go that way")
    return current_cave
# create enemy
def create_enemy(name, description, conversation, weakness):
  return {
    'name': name,
    'description': description,
    'conversation': conversation,
    'weakness': weakness,
    }

# describe charcters
def describe_enemy(enemy):
  print(f"{enemy['name']} is here!")
  print(enemy['description'])

# fight the enemy
def fight_enemy(harry, item, current_cave):
  if item == harry['weakness']:
    print(f"You fend {harry['name']} off with the {item}")
    return True
  else:
    print(f"{harry['name']} swallows you, little wimp")
    return False

# create friend
def create_friend(name, description, conversation):
  return {
    'name': name,
    'description': description,
    'conversation': conversation,
    }

# describe charcters
def describe_friend(friend):
  print(f"{friend['name']} is here!")
  print(friend['description'])

def steal_from_enemy(enemy):
  print(f"You steal from {enemy['name']}")

# describe items
def describe_item(item):
  print(f"The [{item['name']}] is here - {item['description']}")

# descriptions of caves
cavern_description = " A damp and dirty cave."
grotto_description = " A small cave with ancient graffiti."
dungeon_description = " A large cave with a rack"

# names of caves
cavern_name = "Cavern"
grotto_name = "Grotto"
dungeon_name = "Dungeon"

# create cave instances
cavern = create_cave(cavern_name, cavern_description)
grotto = create_cave(grotto_name, grotto_description)
dungeon = create_cave(dungeon_name, dungeon_description)

# direction mapping for linking caves
direction_opposites = {
'north': 'south',
'south': 'north',
'east': 'west',
'west': 'east'
}

# link the caves
link_caves(cavern, grotto, 'west')
link_caves(cavern, dungeon, 'north')
link_caves(dungeon, grotto, 'east')

set_description(cavern, cavern_description)
set_description(grotto, grotto_description)
set_description(dungeon, dungeon_description)
# create characters
harry = create_enemy(
"Harry", 
"A smelly Wumpus",
"Hangry…Hanggrry",
"vegemite"
)

set_character(dungeon, harry)

josephine = create_friend(
"Josephine", 
"A friendly bat",
"Gidday."
)

set_character(grotto, josephine)

vegemite = {
'name': "vegemite",
'description': "A Wumpuses worst nightmare"
}

set_item(grotto, vegemite)

torch = {
'name': "torch",
'description': "A light for the end of the tunnel"
}

set_item(dungeon, torch)

# game state
bag = []
current_cave = cavern
dead = False

# not needed variables(didn't use it in the game code) 
# direction_opposites = {
#     'north': 'south',
#     'south': 'north',
#     'east': 'west',
#     'west': 'east'
#     }
# }

# game loop
while not dead: => while not True => while False
  print("\n")
  describe_cave(current_cave)

  character = get_character(current_cave)
  if character:
    if isinstance(character, dict) and 'conversation' in character:
      describe_enemy(character)
    elif isinstance(character, dict):
      describe_friend(character)

  item = get_item(current_cave)
  if item:
    describe_item(item)

  command = input(">")

  if command in ['north', 'south', 'east', 'west']:
    current_cave = move_cave(current_cave, command)

  elif command == "talk":
    character = get_character(current_cave)
    if character and isinstance(character, dict) and 'conversation' in character:
      print(f"[{character['name']} says]: {character['conversation']}")

  elif command == "fight":
    character = get_character(current_cave)
    if character and isinstance(character, dict) and 'weakness' in character:
      print("What will you fight with?")
      
      fight_with = input()
      if fight_with in bag:
        # 
        if fight_enemy(character, fight_with, current_cave):
          print("Bravo, hero you won the fight!")
          set_character(current_cave, None)
          
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
    character = get_character(current_cave)
    if character and isinstance(character, dict) and 'weakness' not in character:
      print(f"{character['name']} pats you back!")
    else:
      print("There is no one here to pat :(")
    
  elif command == "take":
    item = get_item(current_cave)

    if item:
      print(f"You put the {item['name']} in your bag")
      
      bag.append(item['name'])
      set_item(current_cave, None)