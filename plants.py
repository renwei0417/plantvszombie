import pygame as pg
import Tool
from metainfo import *
#from  zombie_const import * 
from enum import Enum 
 


class Zombie:
    def __init__(self, kwargs):
        #血量和攻击相关的
        self.const_speed = kwargs[ZombieInitialStateKeyEnum.speed]
        self.const_health = kwargs[ZombieInitialStateKeyEnum.health]
        self.health = self.const_health
        self.speed = self.const_speed
        self.rect = kwargs[ZombieInitialStateKeyEnum.rect]
        self.damage = kwargs[ZombieInitialStateKeyEnum.damage]
        self.can_attack_all = kwargs[ZombieInitialStateKeyEnum.can_attack_all]
        #self.category = kwargs['category']
        self.attack_interval = kwargs[ZombieInitialStateKeyEnum.attack_interval]
        self.attack_type = kwargs[ZombieInitialStateKeyEnum.attack_type]

        #图像相关的
        self.image_refresh_time = kwargs[ZombieInitialStateKeyEnum.image_refresh_time]
        self.time_since_last_image_refresh =  0 
        self.last_attack_time = None 
        self.all_image = kwargs[ZombieInitialStateKeyEnum.all_image]

        self.image_index = 0
        self.image_name = ZombieImageEnum.Zombie  #初始设置为直接的僵尸
        self.images = []
        #self.is_under_attack = False 
        #self.name = name

        #被攻击状态相关的
        #这两个变量是僵尸中最重要的变量
        self.state = ZombieState.Normal
        #这个放置目前的状态
        self.under_attack_dict = {}
        #这个防止目前这一轮的状态
        self.temp_under_attack_dict = {}
        #这个防止目前的攻击状态列表
        self.under_attack_list= []

        self.id = kwargs[ZombieInitialStateKeyEnum.id]

        #时间相关的
        self.current_time =0
        self.previous_time =0 

        #移动相关的
        self.movement = 0.0 
        
    

    #攻击植物
    def update_time(self, current_time):
        self.previous_time = self.current_time
        self.current_time = current_time
    def attack(self, plants_list):
        # 如果现在还在攻击的过程中，并且攻击的过程中还没有

        if self.state == ZombieState.Dying:  #死了就不用攻击了把
            return 


        #接下来判断植物是否可以被攻击
        plants_attack_index_list = []
        for i in range(len(plants_list)):
            if self.rect.colliderect(plants_list[i].rect):
                if plants_list[i].get_state()!= PlantState.Dead: #没死就可以攻击了
                    plants_attack_index_list.append(i)
        #检测是否需要去攻击，那么现在可以攻击了吧，哈哈


        # if self.zombie_state == ZombieState.NormalAttack: #正常攻击状态的画那么如果时间还不到就算了，不要攻击了。
        #     if current_time - self.state.last_attack_time < self.state.attack_interval:
        #         self.state.current_time = current_time
        #         return

        #如果有植物可以攻击
        if len(plants_attack_index_list)>0:
            if self.state == ZombieState.Normal:
                if self.can_attack_all:
                    for i in plants_attack_index_list:
                        plants_list[i].accept_damage(self.damage, self.attack_type)
                    #self.state.is_attacking = True 
                    self.last_attack_time = current_time
                    self.state = ZombieState.NormalAttack
                    #是否需要更新时间呢？
                else:
                    single_plant_index = plants_attack_index_list[0]
                    plants_list[single_plant_index].accept_damage(self.damage, self.attack_type)
                    self.last_attack_time = self.current_time
                    self.state = ZombieState.NormalAttack
            if self.state == ZombieState.NormalAttack:
                if self.current_time - self.last_attack_time  < self.attack_interval:
                    return 
                else:
                    self.last_attack_time = self.current_time
                    single_plant_index = plants_attack_index_list[0]
                    plants_list[single_plant_index].accept_damage(self.damage, self.attack_type)
                    self.last_attack_time = self.current_time
                    self.state = ZombieState.NormalAttack


        else:
            if self.state == ZombieState.NormalAttack:
                self.state = ZombieState.Normal
        #self.state.current_time = current_time






         
        return 
    def accept_damage(self, damage, plantbullet_attack_type):
        #注意这个时候只是把状态记录下来，因为接下来需要看看
        self.temp_under_attack_dict[plantbullet_attack_type] = self.current_time
        self.health = self.health - damage
        if self.health <= 0:
            self.state = ZombieState.Dying
        #self.state.current_time = current_time          
        return
        #注意下面的函数应该智能自己来调用
    def set_under_attack_state(self):

        #首先要更新目前的状态，根据新的状态来设置
        for k, damage in self.temp_under_attack_dict.items():
            if k == AttackType.NormalAttack:
                self.under_attack_dict[k] = self.current_time
            if k == AttackType.IceAttack: #寒冰射手一类的
                self.under_attack_dict[AttackType.IceAttack] = self.current_time
            if k == AttackType.FireAttack:
                if AttackType.IceAttack in self.under_attack_dict:
                    self.under_attack_dict.pop(AttackType.IceAttack, None)
            if k == AttackType.BlindAttack:
                self.under_attack_dict[AttackType.BlindAttack] = self.current_time
            if k == AttackType.BoomAttack:
                if self.state ==ZombieState.Dying:
                    self.under_attack_dict[AttackType.BoomAttack] = self.current_time
                #else:
                    # do nothing right ?
        self.temp_under_attack_dict.clear()
        #解析来根据新的状态来设置最终的状态

        self.under_attack_list.clear()
        under_attack_keys = list(self.under_attack_dict.keys())
        for k in under_attack_keys:
            if k == AttackType.IceAttack or  k == AttackType.BlindAttack: #寒冰射手一类的
                if self.current_time- self.under_attack_dict[k] > Attack_Effect_Time[k]['time']:
                    self.under_attack_dict.pop(k,None) #注意已经结束了， BlindAttack也结束了。
                else:
                    self.under_attack_list.append(k)
            if k == AttackType.BoomAttack:
                if self.state== ZombieState.Dying:
                    self.under_attack_dict.append(AttackType.BoomAttack)

        return 
    def determine_image(self):
        current_image = self.image_name
        image_processing_list = [] 
        speed = 1.0 
        if self.state == ZombieState.Dying: #僵尸要死了
            if  AttackType.BoomAttack in self.under_attack_list: #这说明僵尸是被雷炸死的
                current_image = ZombieImageEnum.BoomDie
            else:
                current_image = ZombieImageEnum.ZombieDie
            if self.image_index == len(self.images)-1: #到了最后一帧了，设置直接僵尸死亡
                self.state = ZombieState.Dead
            speed = 0.0 
        else: #僵尸没有死，这个时候要判断僵尸的血量
            lose_head_suffix = ''
            if self.health <=  0.5 * self.const_health:
                lose_head_suffix = 'LostHead' 
            attack_suffix = ''
            if self.state == ZombieState.NormalAttack:
                attack_suffix = 'Attack' 

            current_image = ZombieImageEnum.Zombie + lose_head_suffix + attack_suffix          

            #接下来考虑僵尸的被攻击状态
            if AttackType.NormalAttack in self.under_attack_list:
                print()
            if AttackType.IceAttack in self.under_attack_list:
                speed =  Attack_Effect_Time[AttackType.IceAttack ]['speed']
            if AttackType.BlindAttack in self.under_attack_list:
                speed = Attack_Effect_Time[AttackType.BlindAttack]['speed']
            if self.state == ZombieState.NormalAttack:
                speed = 0.0



               
        return current_image, speed

        

        




    def update(self):
        #先减去血量
        #再更新一下状态
        self.set_under_attack_state()



        image_name, speed = self.determine_image()
        self.images = self.all_image[image_name]
        self.speed = speed * self.const_speed 

        if self.image_name == image_name: #相等的话那么则增加一个，当然得看时间
            if self.time_since_last_image_refresh > self.image_refresh_time:
                self.image_index =  (self.image_index + 1) % len(self.images)
                if self.image_index == len(self.images)-1 and self.state == ZombieState.Dying:
                    self.state = ZombieState.Dead
                self.time_since_last_image_refresh = 0 
            else:
                 self.time_since_last_image_refresh = self.time_since_last_image_refresh + self.current_time - self.previous_time
        else:
            self.image_index =0 
            self.time_since_last_image_refresh = 0
        self.image_name = image_name
        
            
    def get_state(self):
        return self.state  
    def rect(self):
        return self.rect

    def draw(self, Screen):
        #如果underattack，那么图像在一段时间内需要alpha变化一段时间，也就是仅此而已
        #如果受到了多重攻击，可能就需要做一些改变了
        time_interval = self.current_time - self.previous_time
        self.movement = self.movement + time_interval* self.speed
        #self.images = self.all_image[self.image_name]


        if self.movement > 1.0:
            self.movement = 0.0 
            self.rect.x = self.rect.x - 1
        
        if self.state != ZombieState.Dead:
             Screen.blit(self.images[self.image_index], self.rect)

        return 


class PeaShooterBullet:
    def __init__(self,dict):


        #攻击属性相关
        self.can_attack_all = dict[PeaShooterBulletStateKeyEnum.can_attack_all]
        self.speed = dict[PeaShooterBulletStateKeyEnum.speed]
        self.damage = dict[PeaShooterBulletStateKeyEnum.damage]
        self.attack_type = dict[PeaShooterBulletStateKeyEnum.attack_type]
        self.speed = dict[PeaShooterBulletStateKeyEnum.speed]
        #刷新和时间相关
        self.image_refresh_time = dict[PeaShooterBulletStateKeyEnum.image_refresh_time]
        self.previous_time = 0
        self.current_time =0
        self.state = BulletState.Normal
        self.rect = dict[PeaShooterBulletStateKeyEnum.rect]
        self.default_image = dict[PeaShooterBulletStateKeyEnum.default_image]

        self.time_since_last_image_refresh = 0 
        #图像相关
        self.all_image = dict[PeaShooterBulletStateKeyEnum.all_image]
        self.image_index = 0
        self.image_name = dict[PeaShooterBulletStateKeyEnum.default_image]
        self.images = self.all_image[self.image_name]

        self.movement = 0.0
        #
        self.id = dict[PeaShooterBulletStateKeyEnum.id]
        
    def update_time(self, current_time):
            self.previous_time = self.current_time
            self.current_time = current_time

    def is_alive(self):
        return self.state != BulletState.Dead

    def attack(self, zombie_list):
        if len(zombie_list) == 0: #没有僵尸，怎继续飞
            return 

        zombie_attack_list = []
        if self.state == BulletState.Attacking:
            return 
        for i in range(len(zombie_list)):
            if self.rect.colliderect(zombie_list[i].rect):
                #没死的话就可以攻击
                if zombie_list[i].get_state() !=  ZombieState.Dying:
                    zombie_attack_list.append(i)
            #检测是否需要去攻击，那么现在可以攻击了吧，哈哈
            if len(zombie_attack_list)>0 and self.state == BulletState.Normal :
                #现在找到第一个僵尸然后进行攻击
                zombie_to_attack = zombie_list[zombie_attack_list[0]]
                zombie_to_attack.accept_damage(self.damage, self.attack_type)
                self.state= BulletState.Attacking  #经过AttackTime后经过refresh的时间然后就要变了。
        return
    def determine_image(self):  #只需要设置好图像即可
        current_image= self.image_name
        if self.state == BulletState.Normal:
            current_image = self.default_image
        if self.state == BulletState.Attacking:
            current_image= BulletImageEnum.PeaNormalExplode
        return current_image

    def update(self):
        image_name = self.determine_image()
        self.images = self.all_image[self.image_name]
        if self.image_name == image_name: #相等的话那么则增加一个，当然得看时间
                if self.time_since_last_image_refresh > self.image_refresh_time:
                    self.image_index =  (self.image_index + 1) % len(self.images)
                    self.time_since_last_image_refresh = 0 
                    if self.state == BulletState.Attacking:
                        self.state = BulletState.Dead

                else:
                    self.time_since_last_image_refresh = self.time_since_last_image_refresh + self.current_time - self.previous_time
        else:
            self.image_index = 0 
            time_since_last_image_refresh= 0
        
        self.image_name = image_name
        
        if self.rect.x > Tool.Max_X or self.rect.y > Tool.Max_Y:
            self.state = BulletState.Dead

    def draw(self, Screen):
            #如果underattack，那么图像在一段时间内需要alpha变化一段时间，也就是仅此而已
            #如果受到了多重攻击，可能就需要做一些改变了
            time_interval = self.current_time - self.previous_time
            self.movement = self.movement + time_interval* self.speed


            if self.movement > 1.0:
                self.movement = 0.0 
                self.rect.x = self.rect.x + 1
            #print(self.rect.x, self.current_time)
            if self.state != BulletState.Dead:
                Screen.blit(self.images[self.image_index], self.rect)

            return 
    def get_state(self):
        return self.state


    

#对与这个射手来说可能需要来保持几个状态
# 1. 比如说是update_time
# 2. 
class Peashooter:
    def __init__(self, dict):
        self.can_shoot = True 
        self.attack_interval = dict[PeaShooterStateKeyEnum.attack_interval]
        self.previous_attack_time = - 100000
        self.health = dict[PeaShooterStateKeyEnum.health]
        self.attack_type = AttackType.NoAttack
        #时间相关的
        self.previous_time = 0
        self.current_time =0 
        self.time_since_last_image_refresh = 0
        



        #没啥相关的哈哈。
        self.default_image = dict[PeaShooterStateKeyEnum.default_Image]
        self.image_name = dict[PeaShooterStateKeyEnum.default_Image]
        self.all_image =dict[PeaShooterStateKeyEnum.all_image]
        self.images = self.all_image[self.default_image]
        self.rect = dict[PeaShooterStateKeyEnum.rect]
        self.image_refresh_time = dict[PeaShooterStateKeyEnum.image_refresh_time]
        self.image_index = 0

        #位置相关的

        #设置相关
        self.state = PlantState.Normal
        self.last_under_attack_time =  -1000
        #被攻击相关的
        self.under_attack_dict = {} #所有的累计攻击效果
        self.temp_under_attack_dict = {} #现在的攻击
        self.under_attack_list = [] #目前植物正在被遭受的攻击

        self.id = dict[PeaShooterStateKeyEnum.id]

        
    def update_time(self, current_time):
        self.previous_time = self.current_time
        self.current_time = current_time 

    #追忆他本身其实没法attack
    def attack(self, zombie_list):
        if self.current_time - self.previous_attack_time <  self.attack_interval: #说明已经可以攻击了
            return None
        else: # 发射豆子
            if len(zombie_list) == 0:
                return None 
            if self.default_image == PeashooterImage.Peashooter:
                bullet_state = GetBulletInitialState(BulletNames.PeaNormal)
                bullet_state[PeaShooterBulletStateKeyEnum.rect] =self.rect.copy()
                bullet = PeaShooterBullet(bullet_state)
                self.previous_attack_time = self.current_time
                return [bullet]
            if self.default_image == SnowPeaImage.SnowPea:
                bullet_state = GetBulletInitialState(BulletNames.PeaIce)
                bullet_state[PeaShooterBulletStateKeyEnum.rect] =self.rect.copy()
                bullet = PeaShooterBullet(bullet_state)
                self.previous_attack_time = self.current_time
                return [bullet]

        return None 
    #接受伤害
    def accept_damage(self, damage, zombie_attack_type):
        #注意这个时候只是把状态记录下来，因为接下来需要看看
        self.temp_under_attack_dict[zombie_attack_type] = self.current_time
        self.health = self.health - damage
        if self.health <=0.0 :
            self.state =  PlantState.Dead
        print(f'{self.id} under attack {self.current_time}')
        #self.state.current_time = current_time          
        return 
    def set_under_attack_state(self): 
        for k, v in self.temp_under_attack_dict.items():
            time  = v
            if k == ZombieAttackType.NormalAttack:
                self.under_attack_dict[k] = self.current_time
        self.temp_under_attack_dict.clear()

        self.under_attack_list.clear()

        for k, v in self.under_attack_dict.items():
            if k == ZombieAttackType.NormalAttack:
                if self.current_time - self.under_attack_state_dict[k] > Zombie_Attack_Effect_Time[k]['time']:
                    self.under_attack_dict.pop(k)
                else:
                    self.under_attack_list.append(k)
    def determine_image(self):
        current_image = self.image_name
        return current_image

    def update(self):
        image_name = self.determine_image()
        self.image_name = image_name
        self.images = self.all_image[self.image_name]
        if self.image_name == image_name: #相等的话那么则增加一个，当然得看时间
                if self.time_since_last_image_refresh > self.image_refresh_time:
                    self.image_index =  (self.image_index + 1) % len(self.images)
                    self.time_since_last_image_refresh = 0 

                else:
                    self.time_since_last_image_refresh = self.time_since_last_image_refresh + self.current_time - self.previous_time
        else:
            self.image_index = 0 
    def draw(self, Screen):
        if self.state != PlantState.Dead:
            Screen.blit(self.images[self.image_index], self.rect)
        Screen.blit(self.images[self.image_index], self.rect)
        return 
    def get_state(self):
        return self.state

    
    



