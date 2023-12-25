from DSEngine import *
from pygame import Vector2
from random import randint

class GameTime:
    def __init__(self, rt_milis):
        self.rt_milis = rt_milis
        self.rt_secs = rt_milis/1000
        self.hours = int(self.rt_secs/15)
        self.days = int(self.hours/24)
    
    def update_milis(self, milis):
        self.rt_milis += milis
        self.rt_secs = self.rt_milis/1000
        self.hours = int(self.rt_secs/15)
        self.days = int(self.hours/24)
    
    def to_json(self):
        data = {}
        data['rt_milis'] = self.rt_milis
        data['hours'] = self.hours
        data['days'] = self.days
        return data

    def import_json(self, data: dict):
        self.rt_milis = data['rt_milis']
        self.hours = data['hours']
        self.days = data['days']

def vector2json(vec: Vector2):
    data = {}
    data['x'] = vec.x
    data['y'] = vec.y
    return data

def json2vector(data: dict):
    vec = Vector2()
    vec.x = data['x']
    vec.y = data['y']
    return vec

class WasteCollector:
    def __init__(self, wfs) -> None:
        self.wfs = wfs
        self.waste = 0.0
        self.speed = 0.5
    
    def to_json(self):
        data = {}
        data["filt"] = self.wfs.to_json()
        data['waste'] = self.waste
        data['speed'] = self.speed
        return data
    
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
    
    def to_json(self):
        data = {}
        data['pump'] = self.pump.to_json()
        data['cap'] = self.cap
        data['val'] = self.val
        data['backed_up'] = self.backed_up
        return data
    
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
        self.users = []
    
    def to_json(self):
        data = {}
        data['cap'] = self.capacity
        data['usage'] = self.usage
        data['handle'] = self.cannot_handle
        data['users'] = []
        for user in self.users:
            data['users'].append(user.to_json())
        return data
        
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
    
    def to_json(self):
        data = {}
        data['con'] = self.con
        data['value'] = self.consuming
        return data

    def add_water_con(self):
        if not self.con:
            self.pump.users.append(self)
            self.pump.usage += self.consuming
            self.con = True

    def remove_water_con(self):
        if self.con:
            self.pump.users.remove(self)
            self.pump.usage -= self.consuming
            self.con = False

class Generator:
    def __init__(self, total_power: float):
        self.total_pow = total_power
        self.consuming_power = 0.0
        self.blackout = False
        self.users = []
    
    def to_json(self):
        data = {}
        data['power'] = self.total_pow
        data['power_usage'] = self.consuming_power
        data['blackout'] = self.blackout
        data['users'] = []
        for user in self.users:
            data['users'].append(user.to_json())
        return data

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
    
    def to_json(self):
        data = {}
        data['con'] = self.con
        data['pow'] = self.consuming
        return data

    def add_power_con(self):
        if not self.con:
            self.generator.users.append(self)
            self.generator.consuming_power += self.consuming
            self.con = True

    def remove_power_con(self):
        if self.con:
            self.generator.users.remove(self)
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
        self.move_pos = Vector2(0, 0)
        super().__init__(sheet, 1, position)
    
    def to_json(self):
        data = {}
        obj_pos = vector2json(self.position)
        mov_pos = vector2json(self.move_pos)
        data['pos'] = obj_pos
        data['move_pos'] = mov_pos
        return data
    
    def import_json(self, data: dict):
        self.position = json2vector(data['pos'])
        self.move_pos = json2vector(data['move_pos'])
    
    def render(self, window: Window):
        if self.moving_towards and not self.playing:
            self.play_sheet("walk")
        if not self.moving_towards and self.playing:
            self.stop_playing()
        if int(window.seconds-self.last_secs) >= 25:
            rx = randint(0, window.size[0])
            ry = randint(0, window.size[1])
            self.move_pos = Vector2(rx, ry)
            self.move_towards(self.move_pos)
            self.last_secs = int(window.seconds)
        super().render(window)
