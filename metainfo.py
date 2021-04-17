import pygame as pg
import Tool
#from  zombie_const import * 
from enum import Enum 


#Plants based  ============================================
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

class PlantNameEnum(Enum):
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

class ZombieImageEnum(Enum):
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
class BulletImageEnum(Enum):
        BulletMushRoom="BulletMushRoom"
        BulletMushRoomExplode="BulletMushRoomExplode"
        PeaIce="PeaIce"
        PeaNormal="PeaNormal"
        PeaNormalExplode="PeaNormalExplode"
BulletImagesArray=["BulletMushRoom","BulletMushRoomExplode","PeaIce","PeaNormal","PeaNormalExplode"]

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

