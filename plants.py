import pygame as pg
import Tool




class PeaShooterType(Enum):
    Normal= 0
    Ice = 1
    #Fire = 2

pea_bullet_damage ={PeaShooterType.Normal: 20,  PeaShooterType.Ice:20 }  #, PeaShooterType.Fire:40}




def get_peashooter_bullet_image():
    normal_image =Tool.All_Images['PeaNormal'].copy()
    ice_image = Tool.All_Images['PeaIce'].copy()
    normal_exploade = Tool.All_Images['PeaNormalExplode'].copy()

    regular_image_dict = {PeaShooterType.Normal:[normal_image],  PeaShooterType.Ice:[ice_image]}
    exploade_image_dict= {PeaShooterType.Normal:[normal_exploade],  PeaShooterType.Ice:[normal_exploade]}

    return regular_image_dict, exploade_image_dict

pea_bullet_normal_image, pea_bullet_explade_image = get_peashooter_bullet_image()


class Plant:
    def __init__(self, name, images, x, y, width, height, current_time):
        self.name=name
        self.images = []
        for single_image in images:
            image_copy = Tool.get_surface_from_image_samesize(single_image)
            self.images.append(image_copy)
        #  self.x =x 
        # self.y =y 
        # self.width = width
        # self.height =height 

        self.rect = pg.Rect(x, y, width, height)
        # self.rect= （x, y, width, height)
        self.current_time = current_time
        self.image_index =0 
        self.refresh_time_interval = 100
        self.attack_interval = 10
    def update(self, time):
        if time - self.current_time >= self.refresh_time_interval:
            self.image_index = (self.image_index +1) % len(self.images)
            self.current_time =time 
    def draw(self, Screen):
        Screen.blit(self.images[self.image_index], (self.rect.x, self.rect.y), (0, 0, self.rect.width, self.rect.height))
        
    def can_attach(self):
        return False 



class BulletType(Enum):
    PeaShooter =0
    MushRoom = 1

class PeaShooterBullet:
    def __init__(self, x, y, width, height, speed, category, normal_image, explode_images):

        self.name = name
        self.images = 


    def update(self, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        if self.state == c.FLY:
            if self.rect.y != self.dest_y:
                self.rect.y += self.y_vel
                if self.y_vel * (self.dest_y - self.rect.y) < 0:
                    self.rect.y = self.dest_y
            self.rect.x += self.x_vel
            if self.rect.x > c.SCREEN_WIDTH:
                self.kill()
        elif self.state == c.EXPLODE:
            if(self.current_time - self.explode_timer) > 500:
                self.kill()

    def setExplode(self):
        self.state = c.EXPLODE
        self.explode_timer = self.current_time
        self.frames = self.explode_frames
        self.image = self.frames[self.frame_index]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

