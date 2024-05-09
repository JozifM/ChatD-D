import random
import openai
from parameters import *
from functions import *
from classes import *

gpt_toggle = 1
intro = 1

def main():

    history = []

    openai.api_key = params['API_key']

    player = create_character()
    print(f"Welcome, {player.name}. Your stats are: {player}")

    if intro == 1:

        init_dict={'role1': 'system', 'content1': 'You are a Dungeons and Dragons dungeon master running a game based in the Lord Of the Rings universe',
        'role2':'assistant', 'content2': 'Set the scene for the main character named ' + player.name + ', who is a member of the ' + player.race + 'race, from his perspective. This should simply be a beginning of an adventure with minimal or no character development, It should be mysterious and under 200 characters'}

        history, response, description = init_scenario(init_dict)

        image_ref = generate_image(description)

        print("URL:")
        print(image_ref)
        print('------------------')

        print('--The Begninning--')
        print(response.choices[0].message.content)

    while True:
        print('Command: ')
        user_input = input()
        history, response = append_history(history, 'user', user_input)
        print(print(response.choices[0].message.content))
        image_ref = update_image(image_ref, response.choices[0].message.content)
        print(image_ref)
    '''player = create_character()
    print(f"Welcome, {player.name}. Your stats are: {player}")
    while True:
        monster = create_monster()
        if not combat(player, monster):
            break
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() != "y":
            break
    print(f"You ended the game with {player.gold} gold coins.")'''

if __name__ == "__main__":
    main()

