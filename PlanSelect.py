import pygame as pg
import os 
import constant as C
import Tool

class PanelSelector():
    def __init__(self):
        self.CardImage_dictionary={}
        self.BottomCards=[]
        self.BottomCards_Type=[]
        self.UpperCards=[]
        self.UpperCards_Type=[]

        #set card offset
        self.LowerCard_TotalOffSet_X=C.Constant_PlantSelection_LayOut.Lower_Panel_Offset_X + C.Constant_PlantSelection_LayOut.Lower_Panel_Card_Offset_x
        self.LowerCard_TotalOffSet_Y= C.Constant_PlantSelection_LayOut.Lower_Panel_Offset_Y+C.Constant_PlantSelection_LayOut.Lower_Panel_Card_Offset_Y

        self.UpperCard_TotalOffSet_X = C.Constant_PlantSelection_LayOut.Upper_Panel_Card_Offset_X + C.Constant_PlantSelection_LayOut.Upper_Panel_Offset_X;
        self.UpperCard_TotalOffSet_Y=C.Constant_PlantSelection_LayOut.Upper_Panel_Offset_Y+ C.Constant_PlantSelection_LayOut.Upper_Panel_Card_Offset_y
        self.TotalCardNumber=len(C.Constant_PlantInfo.all_card_list)
        self.TotalSelectCardMax=8
        self.IsAllSelected=False
        self.Done=False


        for i  in C.Constant_PlantInfo.all_card_list:
            card=C.Constant_Card.card_name_list[i]
            CardImage_Raw=Tool.All_Images[card]
            alpha=i*32%256
            #allPlants.append(card)
            #CardImage_Raw.set_alpha(alpha)
            CardImage_big=Tool.get_surface_from_image_samesize(CardImage_Raw,C.Constant_Color.WHITE,0.8)
            CardImage=Tool.get_surface_from_image_samesize(CardImage_Raw,C.Constant_Color.WHITE,0.75)
            CardImage_dark=CardImage.copy()
            CardImage_dark.set_alpha(128)
            self.CardImage_dictionary[card]=[CardImage,CardImage_dark,CardImage_big]
            self.BottomCards.append(card)
            self.BottomCards_Type.append(0)
        #for item in self.CardImage_dictionary.keys:

        
        #set up pannel images
                
        UpperPanelImage_Raw=Tool.All_Images[C.Constant_MenuBar.MENUBAR_BACKGROUND]
        LowerPanelImage_Raw=Tool.All_Images[C.Constant_MenuBar.PANEL_BACKGROUND]
        self.UpperPanelImage=Tool.get_surface_from_image_samesize(UpperPanelImage_Raw,C.Constant_Color.WHITE,1)
        self.LowerPanelImage=Tool.get_surface_from_image_samesize(LowerPanelImage_Raw,C.Constant_Color.WHITE,1)
        self.BackGround_StartPoint_X=C.Constant_MapComponent.BACKGROUND_OFFSET_X
        self.LowerGrid=Tool.Grid(5,8,self.LowerCard_TotalOffSet_X, self.LowerCard_TotalOffSet_Y, C.Constant_PlantSelection_LayOut.Lower_PANEL_Card_X_INTERNAL, C.Constant_PlantSelection_LayOut.Lower_PANEL_Card_Y_INTERNAL)

        self.UpperGrid=Tool.Grid(1,8, self.UpperCard_TotalOffSet_X,self.UpperCard_TotalOffSet_Y,C.Constant_PlantSelection_LayOut.Upper_Panel_Card_Interval_X,C.Constant_PlantSelection_LayOut.Upper_Panel_Card_Interval_Y)

        self.ButtonImage=Tool.All_Images[C.Constant_MenuBar.START_BUTTON]
        self.ButtonImage_Width=self.ButtonImage.get_rect().width
        self.ButtonImage_Height=self.ButtonImage.get_rect().height

        self.ButtonGrid=Tool.Grid(1,1,C.Constant_PlantSelection_LayOut.Button_Image_Offset_x,C.Constant_PlantSelection_LayOut.Button_Image_Offset_y,self.ButtonImage_Width,self.ButtonImage_Height)
       
    def ProcessEvent(self, x,y,clickLeft,clickRight):
        if x is None and y is None:
            # this is handling the time events instead of user inputs
            return

        if not clickLeft and not clickRight:
            return 
        if self.UpperGrid.IsInRegion(x,y):
            r,c, index= self.UpperGrid.GetIndexFromXY(x,y)
            #note that we only need to check case where it returns
            if index < len(self.UpperCards):
                removeName=self.UpperCards[index]
                del self.UpperCards[index]
                del self.UpperCards_Type[index]
                index_of_name=self.BottomCards.index(removeName)
                self.BottomCards_Type[index_of_name]=0 #//set to normal 
                self.IsAllSelected=False

                
        if self.LowerGrid.IsInRegion(x,y):
            r,c, index= self.LowerGrid.GetIndexFromXY(x,y)
            if index < self.TotalCardNumber and len(self.UpperCards)<self.TotalSelectCardMax and self.BottomCards_Type[index] ==0:
                self.BottomCards_Type[index]=1
                selectcard_name=self.BottomCards[index]
                self.UpperCards.append(selectcard_name)
                self.UpperCards_Type.append(2)

                if(len(self.UpperCards)==self.TotalSelectCardMax):
                    self.IsAllSelected=True
        if self.ButtonGrid.IsInRegion(x,y) and self.IsAllSelected:
            self.Done=True
                
    def GetCardImages(self,CardNames, CardImageTypes):
        CardImage=[]
        for i in range(len(CardNames)):
            temp_card_name=CardNames[i]
            temp_image_type=CardImageTypes[i]
            image_list=self.CardImage_dictionary[temp_card_name]
            CardImage.append(image_list[temp_image_type])
        return CardImage


    def Draw(self, Screen):
        viewpoint=Tool.Screen.get_rect();
        viewpoint.x+=C.Constant_MapComponent.BACKGROUND_OFFSET_X
        #Tool.Screen.blit(BackGroundImage,(0,0),viewpoint )
        Tool.Screen.blit(self.UpperPanelImage, (C.Constant_PlantSelection_LayOut.Upper_Panel_Offset_X,C.Constant_PlantSelection_LayOut.Upper_Panel_Offset_Y))
        Tool.Screen.blit(self.LowerPanelImage, (C.Constant_PlantSelection_LayOut.Lower_Panel_Offset_X,C.Constant_PlantSelection_LayOut.Lower_Panel_Offset_Y))

        upper_card_image_list= self.GetCardImages(self.UpperCards,self.UpperCards_Type)
        lower_card_image_list=self.GetCardImages(self.BottomCards,self.BottomCards_Type)

        self.UpperGrid.DrawImages(Screen,upper_card_image_list)
        self.LowerGrid.DrawImages(Screen,lower_card_image_list)

        if self.IsAllSelected:
            self.ButtonGrid.DrawImages(Screen,[self.ButtonImage])

        return 