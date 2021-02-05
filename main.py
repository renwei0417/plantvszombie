import random
import pygame as pg
import os
import constant as C 
import Tool
import PlanSelect


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
        # if click_state == 1 then means it's not clicked
        # if it's clicked then it will be unclicked
    def isClickable(self, money):
        if self.cost >= money:
            return False 
        if self.current_time is None:
            return True  
        if self.current_time - self.previous_time > 0.1 * self.freeze_time:
            return True
        return False

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
        self.current_time = current_time
             
    def draw(self, screen):
        image_to_draw = self.image_list[self.draw_image_index]
        screen.blit(image_to_draw, (self.x, self.y), (0, 0, self.width, self.height))


#现在来说，只是为了能够显示出来
class Plant:
    def __init__(self, name, images, x, y, width, height, current_time):
        self.name=name
        self.images = []
        for single_image in images:
            image_copy = Tool.get_surface_from_image_samesize(single_image)
            self.images.append(image_copy)
        self.x =x 
        self.y =y 
        self.width = width
        self.height =height 
        self.current_time = current_time
        self.image_index =0 
        self.refresh_time_interval = 100
    def update(self, time):
        if time - self.current_time >= self.refresh_time_interval:
            self.image_index = (self.image_index +1) % len(self.images)
            self.current_time =time 
    def draw(self, Screen):
        Screen.blit(self.images[self.image_index], (self.x, self.y), (0, 0, self.width, self.height))


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

        isClickInPlants = False 
        isClickInMap = False 
        if clickLeft is False and clickRight is False:
            for card in self.card_list:
                card.handle_idle(time)
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
                            self.card_list[i].handle_idle(time)

              

                #如果以前就点了，那就是取消或者换一个。
                elif self.click_state == 1:
                    if self.card_list[total_index].name == self.click_card_name:
                     #点击的还是之前的那一个，那么简单重置即可
                        self.card_list[total_index].handle_unclicked(time)
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
                newplant= Plant(self.click_card_name, plant_images,x,y, self.map_grid.xinterval, self.map_grid.yinterval, current_time)
                self.plant_list.append(newplant)
                self.plant_position_map[row_index][column_index] = False

                self.click_state = 0
                self.click_card_name = None 
        
        if not isClickInPlants and not isClickInPlants:
            for card in self.card_list:
                card.handle_idle(time)
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



background_image_index=0
background_image_name='Background'
BackGroundImage=Tool.All_Images[background_image_name][background_image_index]
viewpoint=Tool.Screen.get_rect();
viewpoint.x+=C.Constant_MapComponent.BACKGROUND_OFFSET_X
Tool.Screen.blit(BackGroundImage,(0,0),viewpoint )

# panelSelector=PlanSelect.PanelSelector()
# panelSelector.Draw(Tool.Screen)




pg.display.flip()
pg.display.update()
TimeEvent = pg.USEREVENT+1

done = False

mouse_pos=[None,None]
mouse_click= [False,False] 
keys_press=None
keys_up= None 


game_state= {}
current_time = pg.time.get_ticks()
game_state['current_time'] = current_time

level_play = Play()
level_play.init_game(game_state)

# games_level = [PlanSelect(), Play()]

time_delay = 100 # 0.1 second
timer_event = pg.USEREVENT + 1


while not done:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            done=True
        elif event.type==pg.KEYDOWN:
            keys_press=pg.key.get_pressed()
            if event.key==pg.K_UP:
                print("you pressed UP key")
        elif event.type==pg.KEYUP:
            keys_up=pg.key.get_pressed()
            print("you pressed down up")
        elif event.type==pg.MOUSEBUTTONDOWN:
            mouse_pos=pg.mouse.get_pos()
            print("mouse position {}".format(mouse_pos))
            mouse_click[0], _, mouse_click[1] = pg.mouse.get_pressed() 
            print("mouse click {0}".format(mouse_click))
        
        x,y=mouse_pos
        left_click,right_click=mouse_click
        current_time = pg.time.get_ticks()

        level_play.ProcessEvent(x, y, left_click, right_click, current_time)
        Tool.Screen.fill((0,0,0))
        Tool.Screen.blit(BackGroundImage,(0,0),viewpoint )
        level_play.Draw(Tool.Screen)
        # if not panelSelector.Done:
        #     panelSelector.ProcessEvent(x,y,left_click,right_click)
        #     panelSelector.Draw(Tool.Screen)
        #     if panelSelector.Done:
        #         print('need to handle the changes')
           
        pg.display.update()
        mouse_pos=[None,None]
        mouse_click=[None,None]

a=input()
# print("done")

# class Grid():
#     def __init__(self,row, column, leftx, lefty, xinterval, yinterval):
#         self.row=row
#         self.column=column
#         self.leftx=leftx
#         self.lefty=lefty
#         self.xinterval=xinterval
#         self.yinterval=yinterval
#         self.width=xinterval*column
#         self.height=yinterval*row
#     def IsInRegion(self, x,y):
#         x_distance=x-self.leftx
#         y_distance=y-self.lefty
#         if x_distance >=0 and y_distance>=0 and x_distance<= self.width and y_distance<=self.height:
#             return True
#         return False
#     def GetIndexFromXY(self,x,y):
#         x_distance=x-self.leftx
#         y_distance=y-self.lefty
#         columnIndex=x_distance// self.xinterval
#         rowIndex= y_distance//self.yinterval
#         Index=rowIndex*self.column + columnIndex

#         return (rowIndex,columnIndex,Index)
#     def GetCorxCorY(self,Index):
#         rowIndex=Index//self.column
#         columnIndex=Index% self.column

#         x=self.leftx + columnIndex* self.yinterval
#         y=self.lefty + rowIndex*self.yinterval
#         return (x,y)

myGrid=Grid(2,3,5,4,40,40)

print(myGrid.IsInRegion(50,50))

print(myGrid.GetIndexFromXY(50,50))
print(myGrid.GetCorxCorY(5))


print('good')





print('good')






    
