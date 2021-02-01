import pygame as pg
import os 
import constant as C
import Tool


class Card:
    def __init__(self, grid, index, name, image, cost, freeze_time, current_time):
        self.grid=grid
        self.index=index
        self.name=name

        dark_image= image.copy()
        # dard image is used when clickable
        dark_image =dard_image.set_alpha(128)
        
        self.image= [image.copy(), dark_image]
        self.freeze_time = freeze_time
        self.current_time = None
        self.click_state = 0 
        self.draw_image_index = 0
        self.previous_time = current_time
        # if click_state == 1 then means it's not clicked
        # if it's clicked then it will be unclicked
    def isClickable(money):
        if self.cost >= money:
            return False 
        if self.current_time is None:
            return True  
        if self.current_time - self.previous_time > self.freeze_time:
            return True
        return False

    def ProcessEvent(self, x,y,clickLeft,clickRight, money, current_time, is_valid_region): # / return whether it's clicked
        if clickLeft is None and clickRight is None:
            return False
        if grid.IsInRegion(x,y): #// 现在在点击我，我得看看
            if  self.click_state == 0: #以前没点的话就要看看能否点，有钱并且时间已经超过冷冻时间。
                if(self.isClickable(money)): 
                    self.click_state == 1
                    self.draw_image_index =1
                else:
            else:
                self.click_state == 0 # // 
                self.draw_image_index = 0
            # now should be able to process time
            self.current_time = current_time
        else:
            if is_valid_region:
                if self.click_state == 1:  #按下鼠标这个时候要布置植物，这个时候需要判断是不是
                    self.click_state = 0
                    self.draw_image_index = 0
                    self.previous_time = current_time
                    self.current_time = current_time
                    return True
            else:
                self.current_time = current_time
        return False
                
    def get_draw_image():
        return self.image_list[self.draw_image_index]
            


class Play:
    def __init__(self, cardname_list, card_images, card_play_images, money, current_time):

    def init_game(self, dictstate):

        self.card_list = ["card_sunflower",
        'card_peashooter',
        'card_snowpea',
        'card_wallnut',
        'card_cherrybomb',
        'card_threepeashooter',
        'card_squash',
        'card_jalapeno',

        ]
        if 'select_cards' in dictstate:
            self.card_list = dictstate['select_cards']
        self.money = 100
        if "money" in dictstate:
            self.money = dictstate['money']
        self.done = False
        self.current_time =dictstate['current_time']
        self.card_list= []
        self.card_to_sprite_image={}

        card_x_length = 53
        card_y_length = 74

        grid_x = 9
        grid_y =5 


        #self.UpperCard_TotalOffSet_X = C.Constant_PlantSelection_LayOut.Upper_Panel_Card_Offset_X + C.Constant_PlantSelection_LayOut.Upper_Panel_Offset_X
        self.UpperCard_TotalOffSet_X = 78
        #self.UpperCard_TotalOffSet_Y=C.Constant_PlantSelection_LayOut.Upper_Panel_Offset_Y+ C.Constant_PlantSelection_LayOut.Upper_Panel_Card_Offset_y
        self.UpperCard_TotalOffSet_Y = 8

        #下面的是用来选牌用的
        sef.card_grid = Tool.Grid(1, 8, self.UpperCard_TotalOffSet_X, self.UpperCard_TotalOffSet_Y, card_x_length, card_y_length)
        # 
        self.map_grid = Tool.Grid(grid_y, grid_x , 30, 80,  100)
        self.plant_position_map = [[True *grid_x] for i in range(grid_y)]
        for i, card_name in enumerate(self.card_list):
            single_card_image = Tool.All_Images[card_name]
            card_spirte_info = Tool.get_plant_info_from_card_name(card_name)
            plant_name, plant_freezetime, plant_cost = card_spirte_info
            plant_sprite_images = Tool.All_Images[plant_name]

            single_card = Card(self.card_grid,i,card_name,single_card_image, plant_cost, plant_freezetime)
            self.card_list.append(single_card)
            
    def ProcessEvent(self, x,y,clickLeft,clickRight):
