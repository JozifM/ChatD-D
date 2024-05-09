import random
import openai
from io import BytesIO
from classes import *

def create_character():
    name = input("What is your character's name? ")
    race = input("What is your character's race? ")
    hp = random.randint(10, 20)
    strength = random.randint(1, 10)
    return Player(name, race, hp, strength)

def create_monster():
    name = random.choice(["Goblin", "Orc", "Troll"])
    hp = random.randint(5, 15)
    strength = random.randint(1, 8)
    loot = random.choice(["Gold", "Potion", "Sword"])
    return Monster(name, hp, strength, loot)

def combat(player, monster):
    print(f"You encounter a {monster}!")
    while player.is_alive() and monster.is_alive():
        player_damage = player.attack()
        monster_damage = monster.attack()
        print(f"{player.name} attacks the {monster.name} for {player_damage} damage!")
        monster.take_damage(player_damage)
        if not monster.is_alive():
            print(f"{player.name} defeats the {monster.name}!")
            loot = monster.drop_loot()
            if loot == "Gold":
                gold = random.randint(1, 10)
                player.add_gold(gold)
                print(f"You find {gold} gold coins.")
            else:
                print(f"You find a {loot}.")
            return True
        print(f"The {monster.name} attacks {player.name} for {monster_damage} damage!")
        player.take_damage(monster_damage)
    print(f"{player.name} is defeated by the {monster.name}. Game over.")
    return False

def init_scenario(init_dict):

    stash = [{'role': init_dict['role1'], 'content': init_dict['content1']}]

    init_list = [{'role': init_dict['role1'], 'content': init_dict['content1']},
               {'role': init_dict['role2'], 'content': init_dict['content2']}]

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=init_list
    )

    stash.append({'role': 'assistant', 'content': response.choices[0].message.content})

    image_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "create a description of this scenery in under 100 characters: " + response.choices[0].message.content}]
    )
    description = image_response.choices[0].message.content

    stash.append({'role': 'system', 'content': 'for every message you should only offer an extention to the story and let the user make every decision for the main character, responses should be no more than 200 characters'})

    return stash, response, description


def append_history(history, role, message):
    history.append({'role': role, 'content': message})

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=history
    )

    history.append({'role': 'assistant', 'content': response.choices[0].message.content})

    return history, response

def generate_image(description):
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="1024x1024"
        )
    
    return response['data'][0]['url']

def update_image(image ,description):

    img = image.open(BytesIO(response.content))
    print(img)

    response = openai.Image.create_variation(
        image = open(img, 'rb'),
        prompt=description,
        n=1,
        size="1024x1024"
        )
    
    return response['data'][0]['url']