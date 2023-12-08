from DSEngine import *
from pygame import Vector2
from random import randint

class WasteCollector:
    def __init__(self, wfs) -> None:
        self.wfs = wfs
        self.waste = 0.0
        self.speed = 0.5
    
    def calc(self):
        if self.wfs.val >= 0+self.speed:
            self.waste += self.wfs.val-self.speed
            self.wfs.val -= self.speed

class WasteFiltrationSystem:
    def __init__(self, pump, max_cap: float) -> None:
        self.pump = pump
        self.cap = max_cap
        self.val = 0.0
        self.backed_up = False
    
    def calc(self):
        self.val += self.pump.usage/100
        if self.val > self.cap:
            self.backed_up = True
        else:
            self.backed_up = False

class WaterPump:
    def __init__(self, max_l: float):
        self.capacity = max_l
        self.usage = 0.0
        self.cannot_handle = False
        
    def calc(self):
        if self.usage > self.capacity/2:
            self.cannot_handle = True
        else:
            self.cannot_handle = False
        
class WaterUser:
    def __init__(self, pump, power: float):
        self.con = False
        self.consuming = power
        self.pump = pump

    def add_water_con(self):
        if not self.con:
            self.pump.usage += self.consuming
            self.con = True

    def remove_water_con(self):
        if self.con:
            self.pump.usage -= self.consuming
            self.con = False

class Generator:
    def __init__(self, total_power: float):
        self.total_pow = total_power
        self.consuming_power = 0.0
        self.blackout = False

    def calc(self):
        if self.consuming_power > self.total_pow/2:
            self.blackout = True
        else:
            self.blackout = False

class PowerUser:
    def __init__(self, generator, power: float):
        self.con = False
        self.consuming = power
        self.generator = generator

    def add_power_con(self):
        if not self.con:
            self.generator.consuming_power += self.consuming
            self.con = True

    def remove_power_con(self):
        if self.con:
            self.generator.consuming_power -= self.consuming
            self.con = False

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
