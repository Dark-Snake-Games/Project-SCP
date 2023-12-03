from DSEngine import *
from pygame import Vector2
from pygame.display import update
from sys import exit
from random import randint
from scps import SCP999

from DSEngine.animated import AnimationSheet
default_title="Project: SCP"
click_sound = AudioPlayer("beep.mp3")
AUDIO_MAN = AudioManager(click=click_sound)

def main_menu():
    global default_title, AUDIO_MAN
    window = Window(title=default_title, fps=120, size=(1280, 720), bg=(100, 100, 100))
    text = Text2D("Project: SCP", position=Vector2(530, 150))
    play_button = Button("Play", position=Vector2(595, 280))
    exit_button = Button("Exit", position=Vector2(600, 380))
    text.init(window)
    play_button.init(window)
    exit_button.init(window)
    while window.running:
        keys = window.frame()
        if keys[27]:
            #exit(1)
            pass
        elif play_button.pressed:
            AUDIO_MAN.play("click")
            hub()
        elif exit_button.pressed:
            AUDIO_MAN.play("click")
            exit(1)
        else:
            #print("Nothing pressed")
            pass

def hub():
    global default_title, AUDIO_MAN
    window = Window(title=default_title, fps=120, size=(1280, 720), bg=(100, 100, 100))
    text = Text2D("Hub", position=Vector2(600, 0))
    scp999_button = Button("SCP-999", position=Vector2(0, 100))
    main_menu_button = Button("Main Menu", position=Vector2(0, scp999_button.rect.bottom-50))
    text.init(window)
    scp999_button.init(window)
    main_menu_button.init(window)
    while window.running:
        keys = window.frame()
        if keys[27]:
            AUDIO_MAN.play("click")
            return 1
        elif scp999_button.pressed:
            AUDIO_MAN.play("click")
            scp_999_scene()
        elif main_menu_button.pressed:
            AUDIO_MAN.play("click")
            main_menu()
        else:
            #print("Nothing pressed")
            pass

def scp_999_scene():
    global default_title, AUDIO_MAN
    window = Window(title=default_title, fps=120, size=(1280, 720), bg=(100, 100, 100))
    exit_button = Button("Hub", position=Vector2(0, 0))
    exit_button.rect.right = 720
    text = Text2D("SCP-999", position=Vector2(550, 0))
    scp = SCP999(position=Vector2(640, 360))
    text.init(window)
    scp.init(window)
    exit_button.init(window)
    scp.move_towards(Vector2(0, 0))
    while window.running:
        keys = window.frame()
        if exit_button.pressed:
            AUDIO_MAN.play("click")
            hub()
        if keys[27]:
            AUDIO_MAN.play("click")
            return 1

if __name__ == "__main__":
    main_menu()