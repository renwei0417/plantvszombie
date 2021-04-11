import pygame as pg
import Tool


class PlantAndBulletHarmType(Enum):
    NoAttack =0
    NormalAttack =1
    FreeAttack = 2
    BlindAttack = 3
    StopAttack = 4
class ZombieAttachType(Enum):
    NoAttack =0
    NormalAttack =1
# class PlantStateType(Enum):
#     Normal =0
#     Attacked =1
#     UnderAttack = 2
#     Dead = 3 
# class NormalZombieState(Enum):
#     Zombie = "Zombie"
#     BoomDie = "BoomDie"
#     ZombieAttack = "ZombieAttack"
#     ZombieDie = "ZombieDie"
#     ZombieHead = "ZombieHead"
#     ZombieLostHead = "ZombieLostHead"
#     ZombieLostHeadAttack = "ZombieLostHeadAttack"
    
#     Freeze = 2
#     Blind =3 
#     Dying = 4



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
    def __init__(self, name, images, x, y, width, height, health, current_time, dict):
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
        self.health = health
        self.refresh_time_interval = 100
        self.attack_interval = 10
    def handle_previous(self, time):
        return 
    def update(self, time):
        if time - self.current_time >= self.refresh_time_interval:
            self.image_index = (self.image_index +1) % len(self.images)
            self.current_time =time 
    def draw(self, Screen):
        Screen.blit(self.images[self.image_index], (self.rect.x, self.rect.y), (0, 0, self.rect.width, self.rect.height))
    def attack(self, zombie_list):
        return None # or a list if it generate bullet
    def accept_damage(self, harm_value, zombie_attack_type):
        self.health = self.health - harm_value
    def produce_sun(self):
        return None
    def is_alive(self):
        return True 

        
    # def can_attach(self):
    #     return False 



class BulletType(Enum):
    PeaShooter =0
    MushRoom = 1

class PeaShooterBullet:
    def __init__(self, x, y, width, height, speed, damage, category, normal_image, explode_images):

        self.name = name
        self.normal_image = normal_image
        self.explode_images = explode_images
        self.rect = pg.Rect(x, y, width, height)
        self.speed = speed 
        self.damage = damage 
        self.category = category 


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

    def attack(self, zombie_list):
        return 

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def handle_previous(self, time):
        return 


class ZombieInternalState:
    def __init__(self, **kwargs):
        self.const_speed = kwargs['speed']
        self.health = kwargs['health']
        self.speed = self.const_speed
        self.rect = kwargs['rect']
        self.damage = kwargs['damage']
        self.category = kwargs['category']
        self.attack_interval = kwargs['attack_interval']
        self.attack_type = kwargs['attack_type']
        self.image_refresh_time = kwargs['image_refresh_time']
        self.previous_image_refresh_time = None 
        self.previous_time = None 
        self.current_time = None 
        self.is_attacking = False
        self.last_attack_time = None 
        self.is_freezed = False  
        self.freeze_time = None 
        self.all_image = kwargs['all_image']
        self.can_attack_all = kwargs['can_attack_all']

        self.is_under_attack = False 
        self.under_attack_dict = {}  # category and time , 因为可以被攻击很多次，这时候需要被攻击后的策略。

        self.image_category = "Normal"
        self.image_index = 0
        self.is_alive = True   


class Zombie:
    def __init__(self, **kwargs):
        #self.name = name
        self.state = ZombieInternalState(kwargs)
        self.state_change = False 

    #攻击植物
    def attack(self, plants_list, current_time):
        # 如果现在还在攻击的过程中，并且攻击的过程中还没有

        if self.state.health <= 0:
            return 
        if self.state.is_attacking:
            if current_time - self.state.last_attack_time < self.state.attack_interval:
                self.state_change = False
                self.state.current_time = current_time
                return
            else:
                raise ValueError("现在还在攻击中，并且下次攻击时间还未到")
        else: #没有在攻击，这时候应该去看找一个可以攻击的植物来去攻击
            plants_attack_index_list = []
            for i in range(len(plants_list)):
                if self.rect.colliderect(plants_list[i].rect):
                    if plants_list[i].health() >0:
                        plants_attack_index_list.append(i)
            #检测是否需要去攻击，那么现在可以攻击了吧，哈哈
            if len(plants_attack_index_list)>0:
                if self.state.can_attack_all:
                    for i in plants_attack_index_list:
                        plants_list[i].accept_damage(self.state.damage, self.state.attack_type, current_time)
                    self.state.is_attacking = True 
                    self.state.last_attack_time = current_time
                    #是否需要更新时间呢？
                else:
                    plants_list[0].accept_damage(self.state.damage, self.state.attack_type, current_time)
                    self.state.is_attacking = True 
                    self.state.last_attack_time = current_time
                self.state_change = True 





         
        return 
    def rect(self):
        return self.state.rect
    def update(self, time):
        #主要的更新逻辑估计就在这儿，这里主要是来设置各种图像的应该画什么样的，就是根据state里边的来控制而已。

        return 
    def draw(self, Screen):
        #如果underattack，那么图像在一段时间内需要alpha变化一段时间，也就是仅此而已
        #如果受到了多重攻击，可能就需要做一些改变了
        return 
    def accept_damage(self, damage, plantbullet_attack_type, current_time):
        if damage >= 0:
            self.state.is_under_attack = True 
            self.state.last_under_attack_time = current_time
            self.state.health = self.state.health - damage 
            self.state_change.under_attack_dict[plantbullet_attack_type] = current_time

        return 
    def is_alive(self,damage):
        return self.state.is_alive
        

