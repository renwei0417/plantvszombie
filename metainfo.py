import pygame as pg
import Tool
#from  zombie_const import * 
from enum import Enum 


#Plants based  ============================================
class CherryBombImage:    
        CherryBomb ="CherryBomb"

class ChomperImage:
        Chomper ="Chomper"
        ChomperAttack ="ChomperAttack"      
        ChomperDigest ="ChomperDigest"      

class HypnoShroomImage:
        HypnoShroom ="HypnoShroom"
        HypnoShroomSleep ="HypnoShroomSleep"

class IceShroomImage:
        IceShroom ="IceShroom"
        IceShroomSleep ="IceShroomSleep"    
        IceShroomSnow ="IceShroomSnow"      
        IceShroomTrap ="IceShroomTrap"      

class JalapenoImage:
        Jalapeno ="Jalapeno"
        JalapenoExplode ="JalapenoExplode"

class PeashooterImage:
        Peashooter ="Peashooter"

class PotatoMineImage:
        PotatoMine ="PotatoMine"
        PotatoMineExplode ="PotatoMineExplode"
        PotatoMineInit ="PotatoMineInit"

class PuffShroomImage:
        PuffShroom ="PuffShroom"
        PuffShroomSleep ="PuffShroomSleep"

class RepeaterPeaImage:
        RepeaterPea ="RepeaterPea"

class ScaredyShroomImage:
        ScaredyShroom ="ScaredyShroom"
        ScaredyShroomCry ="ScaredyShroomCry"
        ScaredyShroomSleep ="ScaredyShroomSleep"

class SnowPeaImage:
        SnowPea ="SnowPea"

class SpikeweedImage:
        Spikeweed ="Spikeweed"

class SquashImage:
        Squash ="Squash"
        SquashAim ="SquashAim"
        SquashAttack ="SquashAttack"

class SunImage:
        Sun ="Sun"

class SunFlowerImage:
        SunFlower ="SunFlower"

class SunShroomImage:
        SunShroom ="SunShroom"
        SunShroomBig ="SunShroomBig"
        SunShroomSleep ="SunShroomSleep"

class ThreepeaterImage:
        Threepeater ="Threepeater"

class WallNutImage:
        RedWallNutBowling ="RedWallNutBowling"
        RedWallNutBowlingExplode ="RedWallNutBowlingExplode"
        WallNut ="WallNut"
        WallNutBowling ="WallNutBowling"
        WallNut_cracked1 ="WallNut_cracked1"
        WallNut_cracked2 ="WallNut_cracked2"

class PlantNameEnum:
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

PlantName2ImageList = {
PlantNameEnum.CherryBomb:["CherryBomb"],
PlantNameEnum.Chomper:["Chomper","ChomperAttack","ChomperDigest"],
PlantNameEnum.HypnoShroom:["HypnoShroom","HypnoShroomSleep"],
PlantNameEnum.IceShroom:["IceShroom","IceShroomSleep","IceShroomSnow","IceShroomTrap"],
PlantNameEnum.Jalapeno:["Jalapeno","JalapenoExplode"],
PlantNameEnum.Peashooter:["Peashooter"],
PlantNameEnum.PotatoMine:["PotatoMine","PotatoMineExplode","PotatoMineInit"],
PlantNameEnum.PuffShroom:["PuffShroom","PuffShroomSleep"],
PlantNameEnum.RepeaterPea:["RepeaterPea"],
PlantNameEnum.ScaredyShroom:["ScaredyShroom","ScaredyShroomCry","ScaredyShroomSleep"],
PlantNameEnum.SnowPea:["SnowPea"],
PlantNameEnum.Spikeweed:["Spikeweed"],
PlantNameEnum.Squash:["Squash","SquashAim","SquashAttack"],
PlantNameEnum.Sun:["Sun"],
PlantNameEnum.SunFlower:["SunFlower"],
PlantNameEnum.SunShroom:["SunShroom","SunShroomBig","SunShroomSleep"],
PlantNameEnum.Threepeater:["Threepeater"],
PlantNameEnum.WallNut:["RedWallNutBowling","RedWallNutBowlingExplode","WallNut","WallNutBowling","WallNut_cracked1","WallNut_cracked2"],
}


#------------------zombie_images------------------------#

class ZombieImageEnum:
        BucketheadZombie="BucketheadZombie"
        BucketheadZombieAttack="BucketheadZombieAttack"
        
        ConeheadZombie="ConeheadZombie"
        ConeheadZombieAttack="ConeheadZombieAttack"

        FlagZombie="FlagZombie"
        FlagZombieAttack="FlagZombieAttack"
        FlagZombieLostHead="FlagZombieLostHead"
        FlagZombieLostHeadAttack="FlagZombieLostHeadAttack"

        NewspaperZombie="NewspaperZombie"
        NewspaperZombieAttack="NewspaperZombieAttack"
        NewspaperZombieDie="NewspaperZombieDie"
        NewspaperZombieLostHead="NewspaperZombieLostHead"
        NewspaperZombieLostHeadAttack="NewspaperZombieLostHeadAttack"
        NewspaperZombieNoPaper="NewspaperZombieNoPaper"
        NewspaperZombieNoPaperAttack="NewspaperZombieNoPaperAttack"

        BoomDie="BoomDie"

        Zombie="Zombie"
        ZombieAttack="ZombieAttack"
        ZombieDie="ZombieDie"
        ZombieHead="ZombieHead"
        ZombieLostHead="ZombieLostHead"
        ZombieLostHeadAttack="ZombieLostHeadAttack"

ZombieImageArray=["BucketheadZombie","BucketheadZombieAttack","ConeheadZombie","ConeheadZombieAttack","FlagZombie","FlagZombieAttack","FlagZombieLostHead","FlagZombieLostHeadAttack","NewspaperZombie","NewspaperZombieAttack","NewspaperZombieDie","NewspaperZombieLostHead","NewspaperZombieLostHeadAttack","NewspaperZombieNoPaper","NewspaperZombieNoPaperAttack","BoomDie","Zombie","ZombieAttack","ZombieDie","ZombieHead","ZombieLostHead","ZombieLostHeadAttack"]

class ZombieName:
        Zombie = "Zombie"
        NewspaperZombie = "NewspaperZombie"
        FlagZombie = "FlagZombie"
        ConeheadZombie = "ConeheadZombie"
        BucketheadZombie = "BucketheadZombie"

#正常的僵尸



#-------------------------------------------------------------------------------------------

class BulletImageEnum:
        BulletMushRoom="BulletMushRoom"
        BulletMushRoomExplode="BulletMushRoomExplode"
        PeaIce="PeaIce"
        PeaNormal="PeaNormal"
        PeaNormalExplode="PeaNormalExplode"
BulletImagesArray=["BulletMushRoom","BulletMushRoomExplode","PeaIce","PeaNormal","PeaNormalExplode"]

class BulletNames:
        PeaNormal= "PeaNormal"
        PeaIce = "PeaIce"
        MushRoom = 'MushRoom'

def get_zombie_image():
    dict = {}
    for image_name in ZombieImageArray:
        images = Tool.All_Images[image_name]
        dict[image_name] =[ image.copy() for image in images ]
    return dict 

def get_plant_image(plant_name):
    dict = {}
    plant_image_names = PlantName2ImageList[plant_name]
    for image_name in plant_image_names:
        images = Tool.All_Images[image_name]
        dict[image_name] =[ image.copy() for image in images ]
    return dict 

def get_bullet_image():
    dict = {}
    for image_name in BulletImagesArray:
        images = Tool.All_Images[image_name]
        dict[image_name] =[ image.copy() for image in images ]
    return dict 



#---------------zombie-------------plant----types #

class ZombieState:
    Normal =0
    NormalAttack =1
    Dying =2
    Dead = 3 
class BulletState:
    Normal = 0  #正常是这样
    Attacking = 1 #如果正在打击的话就这么打
    Dead = 2 #如果死掉了或者出界了就算是死掉了。

class PlantState:
        Normal = 0
        Attacking = 1
        Dead = 2
#================ImageName related ==============================




# this is related to the attack times# --------------#
class AttackType:
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


#initialization state --- for every zombie
# ----------------------------------------------------------------------------------S

class ZombieInitialStateKeyEnum:
        speed ='speed'
        health ='health'
        attack_interval = 'attack_interval'
        image_refresh_time = 'image_refresh_time'
        all_image = 'all_image'
        attack_type= 'attack_type'
        can_attack_all = 'can_attack_all'
        rect = 'rect'
        damage= 'damage'
        id = 'id'

zombie_state_dict ={ZombieInitialStateKeyEnum.speed:0.01,
                ZombieInitialStateKeyEnum.health:12.0,
                ZombieInitialStateKeyEnum.damage: 1.0,
                ZombieInitialStateKeyEnum.attack_interval:10,
                ZombieInitialStateKeyEnum.image_refresh_time:100,
                ZombieInitialStateKeyEnum.all_image: get_zombie_image(),
                ZombieInitialStateKeyEnum.attack_type: ZombieAttackType.NormalAttack,
                ZombieInitialStateKeyEnum.can_attack_all:False} 

class ConeHeadZombieInitialStateKeyEnum:
        speed ='speed'
        health ='health'
        attack_interval = 'attack_interval'
        image_refresh_time = 'image_refresh_time'
        all_image = 'all_image'
        attack_type= 'attack_type'
        can_attack_all = 'can_attack_all'
        rect = 'rect'
        damage = 'damage'
        id = 'id'

cone_head_zombie_state = {ConeHeadZombieInitialStateKeyEnum.speed:0.01,
                ConeHeadZombieInitialStateKeyEnum.health:20.0,
                ConeHeadZombieInitialStateKeyEnum.damage: 1.0,
                ConeHeadZombieInitialStateKeyEnum.attack_interval:10,
                ConeHeadZombieInitialStateKeyEnum.image_refresh_time:100,
                ConeHeadZombieInitialStateKeyEnum.all_image: get_zombie_image(),
                ConeHeadZombieInitialStateKeyEnum.attack_type: ZombieAttackType.NormalAttack,
                ConeHeadZombieInitialStateKeyEnum.can_attack_all:False}

Zombie_IntialState= {ZombieName.Zombie: zombie_state_dict,
ZombieName.ConeheadZombie: cone_head_zombie_state

} 



# initialization state for plants
#-----------------------------------------------------------------------------------

class PeaShooterStateKeyEnum:
        attack_interval='attack_interval'
        health = 'health'
        all_image ='all_image'
        attack_type = 'attack_type'
        default_Image = 'default_Image'
        rect = 'rect'
        image_refresh_time = 'image_refresh_time'
        speed = 'speed'
        id = 'id'

pea_shooter_state_dict ={
       PeaShooterStateKeyEnum.attack_interval:5000,
       PeaShooterStateKeyEnum.health:10,
       PeaShooterStateKeyEnum.all_image:get_plant_image(PlantNameEnum.Peashooter),
       PeaShooterStateKeyEnum.attack_type:AttackType.NoAttack,
       PeaShooterStateKeyEnum.default_Image : PeashooterImage.Peashooter,
       PeaShooterStateKeyEnum.image_refresh_time : 40,
       PeaShooterStateKeyEnum.speed : 0.0
}

snow_pea_shooter_state_dict ={
       PeaShooterStateKeyEnum.attack_interval:5000,
       PeaShooterStateKeyEnum.health:10,
       PeaShooterStateKeyEnum.all_image:get_plant_image(PlantNameEnum.SnowPea),
       PeaShooterStateKeyEnum.attack_type:AttackType.NoAttack,
       PeaShooterStateKeyEnum.default_Image : SnowPeaImage.SnowPea,
       PeaShooterStateKeyEnum.image_refresh_time : 40,
       PeaShooterStateKeyEnum.speed : 0.0
}


Plants_IntialState ={PlantNameEnum.Peashooter:pea_shooter_state_dict

}
#-----------------------------------------------------------------------------------

#initialize state for bullets


class PeaShooterBulletStateKeyEnum:
        attack_interval='attack_interval'
        health = 'health'
        all_image ='all_image'
        attack_type = 'attack_type'
        can_attack_all = 'can_attack_all'
        speed= 'speed'
        image_refresh_time = 'image_refresh_time'
        default_image= 'default_image'
        damage = 'damage'
        rect = 'rect'
        id = 'id'

peashooter_bullet_initial_dict = {PeaShooterBulletStateKeyEnum.can_attack_all:False,
PeaShooterBulletStateKeyEnum.speed:0.3,
PeaShooterBulletStateKeyEnum.damage:10,
PeaShooterBulletStateKeyEnum.attack_type:AttackType.NormalAttack,
PeaShooterBulletStateKeyEnum.image_refresh_time: 500,
PeaShooterBulletStateKeyEnum.all_image:get_bullet_image(),
PeaShooterBulletStateKeyEnum.default_image:BulletImageEnum.PeaNormal

}

peashooter_ice_bullet_initial_dict= {PeaShooterBulletStateKeyEnum.can_attack_all:False,
PeaShooterBulletStateKeyEnum.speed:0.1,
PeaShooterBulletStateKeyEnum.damage:2,
PeaShooterBulletStateKeyEnum.attack_type:AttackType.IceAttack,
PeaShooterBulletStateKeyEnum.image_refresh_time: 500,
PeaShooterBulletStateKeyEnum.all_image:get_bullet_image(),
PeaShooterBulletStateKeyEnum.default_image:BulletImageEnum.PeaIce

}


Bullet_InitialState ={ BulletNames.PeaNormal:peashooter_bullet_initial_dict,
BulletNames.PeaIce:peashooter_ice_bullet_initial_dict}






#below should be the function for creating zombies-----------------------------------------------------------------------------------------

global_zombie_id = 0
global_bullet_id = 0
global_plant_id =0

def GetZombieInitialState(zombie_name):
        global global_zombie_id
        if zombie_name not in Zombie_IntialState:
                raise ValueError(f'zombie type {zombie_name} is not supported')
        else:
                id = global_zombie_id
                global_zombie_id = global_zombie_id + 1
                dict = Zombie_IntialState[zombie_name]
                dict[ZombieInitialStateKeyEnum.id] = id
                return dict
def GetBulletInitialState(bullet_name):
        global global_bullet_id
        if bullet_name not in Bullet_InitialState:
                raise ValueError(f'bullet type {zombie_name} is not supported')
        else:
                id = global_bullet_id
                global_bullet_id = global_bullet_id + 1
                dict =  Bullet_InitialState[bullet_name]
                dict[PeaShooterBulletStateKeyEnum.id] = id
                return dict 
def GetPlantInitialState(plant_name):
        global global_plant_id
        if plant_name not in Plants_IntialState:
                raise ValueError(f'plant type {plant_name} is not supported')
        else:
                id = global_plant_id
                global_plant_id = global_plant_id + 1
                dict =  Plants_IntialState[plant_name]
                dict[PeaShooterStateKeyEnum.id] = id 
                return dict 

# below are boundary
Straight_Bullet_X_Max= 800
Straight_Bullet_Y_Max = 600



