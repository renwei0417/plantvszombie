import pygame as pg
import os 
import constant as C

def get_plant_info_from_card_name(cardname):
    plant_name = cardname.split('_')[1]

    for i, name in enumerate(C.Constant_PlantInfo.plant_name_list):
        if(name.lower()== plant_name.lower()):
            return C.Constant_PlantInfo.plant_name_list[i], C.Constant_PlantInfo.plant_frozen_time_list[i], C.Constant_PlantInfo.plant_sun_list[i]
    return None 
def load_image_frames(directory,image_name, colorkey, accept):
    frame_list=[]
    number_of_image=0
    tmp={}
    start_position=len(image_name)+1

    for pic in os.listdir(directory):
        name,ext=os.path.splitext(pic)
        if ext.lower() in accept:
            index=int(name[start_position:])
            img=pg.image.load(os.path.join(directory,pic))
            if img.get_alpha():
                img=img.convert_alpha()
            else:
                img=img.convert()
                img.set_colorkey(colorkey)
            tmp[index]=img
            number_of_image+=1
    for i in range(number_of_image):
        frame_list.append(tmp[i])
    return frame_list

def load_all_gfx(directory, colorkey=C.Constant_Color.WHITE, accept=('.png', '.jpg', '.bmp', '.gif')):
    graphics = {}
    for name1 in os.listdir(directory):
        # subfolders under the folder resources\graphics
        dir1 = os.path.join(directory, name1)
        if os.path.isdir(dir1):
            for name2 in os.listdir(dir1):
                dir2 = os.path.join(dir1, name2)
                if os.path.isdir(dir2):
                # e.g. subfolders under the folder resources\graphics\Zombies
                    for name3 in os.listdir(dir2):
                        dir3 = os.path.join(dir2, name3)
                        # e.g. subfolders or pics under the folder resources\graphics\Zombies\ConeheadZombie
                        if os.path.isdir(dir3):
                            # e.g. it's the folder resources\graphics\Zombies\ConeheadZombie\ConeheadZombieAttack
                            image_name, _ = os.path.splitext(name3)
                            graphics[image_name] = load_image_frames(dir3, image_name, colorkey, accept)
                        else:
                            # e.g. pics under the folder resources\graphics\Plants\Peashooter
                            image_name, _ = os.path.splitext(name2)
                            graphics[image_name] = load_image_frames(dir2, image_name, colorkey, accept)
                            break
                else:
                # e.g. pics under the folder resources\graphics\Screen
                    name, ext = os.path.splitext(name2)
                    if ext.lower() in accept:
                        img = pg.image.load(dir2)
                        if img.get_alpha():
                            img = img.convert_alpha()
                        else:
                            img = img.convert()
                            img.set_colorkey(colorkey)
                        graphics[name] = img
    return graphics


def get_surface_from_image(image, x, y, width, height, colorkey=C.Constant_Color.BLACK, scale=1):
    subScreen=pg.Surface([width,height])
    rect=subScreen.get_rect()
    #subScreen.blit(image, 
    subScreen.blit(image, (0, 0), (x, y, width, height))
    subScreen.set_colorkey(colorkey)
    subScreen = pg.transform.scale(subScreen,
                                   (int(rect.width*scale),
                                    int(rect.height*scale)))
    return subScreen

def get_surface_from_image_samesize(image,  colorkey=C.Constant_Color.BLACK, scale=1):
    orignal_rect=image.get_rect()
    return get_surface_from_image(image,0,0,orignal_rect.width,orignal_rect.height,colorkey,scale)

class Grid():
    def __init__(self,row, column, leftx, lefty, xinterval, yinterval):
        self.row=row
        self.column=column
        self.leftx=leftx
        self.lefty=lefty
        self.xinterval=xinterval
        self.yinterval=yinterval
        self.width=xinterval*column
        self.height=yinterval*row
    def IsInRegion(self, x,y):
        if x is None or y is None:
            return False 
        x_distance=x-self.leftx
        y_distance=y-self.lefty
        if x_distance >=0 and y_distance>=0 and x_distance<= self.width and y_distance<=self.height:
            return True
        return False
    def GetIndexFromXY(self,x,y):
        x_distance=x-self.leftx
        y_distance=y-self.lefty
        columnIndex=x_distance// self.xinterval
        rowIndex= y_distance//self.yinterval
        Index=rowIndex*self.column + columnIndex

        return (rowIndex,columnIndex,Index)
    def GetCorxCorY(self,Index):
        rowIndex=Index//self.column
        columnIndex=Index% self.column

        x=self.leftx + columnIndex* self.xinterval
        y=self.lefty + rowIndex*self.yinterval
        return (x,y)
    def DrawImages(self, Screen, Images):
        if len(Images)==0:
            return 
        for i, image in enumerate(Images):
            x, y= self.GetCorxCorY(i)
            image_rec=image.get_rect()
            Screen.blit(image,(x,y),(0,0,image_rec.width, image_rec.height))
resourceDirectory=r'D:\Code\PlantsVsZombies\resources\graphics'
pg.init()




def get_level_2_images(path,colorkey=C.Constant_Color.WHITE, accept=('.png', '.jpg', '.bmp', '.gif'),colorkey=C.Constant_Color.WHITE, accept=('.png', '.jpg', '.bmp', '.gif'))
    image_dict = {}
    for path_level in os.listdir(path):
        #这里的level是 NormalZombie,  ConeheadZombie, FlagZombie, NewsPaperZombie, NormalZombie
        for path_level_1 in os.listdir(path_level):
            images = load_image_frames(os.path.join(path,path_level, path_level_1,),path_level_1)
            image_dict[path_level_1] = images 



Screen=pg.display.set_mode((C.Constant_Screen.SCREEN_WIDTH,C.Constant_Screen.SCREEN_HEIGHT))
pg.display.set_caption("plants vs zombi")


resourceDirectory=r'D:\Code\PlantsVsZombies\resources\graphics'
All_Images=load_all_gfx(resourceDirectory)







    





    



    






