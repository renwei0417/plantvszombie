import pygame as pg
import Tool
from  zombie_const import * 
from enum import Enum 



class AttackType(Enum):
    NoAttack =0
    NormalAttack =1
    IceAttack = 2
    BlindAttack = 3
    StopAttack = 4
    BoomAttack = 5 
    FireAttack =6
class PlantStateType(Enum):
    Normal =0
    NormalAttack =1
    Dying =2
    Dead = 3 

class ZombieState(Enum):
    Normal =0
    NormalAttack =1
    Dying =2
    Dead = 3 
class ZombieUnderAttackState(Enum):
    NoAttack = 0 
    UnderNormalAttack = 1
    UnderIceAttack =2 
    UnderBoomAttack = 3
    UnderCreamAttack = 4

#定义一下把

# Image_Process_Function = {
#     Transparent : "Transparent",
#     TurnBlue : "TurnBlue"
# }



Attack_Effect_Time = {
    AttackType.IceAttack: {'time':5, "speed":1.0},
    AttackType.BlindAttack:{'time':20,'speed':0.0},
    AttackType.StopAttack: {'time':20,'speed':0.0},
    AttackType.IceAttack: {'time':20, "speed":0.5},
    AttackType.BlindAttack:{'time':20,'speed':0.0}
}




    
#     Freeze = 2
#     Blind =3 
#     Dying = 4



# class PeaShooterType(Enum):
#     Normal= 0
#     Ice = 1
#     #Fire = 2

# pea_bullet_damage ={PeaShooterType.Normal: 20,  PeaShooterType.Ice:20 }  #, PeaShooterType.Fire:40}




# def get_peashooter_bullet_image():
#     normal_image =Tool.All_Images['PeaNormal'].copy()
#     ice_image = Tool.All_Images['PeaIce'].copy()
#     normal_exploade = Tool.All_Images['PeaNormalExplode'].copy()

#     regular_image_dict = {PeaShooterType.Normal:[normal_image],  PeaShooterType.Ice:[ice_image]}
#     exploade_image_dict= {PeaShooterType.Normal:[normal_exploade],  PeaShooterType.Ice:[normal_exploade]}

#     return regular_image_dict, exploade_image_dict

# pea_bullet_normal_image, pea_bullet_explade_image = get_peashooter_bullet_image()


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
    def __init__(self, kwargs):
        self.const_speed = kwargs['speed']
        self.const_health = kwargs['health']
        self.health = self.const_health
        self.speed = self.const_speed
        self.rect = kwargs['rect']
        self.damage = kwargs['damage']
        self.category = kwargs['category']
        self.attack_interval = kwargs['attack_interval']
        self.attack_type = kwargs['attack_type']
        self.image_refresh_time = kwargs['image_refresh_time']
        self.time_since_last_image_refresh = 0 
        self.is_attacking = False
        self.last_attack_time = None 
        self.is_freezed = False  
        self.freeze_time = None 
        self.all_image = kwargs['all_image']
        self.can_attack_all = kwargs['can_attack_all']

        self.is_under_attack = False 
        self.under_attack_dict = {}  # category and time , 因为可以被攻击很多次，这时候需要被攻击后的策略。
        self.temp_attack_dict  = {}

        self.image_category = "Normal"
        self.image_index = 0
        self.is_alive = True   


class Zombie:
    def __init__(self, dict):
        #self.name = name
        self.state = ZombieInternalState(dict)

        self.all_zombie_image = dict['all_image']

        #这两个变量是僵尸中最重要的变量
        self.zombie_state = ZombieState.Normal
        #这个放置目前的状态
        self.zombie_under_attack_state_dict = {}
        #这个防止目前这一轮的状态
        self.temp_attack_dict = {}
        #这个防止目前的攻击状态列表
        self.zombie_under_attack_list= {}
 
        self.image_index = 0
        self.image_name =ZombieImages.Zombie  #初始设置为直接的僵尸
        self.images = []
        self.current_time =0
        self.previous_time =0 
        self.movement = 0.0 
    

    #攻击植物
    def update_time(self, current_time):
        self.previous_time = self.current_time
        self.current_time = current_time
    def attack(self, plants_list):
        # 如果现在还在攻击的过程中，并且攻击的过程中还没有

        if self.zombie_state == ZombieState.Dying:  #死了就不用攻击了把
            return 


        #接下来判断植物是否可以被攻击
        plants_attack_index_list = []
        for i in range(len(plants_list)):
            if self.rect.colliderect(plants_list[i].rect):
                if plants_list[i].state()!= PlantStateType.Die: #没死就可以攻击了
                    plants_attack_index_list.append(i)
        #检测是否需要去攻击，那么现在可以攻击了吧，哈哈


        # if self.zombie_state == ZombieState.NormalAttack: #正常攻击状态的画那么如果时间还不到就算了，不要攻击了。
        #     if current_time - self.state.last_attack_time < self.state.attack_interval:
        #         self.state.current_time = current_time
        #         return

        #如果有植物可以攻击
        if len(plants_attack_index_list)>0:
            if self.zombie_state == ZombieState.Normal:
                if self.state.can_attack_all:
                    for i in plants_attack_index_list:
                        plants_list[i].accept_damage(self.state.damage, self.state.attack_type, current_time)
                    #self.state.is_attacking = True 
                    self.state.last_attack_time = current_time
                    self.zombie_state = ZombieState.NormalAttack
                    #是否需要更新时间呢？
                else:
                    plants_list[0].accept_damage(self.state.damage, self.state.attack_type, current_time)
                    self.state.last_attack_time = self.current_image
                    self.zombie_state = ZombieState.NormalAttack
            if self.zombie_state == ZombieState.NormalAttack:
                if self.current_time - self.state.last_attack_time  < self.state.attack_interval:
                    return 
        else:
            if self.zombie_state == ZombieState.NormalAttack:
                self.zombie_state == ZombieState.Normal
        #self.state.current_time = current_time






         
        return 
    def accept_damage(self, damage, plantbullet_attack_type):
        #注意这个时候只是把状态记录下来，因为接下来需要看看
        self.state.temp_attack_dict[plantbullet_attack_type] = (self.current_time, damage)
        #self.state.current_time = current_time          
        return
#注意下面的函数应该智能自己来调用
    def reduce_health(self):
        for k,v in self.temp_attack_dict.items():
            time, damage = v
            self.state.health = self.state.health - damage
        
        if self.state.health <= 0:
            self.zombie_state = ZombieState.Dying 
        return 
    def set_zombie_under_attack_state(self):

        #首先要更新目前的状态，根据新的状态来设置
        for k, v in self.temp_attack_dict.items():
            time, damage = v
            if k == AttackType.NormalAttack:
                self.zombie_under_attack_state_dict[k] = self.state.current_time
            if k == AttackType.IceAttack: #寒冰射手一类的
                self.zombie_under_attack_state_dict[AttackType.IceAttack] = self.state.current_time
            if k == AttackType.FireAttack:
                # if AttackType.IceAttack in self.zombie_under_attack_state_dict:
                #     self.zombie_under_attack_state_dict.remove
                self.zombie_under_attack_state_dict.pop(AttackType.FireAttack, None)
            if k == AttackType.BlindAttack:
                self.zombie_under_attack_state_dict[AttackType.BlindAttack] = self.state.current_time
            if k == AttackType.BoomAttack:
                if self.state ==ZombieState.Dying:
                    self.zombie_under_attack_state_dict[AttackType.BoomAttack] = self.state.current_time
                #else:
                    # do nothing right ?
        #解析来根据新的状态来设置最终的状态

        remove_keys = []
        self.zombie_under_attack_list.clear()
        for k, v in self.zombie_under_attack_state_dict.items():
            if k == AttackType.IceAttack or k == k == AttackType.BlindAttack: #寒冰射手一类的
                if self.state.current_time- self.zombie_under_attack_state_dict[k] > Attack_Effect_Time[k]['speed']:
                    self.zombie_under_attack_state_dict.pop(k,None) #注意已经结束了， BlindAttack也结束了。
                else:
                    self.zombie_under_attack_list.append(k)
            if k == AttackType.BoomAttack:
                if self.zombie_state== ZombieState.Dying:
                    self.zombie_under_attack_list.append(AttackType.BoomAttack)

        return 
    def determine_image(self):
        current_image = self.image_name
        image_processing_list = [] 
        speed = 1.0 
        if self.zombie_state == ZombieState.Dying: #僵尸要死了
            if  AttackType.BoomAttack in self.zombie_under_attack_list: #这说明僵尸是被雷炸死的
                current_image = ZombieImages.BoomDie
            else:
                current_image = ZombieImages.ZombieDie
            if self.image_index == len(self.images)-1: #到了最后一帧了，设置直接僵尸死亡
                self.zombie_state = ZombieState.Dead
            speed = 0.0 
        else: #僵尸没有死，这个时候要判断僵尸的血量
            lose_head_suffix = ''
            if self.state.health <=  0.5 * self.state.const_speed:
                lose_head_suffix = 'LostHead' 
            attack_suffix = ''
            if self.zombie_state == ZombieState.NormalAttack:
                attack_suffix = 'Attack'           

            #接下来考虑僵尸的被攻击状态
            if AttackType.NormalAttack in self.zombie_under_attack_list:
                print()
            if AttackType.IceAttack in self.zombie_under_attack_list:
                speed =  Attack_Effect_Time[AttackType.IceAttack ]['speed']
            if AttackType.BlindAttack in self.zombie_under_attack_list:
                speed = Attack_Effect_Time[AttackType.BlindAttack]['speed']



               
        return current_image, speed

        

        




    def update(self, time):
        #先减去血量
        self.reduce_health()
        #再更新一下状态
        self.set_zombie_under_attack_state()



        image_name, speed = self.determine_image()
        self.images = self.state.all_image[image_name]
        self.state.speed = speed * self.state.const_speed 

        if self.image_name == image_name: #相等的话那么则增加一个，当然得看时间
            if self.state.time_since_last_image_refresh > self.state.image_refresh_time:
                self.image_index =  (self.image_index + 1) % len(self.images)
                self.state.time_since_last_image_refresh = 0 
            else:
                 self.state.time_since_last_image_refresh = self.state.time_since_last_image_refresh + self.current_time - self.previous_time
        else:
            self.image_index =0 
            self.state.time_since_last_image_refresh = 0
        
            
    def is_alive(self,damage):
        return self.zombie_state == ZombieState.Dead   
        return 
    def rect(self):
        return self.state.rect

    def draw(self, Screen):
        #如果underattack，那么图像在一段时间内需要alpha变化一段时间，也就是仅此而已
        #如果受到了多重攻击，可能就需要做一些改变了
        time_interval = self.current_time - self.previous_time
        self.movement = self.movement + time_interval* self.state.speed


        if self.movement > 1.0:
            self.movement = 0.0 
            self.state.rect.x = self.state.rect.x - 1
        print(self.state.rect.x, self.current_time)
        Screen.blit(self.images[self.image_index], self.state.rect)

        return 

