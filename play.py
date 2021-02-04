import pygame as pg
import os 
import constant as C
import Tool


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
#//return value , 前面表示是否按下，后边表示是否落下

    #现在点的是你
    def handle_clicked(self, current_time, money):
        self.current_time= current_time
        if  self.click_state == 0: #以前没点的话就要看看能否点，有钱并且时间已经超过冷冻时间。
            if(self.isClickable(money)): 
                self.click_state == 1
                self.draw_image_index =1
                return True
        if self.click_state == 1:
            self.click_state = 0
            self.draw_image_index = 0
            return False
        return False 
    # 之前点了你，但是现在不点你了
    def handle_unclicked(self, current_time):
        self.current_time= current_time
        if self.click_state == 1:
            self.click_state == 0
            self.draw_image_index =0  

    def hanlde_user_plant(self, current_time):
            if self.click_state == 1:  #按下鼠标这个时候要布置植物，这个时候需要判断是不是
                self.click_state = 0
                self.draw_image_index = 0
                self.previous_time = current_time
                self.current_time = current_time
    def handle_idle(self, current_time):
        this.current_time = current_time


    


    # def ProcessEvent(self, x,y,clickLeft,clickRight, money, current_time, is_valid_region): # / return whether it's clicked
    #     if clickLeft is None and clickRight is None:
    #         return False, False 
    #     if grid.IsInRegion(x,y): #// 现在在点击我，我得看看
    #         if  self.click_state == 0: #以前没点的话就要看看能否点，有钱并且时间已经超过冷冻时间。
    #             if(self.isClickable(money)): 
    #                 self.click_state == 1
    #                 self.draw_image_index =1
    #                 return True, False
    #         else:
    #             self.click_state == 0 # // 
    #             self.draw_image_index = 0
    #         # now should be able to process time
    #         self.current_time = current_time
    #     else:
    #         if is_valid_region:
    #             if self.click_state == 1:  #按下鼠标这个时候要布置植物，这个时候需要判断是不是
    #                 self.click_state = 0
    #                 self.draw_image_index = 0
    #                 self.previous_time = current_time
    #                 self.current_time = current_time
    #                 return False, True 
    #         else:
    #             self.current_time = current_time
    #     return False, False 
                
    def draw(self, screen)
        image_to_draw = self.image_list[self.draw_image_index]
        screen.blit(image_to_draw, (self.x, self.y), (0, 0, self.width, self.height))


#现在来说，只是为了能够显示出来
class Plant:
    def __init__(self, name, images, x, y, width, height, current_time):
        self.name=name
        self.images = images 
        self.x =x 
        self.y =y 
        self.width = width
        self.height =self.height
        self.current_time = current_time
        self.image_index =0 
        self.refresh_time_interval = 10
    def update(self, time):
        if time - self.current_time > = self.refresh_time_interval:
            self.image_index = (self.image_index +1) % len(self.images)
            self.current_time =time 
    def draw(self, Screen)
        Screen.blit(self.images[self.image_index], (self.x, self.y), (0, 0, self.width, self.height))


class Play:
    def __init__(self, cardname_list, card_images, card_play_images, money, current_time):
        self.card_list = ["card_sunflower",
        'card_peashooter',
        'card_snowpea',
        'card_wallnut',
        'card_cherrybomb',
        'card_threepeashooter',
        'card_squash',
        'card_jalapeno',

        ]
        self.money = 100
        self.done = False
        self.current_time = None 
        self.card_list= []
        self.card_to_sprite_image={}
        self.plant_list=[]
        self.click_state = 0  # 0 for nothing, 1 for user have clicked a plant and its Ok, 2 for user clicked somewhere else.
        self.click_card_name = None 

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
        self.map_grid = Tool.Grid(grid_y, grid_x , 30, 80,  100)
        self.plant_position_map = [[True *grid_x] for i in range(grid_y)]
        for i, card_name in enumerate(self.card_list):
            single_card_image = Tool.All_Images[card_name]
            single_card_image = Tool.get_surface_from_image_samesize(single_card_image)
            card_spirte_info = Tool.get_plant_info_from_card_name(card_name)
            plant_name, plant_freezetime, plant_cost = card_spirte_info
            plant_sprite_images = Tool.All_Images[plant_name]

            single_card = Card(self.card_grid,i,card_name,single_card_image, plant_cost, plant_freezetime)
            self.card_list.append(single_card)
            sefl.card_to_sprite_image[card_name] = plant_sprite_images
            
    def ProcessEvent(self, x,y,clickLeft,clickRight, time):

        #如果啥都没有，那么这么搞吧
        if clickLeft is False and clickRight is False:
            for card in self.card_list:
                card.handle_idle(time)

        isClickInPlants = self.card_grid.IsInRegion(x,y)
        isClickInMap = self.map_grid.IsInRegion(x,y)
        
        if isClickInPlants:
            click_rowIndex, click_columnIndex, total_index = self.card_grid.GetIndexFromXY(x,y)
            if total_index < len(self.card_list): # now click in
                if self.click_state == 0:
                    for i in range(len(self.card_list)):
                        if i == total_index:
                            is_valid_click = card_list[i].handle_clicked(time, self.money)
                            if IsClickedValid:
                                self.click_state = 1
                                self.click_card_name = card_list[i].name
                        else:
                            card_list[i].handle_idle(time)

              

                #如果以前就点了，那就是取消或者换一个。
                if self.click_state == 1:
                    if self.card_list[total_index].name == self.click_card_name：
                     #点击的还是之前的那一个，那么简单重置即可
                        self.click_state[total_index].handle_unclicked(time)
                        self.click_state =0
                        self.click_card_name = None 
                        for i in range(len(self.card_list)):
                            if i != total_index:
                                self.card_list[i].handle_idle(time)
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
                                self.card_list[i].handle_unclicked(time)
                            else:
                                self.card_list[i].handle_idle(time)
        
        if isClickInMap:
            row_index, column_index, total_index = self.map_grid.GetIndexFromXY(x,y)
            if self.plant_position_map[row_index][column_index] and self.click_state ==1:
                #这时候就可以种植植物了
                plant_images = self.card_to_sprite_image[self.click_card_name]
                x, y = self.map_grid.GetCorxCorY(total_index)
                newplant= Plant(images,x,y, self.map_grid.xinterval, self.map_grid.yinterval, current_time)
                self.plant_list.append(newplant)

                self.click_state = 0
                self.click_card_name = None 
        
        if not isClickInPlants and not isClickInPlants:
            for card in self.card_list:
                card.handle_idle()
        
    def Draw(self, screen):

        # now started to draw
        if self.click_state == 1:
            pg.mouse.set_visible(False)
            #还需要画出来，并且中心实际上应该是鼠标的位置，所以大小上就弄个跟他一样的。
            mouse_image = self.card_to_sprite_image[self.click_card_name][0]
            mouse_image.set_alpha(128)
            mouse_image = Tool.get_surface_from_image_samesize(mouse_image)
            mouse_rect = mouse_image.get_rect()
            mouse_rect.centerx = x 
            mouse_rect.centery = y

            screen.blit(mouse_image, mouse_rect, (0, 0, mouse_rect.width, mouse_rect.height))
        if self.click_state == 0:
            pg.mouse.set_visible(True)
            # no blit is fine
        
        for card in self.card_list:
            card.draw(screen)
        
        for sprite in self.plant_list:
            sprite.draw(screen)



            

        
