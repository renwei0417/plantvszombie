import random
import pygame as pg
import os
import constant as C 
import Tool
import PlanSelect


background_image_index=0
background_image_name='Background'
BackGroundImage=Tool.All_Images[background_image_name][background_image_index]
viewpoint=Tool.Screen.get_rect();
viewpoint.x+=C.Constant_MapComponent.BACKGROUND_OFFSET_X
Tool.Screen.blit(BackGroundImage,(0,0),viewpoint )

panelSelector=PlanSelect.PanelSelector()
panelSelector.Draw(Tool.Screen)


pg.display.flip()
pg.display.update()
TimeEvent = pg.USEREVENT+1

done = False

mouse_pos=[None,None]
mouse_click= [False,False] 
keys_press=None
keys_up= None 


game_state= {}

games_level = [PlanSelect(), Play()]



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
        if not panelSelector.Done:
            panelSelector.ProcessEvent(x,y,left_click,right_click)
            panelSelector.Draw(Tool.Screen)
            if panelSelector.Done:
                print('need to handle the changes')
           
        pg.display.update()
        mouse_pos=[None,None]
        mouse_click=[None,None]


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






    
