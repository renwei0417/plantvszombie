__author__ = 'marble_xu'

START_LEVEL_NUM = 1

ORIGINAL_CAPTION = 'Plant VS Zombies Game'

class Constant_Screen:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
class Constant_GridSize:
    GRID_X_LEN = 9
    GRID_Y_LEN = 5
    GRID_X_SIZE = 80
    GRID_Y_SIZE = 100
    GRID_OFFSET_X = 10
    GRID_OFFSET_Y = 0
    

class Constant_Color:
    WHITE        = (255, 255, 255)
    NAVYBLUE     = ( 60,  60, 100)
    SKY_BLUE     = ( 39, 145, 251)
    BLACK        = (  0,   0,   0)
    LIGHTYELLOW  = (234, 233, 171)
    RED          = (255,   0,   0)
    PURPLE       = (255,   0, 255)
    GOLD         = (255, 215,   0)
    GREEN        = (  0, 255,   0) 

SIZE_MULTIPLIER = 1.3

#GAME INFO DICTIONARY KEYS
CURRENT_TIME = 'current time'
LEVEL_NUM = 'level num'

class Constant_GameStates:
#STATES FOR ENTIRE GAME
    MAIN_MENU = 'main menu'
    LOAD_SCREEN = 'load screen'
    GAME_LOSE = 'game los'
    GAME_VICTORY = 'game victory'
    LEVEL = 'level'

    MAIN_MENU_IMAGE = 'MainMenu'
    OPTION_ADVENTURE = 'Adventure'
    GAME_LOOSE_IMAGE = 'GameLoose'
    GAME_VICTORY_IMAGE = 'GameVictory'

#MAP COMPONENTS
class Constant_MapComponent:
    BACKGROUND_NAME = 'Background'
    BACKGROUND_TYPE = 'background_type'
    INIT_SUN_NAME = 'init_sun_value'
    ZOMBIE_LIST = 'zombie_list'

    MAP_EMPTY = 0
    MAP_EXIST = 1

    BACKGROUND_OFFSET_X = 220
    MAP_OFFSET_X = 35
    MAP_OFFSET_Y = 100

#MENUBAR

class Constant_MenuBar:
    CHOOSEBAR_TYPE = 'choosebar_type'
    CHOOSEBAR_STATIC = 0
    CHOOSEBAR_MOVE = 1
    CHOSSEBAR_BOWLING = 2
    MENUBAR_BACKGROUND = 'ChooserBackground'
    MOVEBAR_BACKGROUND = 'MoveBackground'
    PANEL_BACKGROUND = 'PanelBackground'
    START_BUTTON = 'StartButton'
    CARD_POOL = 'card_pool'

    MOVEBAR_CARD_FRESH_TIME = 6000
    CARD_MOVE_TIME = 60

#PLANT INFO

class Constant_PlantInfo:
    PLANT_IMAGE_RECT = 'plant_image_rect'
    CAR = 'car'
    SUN = 'Sun'
    SUNFLOWER = 'SunFlower'
    PEASHOOTER = 'Peashooter'
    SNOWPEASHOOTER = 'SnowPea'
    WALLNUT = 'WallNut'
    CHERRYBOMB = 'CherryBomb'
    THREEPEASHOOTER = 'Threepeater'
    REPEATERPEA = 'RepeaterPea'
    CHOMPER = 'Chomper'
    CHERRY_BOOM_IMAGE = 'Boom'
    PUFFSHROOM = 'PuffShroom'
    POTATOMINE = 'PotatoMine'
    SQUASH = 'Squash'
    SPIKEWEED = 'Spikeweed'
    JALAPENO = 'Jalapeno'
    SCAREDYSHROOM = 'ScaredyShroom'
    SUNSHROOM = 'SunShroom'
    ICESHROOM = 'IceShroom'
    HYPNOSHROOM = 'HypnoShroom'
    WALLNUTBOWLING = 'WallNutBowling'
    REDWALLNUTBOWLING = 'RedWallNutBowling'

    PLANT_HEALTH = 5
    WALLNUT_HEALTH = 30
    WALLNUT_CRACKED1_HEALTH = 20
    WALLNUT_CRACKED2_HEALTH = 10
    WALLNUT_BOWLING_DAMAGE = 10

    PRODUCE_SUN_INTERVAL = 7000
    FLOWER_SUN_INTERVAL = 22000
    SUN_LIVE_TIME = 7000
    SUN_VALUE = 25

    ICE_SLOW_TIME = 2000

    FREEZE_TIME = 7500
    ICETRAP = 'IceTrap'

    plant_name_list = [SUNFLOWER, PEASHOOTER, SNOWPEASHOOTER, WALLNUT,
                   CHERRYBOMB, THREEPEASHOOTER, REPEATERPEA, CHOMPER,
                   PUFFSHROOM, POTATOMINE, SQUASH, SPIKEWEED,
                   JALAPENO, SCAREDYSHROOM, SUNSHROOM, ICESHROOM,
                   HYPNOSHROOM, WALLNUTBOWLING, REDWALLNUTBOWLING]
    plant_sun_list = [50, 100, 175, 50, 150, 325, 200, 150, 0, 25, 50, 100, 125, 25, 25, 75, 75, 0, 0]
    plant_frozen_time_list = [7500, 7500, 7500, 30000, 50000, 7500, 7500, 7500, 7500, 30000,
                          30000, 7500, 50000, 7500, 7500, 50000, 30000, 0, 0]
    all_card_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


#PLANT CARD INFO
class Constant_Card:
    CARD_SUNFLOWER = 'card_sunflower'
    CARD_PEASHOOTER = 'card_peashooter'
    CARD_SNOWPEASHOOTER = 'card_snowpea'
    CARD_WALLNUT = 'card_wallnut'
    CARD_CHERRYBOMB = 'card_cherrybomb'
    CARD_THREEPEASHOOTER = 'card_threepeater'
    CARD_REPEATERPEA = 'card_repeaterpea'
    CARD_CHOMPER = 'card_chomper'
    CARD_PUFFSHROOM = 'card_puffshroom'
    CARD_POTATOMINE = 'card_potatomine'
    CARD_SQUASH = 'card_squash'
    CARD_SPIKEWEED = 'card_spikeweed'
    CARD_JALAPENO = 'card_jalapeno'
    CARD_SCAREDYSHROOM = 'card_scaredyshroom'
    CARD_SUNSHROOM = 'card_sunshroom'
    CARD_ICESHROOM = 'card_iceshroom'
    CARD_HYPNOSHROOM = 'card_hypnoshroom'
    CARD_REDWALLNUT = 'card_redwallnut'

    all_card_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    card_name_list = [CARD_SUNFLOWER, CARD_PEASHOOTER, CARD_SNOWPEASHOOTER, CARD_WALLNUT,
                  CARD_CHERRYBOMB, CARD_THREEPEASHOOTER, CARD_REPEATERPEA, CARD_CHOMPER,
                  CARD_PUFFSHROOM, CARD_POTATOMINE, CARD_SQUASH, CARD_SPIKEWEED,
                  CARD_JALAPENO, CARD_SCAREDYSHROOM, CARD_SUNSHROOM, CARD_ICESHROOM,
                  CARD_HYPNOSHROOM, CARD_WALLNUT, CARD_REDWALLNUT]



#BULLET INFO

class Constant_Bullet:
    BULLET_PEA = 'PeaNormal'
    BULLET_PEA_ICE = 'PeaIce'
    BULLET_MUSHROOM = 'BulletMushRoom'
    BULLET_DAMAGE_NORMAL = 1

#ZOMBIE INFO

class Constant_Zombie:
    ZOMBIE_IMAGE_RECT = 'zombie_image_rect'
    ZOMBIE_HEAD = 'ZombieHead'
    NORMAL_ZOMBIE = 'Zombie'
    CONEHEAD_ZOMBIE = 'ConeheadZombie'
    BUCKETHEAD_ZOMBIE = 'BucketheadZombie'
    FLAG_ZOMBIE = 'FlagZombie'
    NEWSPAPER_ZOMBIE = 'NewspaperZombie'
    BOOMDIE = 'BoomDie'

    LOSTHEAD_HEALTH = 5
    NORMAL_HEALTH = 10
    FLAG_HEALTH = 15
    CONEHEAD_HEALTH = 20
    BUCKETHEAD_HEALTH = 30
    NEWSPAPER_HEALTH = 15

    ATTACK_INTERVAL = 1000
    ZOMBIE_WALK_INTERVAL = 70

    ZOMBIE_START_X = Constant_Screen.SCREEN_WIDTH + 50

class Constant_ZombieState:
    IDLE = 'idle'
    FLY = 'fly'
    EXPLODE = 'explode'
    ATTACK = 'attack'
    ATTACKED = 'attacked'
    DIGEST = 'digest'
    WALK = 'walk'
    DIE = 'die'
    CRY = 'cry'
    FREEZE = 'freeze'
    SLEEP = 'sleep'

#LEVEL STATE
class Constant_LevelState:
    CHOOSE = 'choose'
    PLAY = 'play'

#BACKGROUND
class Constant_BacckGround:
    BACKGROUND_DAY = 0
    BACKGROUND_NIGHT = 1

    

class Constant_PlantSelection_LayOut:
    

    Upper_Panel_Offset_X=0
    Upper_Panel_Offset_Y=0

    Upper_Panel_Flower_Offset_x=21
    Upper_Panel_Flower_Offset_Y_ToBottome=21

   


    Lower_Panel_Offset_X=0
    Lower_Panel_Offset_Y=87

    Button_Image_Offset_x=155
    Button_Image_Offset_y=547

    Lower_Panel_Card_Offset_x=22
    Lower_Panel_Card_Offset_Y=43
    Lower_Panel_Card_Scale=0.75


    Lower_PANEL_Card_Y_INTERNAL = 74
    Lower_PANEL_Card_X_INTERNAL = 53


    Upper_Panel_Card_Offset_X=78
    Upper_Panel_Card_Offset_y=8
    Upper_Panel_Card_Interval_X=55
    #note need to be changed.
    Upper_Panel_Card_Interval_Y=74

    CARD_LIST_NUM = 8





