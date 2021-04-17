import pygame as pg
import Tool
#from  zombie_const import * 
from enum import Enum 


#Image_related ============================================

class PlantNameList(Enum):
        CherryBomb ="CherryBomb"
        Chomper ="Chomper"
        HypnoShroom ="HypnoShroom"
        IceShroom ="IceShroom"
        Jalapeno ="Jalapeno"
        Peashooter ="Peashooter"
        PotatoMine ="PotatoMine"
        PuffShroom ="PuffShroom"
        RepeaterPea ="RepeaterPea"
        ScaredyShroom ="ScaredyShroom"
        SnowPea ="SnowPea"
        Spikeweed ="Spikeweed"
        Squash ="Squash"
        Sun ="Sun"
        SunFlower ="SunFlower"
        SunShroom ="SunShroom"
        Threepeater ="Threepeater"
        WallNut ="WallNut"
PlantIsSingleImageDict = {PlantNameList.CherryBomb:True,
PlantNameList.Chomper:False,
PlantNameList.HypnoShroom:False,
PlantNameList.IceShroom:False,
PlantNameList.Jalapeno:False,
PlantNameList.Peashooter:True,
PlantNameList.PotatoMine:False,
PlantNameList.PuffShroom:False,
PlantNameList.RepeaterPea:True,
PlantNameList.ScaredyShroom:False,
PlantNameList.SnowPea:True,
PlantNameList.Spikeweed:False,
PlantNameList.Squash:False,
PlantNameList.Sun:True,
PlantNameList.SunFlower:True,
PlantNameList.SunShroom:False,
PlantNameList.Threepeater:True,
PlantNameList.WallNut:False
}

class CherryBombImage(Enum):
        CherryBomb ="CherryBomb"

class ChomperImage(Enum):
        Chomper ="Chomper"
        ChomperAttack ="ChomperAttack"
        ChomperDigest ="ChomperDigest"

class HypnoShroomImage(Enum):
        HypnoShroom ="HypnoShroom"
        HypnoShroomSleep ="HypnoShroomSleep"

class IceShroomImage(Enum):
        IceShroom ="IceShroom"
        IceShroomSleep ="IceShroomSleep"
        IceShroomSnow ="IceShroomSnow"
        IceShroomTrap ="IceShroomTrap"

class JalapenoImage(Enum):
        Jalapeno ="Jalapeno"
        JalapenoExplode ="JalapenoExplode"

class PeashooterImage(Enum):
        Peashooter ="Peashooter"

class PotatoMineImage(Enum):
        PotatoMine ="PotatoMine"
        PotatoMineExplode ="PotatoMineExplode"
        PotatoMineInit ="PotatoMineInit"

class PuffShroomImage(Enum):
        PuffShroom ="PuffShroom"
        PuffShroomSleep ="PuffShroomSleep"

class RepeaterPeaImage(Enum):
        RepeaterPea ="RepeaterPea"

class ScaredyShroomImage(Enum):
        ScaredyShroom ="ScaredyShroom"
        ScaredyShroomCry ="ScaredyShroomCry"
        ScaredyShroomSleep ="ScaredyShroomSleep"

class SnowPeaImage(Enum):
        SnowPea ="SnowPea"

class SpikeweedImage(Enum):
        Spikeweed ="Spikeweed"

class SquashImage(Enum):
        Squash ="Squash"
        SquashAim ="SquashAim"
        SquashAttack ="SquashAttack"

class SunImage(Enum):
        Sun ="Sun"

class SunFlowerImage(Enum):
        SunFlower ="SunFlower"

class SunShroomImage(Enum):
        SunShroom ="SunShroom"
        SunShroomBig ="SunShroomBig"
        SunShroomSleep ="SunShroomSleep"

class ThreepeaterImage(Enum):
        Threepeater ="Threepeater"

class WallNutImage(Enum):
        RedWallNutBowling ="RedWallNutBowling"
        RedWallNutBowlingExplode ="RedWallNutBowlingExplode"
        WallNut ="WallNut"
        WallNutBowling ="WallNutBowling"
        WallNut_cracked1 ="WallNut_cracked1"
        WallNut_cracked2 ="WallNut_cracked2"


class ZombieImages(Enum):
    Zombie = "Zombie"
    ZombieAttack = "ZombieAttack"
    ZombieDie = "ZombieDie"
    ZombieHead= "ZombieHead"
    ZombieLostHead = "ZombieLostHead"
    ZombieLostHeadAttack = "ZombieLostHeadAttack"
    BoomDie = "BoomDie"
    NewspaperZombie = "NewspaperZombie"
    NewspaperZombieAttack = "NewspaperZombieAttack"
    NewspaperZombieDie = "NewspaperZombieDie"
    NewspaperZombieLostHead = "NewspaperZombieLostHead"
    NewspaperZombieLostHeadAttack = "NewspaperZombieLostHeadAttack"
    NewspaperZombieNoPaper = "NewspaperZombieNoPaper"
    NewspaperZombieNoPaperAttack = "NewspaperZombieNoPaperAttack"
    FlagZombie = "FlagZombie"
    FlagZombieAttack = "FlagZombieAttack"
    FlagZombieLostHead = "FlagZombieLostHead"
    FlagZombieLostHeadAttack = "FlagZombieLostHeadAttack"
    ConeheadZombie = "ConeheadZombie"
    ConeheadZombieAttack = "ConeheadZombieAttack"

    BucketheadZombie = "BucketheadZombie"
    BucketheadZombie = "BucketheadZombieAttack"

class BulletImageType(Enum):
    PeaNormal = "PeaNormal"
    PeaNormalExplode = "PeaNormalExplode"
    PeaIce = "PeaIce"
    BulletMushRoom = "BulletMushRoom"
    BulletMushRoomExplode = "BulletMushRoomExplode"

#---------------zombie-------------plant----types #

class ZombieState(Enum):
    Normal =0
    NormalAttack =1
    Dying =2
    Dead = 3 
class BulletState(Enum):
    Normal = 0  #正常是这样
    Attacking = 1 #如果正在打击的话就这么打
    Dead = 2 #如果死掉了或者出界了就算是死掉了。


#================ImageName related ==============================




# this is related to the attack times# --------------#
class AttackType(Enum):
    NoAttack =0
    NormalAttack =1
    IceAttack = 2
    BlindAttack = 3
    StopAttack = 4
    BoomAttack = 5 
    FireAttack =6 

class ZombieAttackType:
    NoAttack = 0
    NormalAttack = 1

Zombie_Attack_Effect_Time = {
    ZombieAttackType.NoAttack: {'time':5, "speed":1.0},
    ZombieAttackType.NormalAttack:{'time':20,'speed':0.0}
}

Attack_Effect_Time = {
    AttackType.IceAttack: {'time':5, "speed":1.0},
    AttackType.BlindAttack:{'time':20,'speed':0.0},
    AttackType.StopAttack: {'time':20,'speed':0.0},
    AttackType.IceAttack: {'time':20, "speed":0.5},
    AttackType.BlindAttack:{'time':20,'speed':0.0}
}
# --- end of attack types  ----------------------#



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
        self.under_attack_dict = {}
        #这个防止目前这一轮的状态
        self.temp_under_attack_dict = {}
        #这个防止目前的攻击状态列表
        self.under_attack_list= {}
 
        self.image_index = 0
        self.image_name =ZombieImages.Zombie  #初始设置为直接的僵尸
        self.images = []
        #时间相关的
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
                if plants_list[i].state()!= PlantState.Dead: #没死就可以攻击了
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
        self.state.temp_under_attack_dict[plantbullet_attack_type] = self.current_time
        self.state.health = self.state.health - damage
        if self.state.health< = 0:
            self.zombie_state = ZombieState.Dying
        #self.state.current_time = current_time          
        return
        #注意下面的函数应该智能自己来调用
    def set_under_attack_state(self):

        #首先要更新目前的状态，根据新的状态来设置
        for k, damage in self.temp_under_attack_dict.items():
            if k == AttackType.NormalAttack:
                self.under_attack_dict[k] = self.state.current_time
            if k == AttackType.IceAttack: #寒冰射手一类的
                self.under_attack_dict[AttackType.IceAttack] = self.state.current_time
            if k == AttackType.FireAttack:
                if AttackType.IceAttack in self.under_attack_dict:
                    self.under_attack_dict.pop(AttackType.IceAttack, None)
            if k == AttackType.BlindAttack:
                self.under_attack_dict[AttackType.BlindAttack] = self.state.current_time
            if k == AttackType.BoomAttack:
                if self.state ==ZombieState.Dying:
                    self.under_attack_dict[AttackType.BoomAttack] = self.state.current_time
                #else:
                    # do nothing right ?
        self.temp_under_attack_dict.clear()
        #解析来根据新的状态来设置最终的状态

        self.under_attack_list.clear()
        for k, v in self.under_attack_dict.items():
            if k == AttackType.IceAttack or  k == AttackType.BlindAttack: #寒冰射手一类的
                if self.state.current_time- self.under_attack_dict[k] > Attack_Effect_Time[k]['time']:
                    self.under_attack_dict.pop(k,None) #注意已经结束了， BlindAttack也结束了。
                else:
                    self.zombie_under_attack_list.append(k)
            if k == AttackType.BoomAttack:
                if self.zombie_state== ZombieState.Dying:
                    self.under_attack_dict.append(AttackType.BoomAttack)

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

        

        




    def update(self):
        #先减去血量
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
        
            
    def is_alive(self):
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


class PeaShooterBullet:
    def __init__(self,dict):


        #攻击属性相关
        self.can_attack_all = dict['can_attack_all']
        self.speed = dict['speed']
        self.damage = dict['damage']
        self.attack_type = dict['attack_type']
        #刷新和时间相关
        self.image_refresh_time = dict['image_refresh_time']
        self.previous_time = 0
        self.current_time =0
        self.state = BulletState.Normal
        self.rect = dict['rect']
        #图像相关
        self.all_image = dict['all_image']
        self.image_index = 0
        self.image_name = dict['default_image']
        self.images = self.all_image[default_image]
        
    def update_time(self, current_time):
            self.previous_time = self.current_time
            self.current_time = current_time

    def is_alive(self):
        return self.state != BulletState.Dead

    def attack(self, zombie_list):
        if len(zombie_list) == 0: #没有僵尸，怎继续飞
            return 

        zombie_attack_list = []
            for i in range(len(zombie_list)):
                if self.rect.colliderect(zombie_list[i].rect):
                    if plants_list[i].state()!= PlantStateType.Dying: #没死就可以攻击了
                        zombie_attack_list.append(i)
            #检测是否需要去攻击，那么现在可以攻击了吧，哈哈
            if len(zombie_attack_list)>0 and self.state == BulletState.Normal 
                #现在找到第一个僵尸然后进行攻击
                zombie_to_attack = zombie_attack_list[0]
                zombie_to_attack.accept_damage(self.damage, self.attack_type)
                self.state= BulletState.Attacking  #经过AttackTime后经过refresh的时间然后就要变了。
            return
    def determine_image(self):  #只需要设置好图像即可
        current_image= self.image_name
        if self.state == BulletState.Normal:
            current_image = BulletImageType.PeaNormal
        if self.state == BulletState.Attacking:
            current_image= BulletImageType.PeaNormalExplode
        return current_image

    def update(self):
        image_name = self.determine_image()
        self.image_name = image_name
        self.images = self.all_image[self.image_name]
        if self.image_name == image_name: #相等的话那么则增加一个，当然得看时间
                if self.time_since_last_image_refresh > self.image_refresh_time:
                    self.image_index =  (self.image_index + 1) % len(self.images)
                    self.time_since_last_image_refresh = 0 
                    if self.state == BulletState.Attacking:
                        self.state == BulletState.Dead

                else:
                    self.time_since_last_image_refresh = self.time_since_last_image_refresh + self.current_time - self.previous_time
        else:
            self.image_index = 0 
        
        if self.rect.x > Tool.Max_X:
            self.state = BulletState.Dead

    def draw(self, Screen):
            #如果underattack，那么图像在一段时间内需要alpha变化一段时间，也就是仅此而已
            #如果受到了多重攻击，可能就需要做一些改变了
            time_interval = self.current_time - self.previous_time
            self.movement = self.movement + time_interval* self.speed


            if self.movement > 1.0:
                self.movement = 0.0 
                self.state.rect.x = self.state.rect.x + 1
            print(self.state.rect.x, self.current_time)
            Screen.blit(self.images[self.image_index], self.state.rect)

            return 

class PlantState(Enum):
    Normal =0, 
    Attacking = 1, 
    Sleeping = 2, 
    Dead = 3 

    

#对与这个射手来说可能需要来保持几个状态
# 1. 比如说是update_time
# 2. 
class Peashooter:
    def __init__(self, dict):
        self.can_shoot = True 
        self.attack_interval = dict['attack_interval']
        self.previous_attack_time = 0
        self.health = dict['health']
        self.attack_type = AttackType.NoAttack
        #时间相关的
        self.previous_time = - 10000
        self.current_time =0 
        self.images = dict['all_image']

        #没啥相关的哈哈。
        self.image_name = 'Peashooter'
        self.rect = dict['rect']

        #位置相关的
        self.rect = dict['rect']

        #设置相关
        self.state = PlantState.Normal
        self.last_under_attack_time =  -1000
        #被攻击相关的
        self.under_attack_dict = {} #所有的累计攻击效果
        self.temp_under_attack_dict = {} #现在的攻击
        self.under_attack_list = [] #目前植物正在被遭受的攻击

        
    def update_time(self, current_time):
        self.previous_time = self.current_time
        self.current_time = current_time 

    #追忆他本身其实没法attack
    def attack(self, zombie_list):
        if self.current_time - self.previous_attack_time >=  self.attack_interval:
            self.previous_attack_time = self.current_time
        
        return None 
    #接受伤害
    def accept_damage(self, damage, zombie_attack_time):
        #注意这个时候只是把状态记录下来，因为接下来需要看看
        self.temp_under_attack_dict[zombie_attack_time] = self.current_time
        self.health = self.health - damage
        if self.health <0 :
            self.state ==  PlantState.Dead
        #self.state.current_time = current_time          
        return 
    def set_under_attack_state(self): 
        for k, v in self.temp_under_attack_dict.items():
            time  = v
            if k == ZombieAttackType.NormalAttack
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
        return self.

        
        

    def is_alive(self):
        return self.zombie_state == PlantState.Dead 
        return 


    
    



