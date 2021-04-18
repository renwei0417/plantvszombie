import random
import pygame as pg
import os
import constant as C 
import Tool
import PlanSelect
import game_play
import plants 
from metainfo import * 




background_image_index=0
background_image_name='Background'
BackGroundImage=Tool.All_Images[background_image_name][background_image_index]
viewpoint=Tool.Screen.get_rect()
viewpoint.x+=C.Constant_MapComponent.BACKGROUND_OFFSET_X
Tool.Screen.blit(BackGroundImage,(0,0),viewpoint )
grid_x = 9
grid_y =5 
map_grid = Tool.Grid(grid_y, grid_x , 30, 80, 80, 100)
zombie_image = Tool.Zombie_Images
zombie_list = []
plant_list =[]
bullet_list = []

for i in range(0,5,2):

    # panelSelector=PlanSelect.PanelSelector()
    # panelSelector.Draw(Tool.Screen)
    zombie_x, zombie_y = map_grid.GetCorxCorY(8+ i*grid_x)
    zombie_initial_state =  GetZombieInitialState(ZombieName.Zombie)
    zombie_initial_state[ZombieInitialStateKeyEnum.rect] = pg.rect.Rect(zombie_x ,zombie_y - 50,80, 100)
    a_zombie= plants.Zombie(zombie_initial_state)
    zombie_list.append(a_zombie)
for i in range(0,5,2):

    # panelSelector=PlanSelect.PanelSelector()
    # panelSelector.Draw(Tool.Screen)
    plant_x, plant_y = map_grid.GetCorxCorY(1+ i*grid_x)
    if i == 4:
        plant_initial_state =  GetPlantInitialState(PlantNameEnum.Peashooter)
        plant_initial_state['rect'] = pg.rect.Rect(plant_x,plant_y,80, 100)
        pea_shooter= plants.Peashooter(plant_initial_state)
        plant_list.append(pea_shooter)
    else:
        plant_initial_state =  GetPlantInitialState(PlantNameEnum.SnowPea)
        plant_initial_state['rect'] = pg.rect.Rect(plant_x,plant_y,80, 100)
        pea_shooter= plants.Peashooter(plant_initial_state)
        plant_list.append(pea_shooter)






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

# level_play = game_play.Play()
# level_play.init_game(game_state)

# games_level = [PlanSelect(), Play()]

time_delay = 100 # 0.1 second
timer_event = pg.USEREVENT + 1

pg.time.set_timer(timer_event, time_delay)

initialize_time = current_time



while not done:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            done=True
            break
        elif event.type==pg.KEYDOWN:#
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
    #print(current_time)

    #level_play.ProcessEvent(x, y, left_click, right_click, current_time)
    Tool.Screen.fill((0,0,0))
    Tool.Screen.blit(BackGroundImage,(0,0),viewpoint )
    #首先植物攻击
    for plant in plant_list:
        plant.update_time(current_time)
        bullets = plant.attack(zombie_list)
        if bullets is not None:
            bullet_list.extend(bullets)


    #其次子弹来攻击：
    for bullet in bullet_list:
        bullet.update_time(current_time)
        bullet.attack(zombie_list)

    #现在来僵尸攻击
    for zombie in zombie_list: 
        zombie.update_time(current_time)
        zombie.attack(plant_list)
    
    #现在来刷新了
    for plant in plant_list:
        plant.update()
    
    for bullet in bullet_list:
        bullet.update()
    for zombie in zombie_list:
        zombie.update()

    #现在把死掉的干掉

    plant_list_alive = []
    for plant in plant_list:
        if plant.get_state() != PlantState.Dead:
            plant_list_alive.append(plant)
            plant.draw(Tool.Screen)
    plant_list = plant_list_alive

    bullet_list_alive = []
    for bullet  in bullet_list:
        if bullet.get_state() != BulletState.Dead:
            bullet_list_alive.append(bullet)
            bullet.draw(Tool.Screen)
    bullet_list = bullet_list_alive

    zombie_list_alive = []
    for zombie  in zombie_list:
        if zombie.get_state() != ZombieState.Dead:
            zombie_list_alive.append(zombie)
            zombie.draw(Tool.Screen)
    zombie_list = zombie_list_alive

    
        

    pg.display.update()
    mouse_pos=[None,None]
    mouse_click=[None,None]

    #print(len(bullet_list))






    
