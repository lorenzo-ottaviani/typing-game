from .play_game import *

def handle_key_press(key, objects):
        print(f"key pressed: {key}\nobjects: {objects[0]}")

        # if key == 13 or key == 27:  # 13: 'enter', 27: 'esc'
        #         game_state = "menu"
        #         print(f"event key: {key}, game state:{game_state} ")
        #         SCREEN.blit(BACKGROUND, (0, 0)) 

        try:
            key_char = chr(key).upper()
        except ValueError:
            print("not a letter")
        for object in objects:
             if key_char == "letter":
                print(f"get sliced")
        # return