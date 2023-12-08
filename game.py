from DSEngine import *
from pygame import Vector2
import pygame
from sys import exit
from random import randint
from scps import *
from DSEngine.animated import AnimationSheet
pygame.init()
default_title="Project: SCP"
click_sound = AudioPlayer("beep.mp3")
AUDIO_MAN = AudioManager(click=click_sound)
SCPS = {}
GENERATOR = Generator(100)
WPUMP = WaterPump(100)
WFS = WasteFiltrationSystem(WPUMP, 1000)
WCOLL = WasteCollector(WFS)

def global_frame():
    global GENERATOR, WPUMP, WFS, WCOLL
    GENERATOR.calc()
    WPUMP.calc()
    WFS.calc()
    WCOLL.calc()
    print(WFS.val, WCOLL.waste, WPUMP.usage)
    #print(GENERATOR.blackout)

def init():
    global SCPS
    SCPS = {"999": SCP999(Vector2(640, 360))}

def testing():
    global default_title, AUDIO_MAN, GENERATOR, WPUMP
    window = Window(title=default_title, fps=120, size=(1280, 720), bg=(100, 100, 100))
    sink = WaterUser(WPUMP, 32.0)
    sink.add_water_con()
    power_tracker = PowerUser(GENERATOR, 65)
    power_tracker.add_power_con()
    while window.running:
        keys = window.frame()
        if keys != None:
            global_frame()

def power_generator_room():
    global default_title, AUDIO_MAN, GENERATOR
    window = Window(title=default_title, fps=120, size=(1280, 720), bg=(100, 100, 100))
    text = Text2D("Power Generators", position=Vector2(530, 0))
    gen1 = Rect2D(1, position=Vector2(70, 70), size=Vector2(160, 160), color=(160, 160, 160))
    text1 = Text2D("Gen 1", position=Vector2(70, 70))
    exit_button = Button("Hub", position=Vector2(0, 0))
    power_tracker = PowerUser(GENERATOR, 65)
    power_tracker.add_power_con()
    text.init(window)
    exit_button.init(window)
    gen1.init(window)
    text1.init(window)
    while window.running:
        keys = window.frame()
        global_frame()
        if keys[27]:
            #exit(1)
            pass
        elif exit_button.pressed:
            AUDIO_MAN.play("click")
            return 1 
        else:
            #print("Nothing pressed")
            pass


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
            #return 1
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
    global default_title, AUDIO_MAN, SCPS
    window = Window(title=default_title, fps=120, size=(1280, 720), bg=(100, 100, 100))
    init()
    exit_button = Button("Hub", position=Vector2(0, 0))
    wall_left = Rect2D(1, position=Vector2(0, 0), size=Vector2(5, 720))
    wall_right = Rect2D(1, position=Vector2(1275, 0), size=Vector2(5, 720))
    wall_up = Rect2D(1, position=Vector2(0, 0), size=Vector2(1280, 5))
    wall_down = Rect2D(1, position=Vector2(0, 715), size=Vector2(1280, 5))
    text = Text2D("SCP-999", position=Vector2(550, 0))
    scp = SCPS["999"]
    text.init(window)
    scp.init(window)
    exit_button.init(window)
    wall_left.init(window)
    wall_right.init(window)
    wall_up.init(window)
    wall_down.init(window)
    rx = randint(0, window.size[0])
    ry = randint(0, window.size[1])
    pos = Vector2(rx, ry)
    scp.move_towards(pos)
    while window.running:
        keys = window.frame()
        global_frame()
        SCPS["999"] = scp
        if exit_button.pressed:
            AUDIO_MAN.play("click")
            return 1
        if keys[27]:
            AUDIO_MAN.play("click")
            return 1

if __name__ == "__main__":
    #main_menu()
    testing()
