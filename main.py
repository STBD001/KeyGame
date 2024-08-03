import time
import math
from random import randint

GAME_WIDTH=10
GAME_HEIGHT=10
player_x=0
player_y=0
player_found_key=False
key_x=randint(0, GAME_WIDTH)
key_y=randint(0, GAME_HEIGHT)
steps=0
distance_before_move = math.sqrt((key_x-player_x)**2+(key_y-player_y)**2)

while not player_found_key:
    steps+=1
    print("Go in the directions W/A/S/D: ")
    move=input("Your option is: ")
    match move.lower():
        case 'w':
            player_y+=1
            if player_y > GAME_HEIGHT:
                player_y=GAME_HEIGHT
                print("you are at the top")
        case 'a':
            player_x-=1
            if player_x < 0:
                player_x = 0
                print("you are on the left side")
        case 's':
            player_y-=1
            if player_y < 0:
                player_y = 0
                print("you are at the bottom")
        case 'd':
            player_x+=1
            if player_x >GAME_WIDTH:
                player_x=GAME_WIDTH
                print("you are on the right side")
        case 'q':
            quit()
    print(player_x, player_y)

    if player_x == key_x and player_y==key_y:
        print("Congratulations, you won")
        print(f"you needed {steps} moves")
        time.sleep(2)
        quit()

    distance_after_move = math.sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_before_move > distance_after_move:
        print("closer")
    else:
        print("along")

    distance_before_move=distance_after_move
    print(player_x, player_y)