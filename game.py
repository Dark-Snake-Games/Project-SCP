from DSEngine import *
from pygame import Vector2
from pygame.display import update
from sys import exit
from random import randint

from DSEngine.animated import AnimationSheet
default_title="Project: SCP"
click_sound = AudioPlayer("beep.mp3")
AUDIO_MAN = AudioManager(click=click_sound)

class SCP999(AnimatedSprite2D):
    def __init__(self, position=...):
        SCP999_1 = Image2D("Test.png")
        SCP999_2 = Image2D("Test1.png")
        walk_sheet = Spritesheet(0, SCP999_1,SCP999_1,SCP999_1,SCP999_1,SCP999_1,SCP999_1,SCP999_1,SCP999_1,SCP999_1,SCP999_1,SCP999_1,SCP999_1,\
                                SCP999_2,SCP999_2,SCP999_2,SCP999_2,SCP999_2,SCP999_2,SCP999_2,SCP999_2,SCP999_2,SCP999_2,SCP999_2,SCP999_2,)
        sheet = AnimationSheet(default=Image2D("Test.png"), walk=walk_sheet)
        self.last_secs = 0
        super().__init__(sheet, 1, position)
    
    def render(self, window: Window):
        if self.moving_towards and not self.playing:
            self.play_sheet("walk")
        if not self.moving_towards and self.playing:
            self.stop_playing()
        if int(window.seconds-self.last_secs) >= 25:
            rx = randint(0, window.size[0])
            ry = randint(0, window.size[1])
            pos = Vector2(rx, ry)
            self.move_towards(pos)
            self.last_secs = int(window.seconds)
        super().render(window)

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
            #exit(1)
            pass
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
    global default_title
    window = Window(title=default_title, fps=120, size=(1280, 720), bg=(100, 100, 100))
    audio_man = AudioManager()
    text = Text2D("SCP-999", position=Vector2(550, 0))
    scp = SCP999(position=Vector2(640, 360))
    text.init(window)
    scp.init(window)
    scp.move_towards(Vector2(0, 0))
    while window.running:
        keys = window.frame()
        if keys[27]:
            return 1

if __name__ == "__main__":
    main_menu()