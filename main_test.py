import random
import pygame as pg
import os
import constant as C 
import Tool
import PlanSelect
import game_play




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

# level_play = game_play.Play()
# level_play.init_game(game_state)

# games_level = [PlanSelect(), Play()]

time_delay = 100 # 0.1 second
timer_event = pg.USEREVENT + 1

pg.time.set_timer(timer_event, 10)

map_grid = Tool.Grid(grid_y, grid_x , 30, 80, 80, 100)

zombie_images = Tool


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

        #level_play.ProcessEvent(x, y, left_click, right_click, current_time)
        Tool.Screen.fill((0,0,0))
        Tool.Screen.blit(BackGroundImage,(0,0),viewpoint )
        #level_play.Draw(Tool.Screen)
        pg.display.update()
        mouse_pos=[None,None]
        mouse_click=[None,None]






    
