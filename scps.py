from DSEngine import *
from pygame import Vector2
from random import randint

class SCP999(AnimatedSprite2D):
    def __init__(self, position=Vector2(0, 0)):
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