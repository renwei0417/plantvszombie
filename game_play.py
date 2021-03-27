import pygame as pg
import os 
import constant as C
import Tool
import plants

class Card:
    def __init__(self, grid, index, name, image, cost, freeze_time, current_time):
        self.grid=grid
        self.index=index
        self.name=name
        
        x, y = self.grid.GetCorxCorY(index)
        self.x= x
        self.y= y
        self.width = self.grid.xinterval
        self.height = self.grid.yinterval
        self.cost= cost 

        dark_image= image.copy()
        # dard image is used when clickable
        dark_image.set_alpha(128)
        
        self.image_list= [image.copy(), dark_image]
        self.freeze_time = freeze_time
        self.current_time = None
        self.click_state = 0 
        self.draw_image_index = 0
        self.previous_time = current_time
        self.is_freezed = False 
        self.is_ready_for_click = False 
        # if click_state == 1 then means it's not clicked
        # if it's clicked then it will be unclicke
    def isClickable(self, money):
        if self.cost >= money:
            return False 
        if self.current_time is None:
            return True

        if self.is_freezed:
            return False   
        return True
    def handle_freeze(self):
        if self.previous_time is not None and self.current_time is not None:
            if self.current_time - self.previous_time >= self.freeze_time :
                self.is_freezed = False 
            else:
                self.is_freezed = True 

    #现在点的是你
    def handle_clicked(self, current_time, money):
        self.current_time= current_time
        self.handle_freeze()
        self.is_ready_for_click = self.isClickable( money)
        if  self.click_state == 0: #以前没点的话就要看看能否点，有钱并且时间已经超过冷冻时间。
            if self.is_ready_for_click: 
                self.click_state = 1
                return True
        else :
            self.click_state = 0
            return False
        return False 
    # 之前点了你，但是现在不点你了，但是点了植物中的其他植物
    def handle_unclicked(self, current_time, money):
        self.current_time= current_time
        self.handle_freeze()
        self.is_ready_for_click = self.isClickable(money)
        if self.click_state == 1:
            self.click_state = 0

    def hanlde_user_plant(self, current_time, money):
            self.current_time= current_time
            if self.click_state == 1:  #按下鼠标这个时候要布置植物，这个时候需要判断是不是
                self.click_state = 0
                self.draw_image_index = 0
                self.previous_time = self.current_time
                self.is_freezed = True 
    def handle_idle(self, current_time, money):
        self.current_time = current_time
        self.handle_freeze()
        self.is_ready_for_click = self.isClickable( money)
        

             
    def draw(self, screen):
        image_index = 0
        if self.click_state == 1:
            image_index = 1
        else:
            if not self.is_ready_for_click:
                image_index = 1
        image_to_draw = self.image_list[image_index]
        screen.blit(image_to_draw, (self.x, self.y), (0, 0, self.width, self.height))


#现在来说，只是为了能够显示出来



class Play:
    def __init__(self):
        self.cardname_list = []
        self.money = 100
        self.done = False
        self.current_time = None 
        self.card_list= []
        self.card_to_sprite_image={}
        self.plant_list=[]
        self.click_state = 0  # 0 for nothing, 1 for user have clicked a plant and its Ok, 2 for user clicked somewhere else.
        self.click_card_name = None 

    def init_game(self, dictstate):

        self.cardname_list = ["card_sunflower",
        'card_peashooter',
        'card_snowpea',
        'card_wallnut',
        'card_cherrybomb',
        'card_threepeater',
        'card_squash',
        'card_jalapeno',

        ]
        if 'select_cards' in dictstate:
            self.card_list = dictstate['select_cards']
        self.money = 30000
        if "money" in dictstate:
            self.money = dictstate['money']
        self.done = False
        self.current_time =dictstate['current_time']


        card_x_length = 53
        card_y_length = 74

        grid_x = 9
        grid_y =5 


        #self.UpperCard_TotalOffSet_X = C.Constant_PlantSelection_LayOut.Upper_Panel_Card_Offset_X + C.Constant_PlantSelection_LayOut.Upper_Panel_Offset_X
        self.UpperCard_TotalOffSet_X = 78
        #self.UpperCard_TotalOffSet_Y=C.Constant_PlantSelection_LayOut.Upper_Panel_Offset_Y+ C.Constant_PlantSelection_LayOut.Upper_Panel_Card_Offset_y
        self.UpperCard_TotalOffSet_Y = 8

        #下面的是用来选牌用的
        self.card_grid = Tool.Grid(1, 8, self.UpperCard_TotalOffSet_X, self.UpperCard_TotalOffSet_Y, card_x_length, card_y_length)
        # 
        self.map_grid = Tool.Grid(grid_y, grid_x , 30, 80, 80, 100)
        self.plant_position_map = [[True for j in range(grid_x)] for i in range(grid_y)]
        for i, card_name in enumerate(self.cardname_list):
            single_card_image = Tool.All_Images[card_name]
            single_card_image = Tool.get_surface_from_image_samesize(single_card_image)
            card_spirte_info = Tool.get_plant_info_from_card_name(card_name)
            plant_name, plant_freezetime, plant_cost = card_spirte_info
            plant_sprite_images = Tool.All_Images[plant_name]

            single_card = Card(self.card_grid,i,card_name,single_card_image, plant_cost, plant_freezetime, self.current_time)
            self.card_list.append(single_card)
            self.card_to_sprite_image[card_name] = plant_sprite_images
            
    def ProcessEvent(self, x,y,clickLeft,clickRight, time):

        #如果啥都没有，那么这么搞吧
        self.current_time = time 
        isClickInPlants = False 
        isClickInMap = False 
        if not clickLeft  and not clickRight :
            for card in self.card_list:
                card.handle_idle(time,self.money)
        else:
            isClickInMap = self.map_grid.IsInRegion(x,y)
            isClickInPlants =self.card_grid.IsInRegion(x, y)

        
        if isClickInPlants:
            click_rowIndex, click_columnIndex, total_index = self.card_grid.GetIndexFromXY(x,y)
            if total_index < len(self.card_list): # now click in
                if self.click_state == 0:
                    for i in range(len(self.card_list)):
                        if i == total_index:
                            is_valid_click = self.card_list[i].handle_clicked(time, self.money)
                            if is_valid_click:
                                self.click_state = 1
                                self.click_card_name = self.card_list[i].name
                        else:
                            self.card_list[i].handle_idle(time, self.money)

              

                #如果以前就点了，那就是取消或者换一个。
                elif self.click_state == 1:
                    if self.card_list[total_index].name == self.click_card_name:
                     #点击的还是之前的那一个，那么简单重置即可
                        self.card_list[total_index].handle_clicked(time, self.money)
                        self.click_state =0
                        self.click_card_name = None 
                        for i in range(len(self.card_list)):
                            if i != total_index:
                                self.card_list[i].handle_unclicked(time, self.money)
                    else:
                        #现在是点击了另外一个，那么之前点的置零，以后点的要看一下了 
                        previous_click_name = self.click_card_name
                        for i in range(len(self.card_list)):
                            if i == total_index:
                                is_valid_click = self.card_list[i].handle_clicked(time, self.money)
                                if is_valid_click:
                                    self.click_card_name= self.card_list[i].name
                                else:
                                    self.click_state =0
                                    self.click_card_name = None
                            elif self.card_list[i].name == previous_click_name:
                                self.card_list[i].handle_unclicked(time, self.money)
                            else:
                                self.card_list[i].handle_idle(time, self.money)
        # else:
        #     for card in self.card_list:
        #         card.handle_idle(time, self.money)
        
        if isClickInMap:
            row_index, column_index, total_index = self.map_grid.GetIndexFromXY(x,y)
            if self.plant_position_map[row_index][column_index] and self.click_state ==1:
                #这时候就可以种植植物了

                for card in self.card_list:
                    if card.name == self.click_card_name:
                        card.hanlde_user_plant(time, self.money)

                plant_images = self.card_to_sprite_image[self.click_card_name]
                x, y = self.map_grid.GetCorxCorY(total_index)
                newplant= plants.Plant(self.click_card_name, plant_images,x,y, self.map_grid.xinterval, self.map_grid.yinterval, self.current_time)
                self.plant_list.append(newplant)
                self.plant_position_map[row_index][column_index] = False

                self.click_state = 0
                self.click_card_name = None 
        
        if not isClickInPlants and not isClickInPlants:
            for card in self.card_list:
                card.handle_idle(time,self.money)
        for plant in self.plant_list:
            plant.update(time)
        
    def Draw(self, screen):

        # now started to draw
        if self.click_state == 1:
            # pg.mouse.set_visible(False)
            # #还需要画出来，并且中心实际上应该是鼠标的位置，所以大小上就弄个跟他一样的。
            # mouse_image = self.card_to_sprite_image[self.click_card_name][0]
            # mouse_image.set_alpha(128)
            # mouse_image = Tool.get_surface_from_image_samesize(mouse_image)
            # mouse_rect = mouse_image.get_rect()
            # mouse_rect.centerx = x 
            # mouse_rect.centery = y

            #screen.blit(mouse_image, mouse_rect, (0, 0, mouse_rect.width, mouse_rect.height))
            print(' ')
        if self.click_state == 0:
            # pg.mouse.set_visible(True)
            # no blit is fine
            print(' ')
        
        for card in self.card_list:
            card.draw(screen)
        
        for sprite in self.plant_list:
            sprite.draw(screen)





            

        
