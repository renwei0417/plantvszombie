from PIL import Image
import os 
import glob
def transparent(myimage, new_image):
    img = Image.open(myimage)
    img = img.convert("RGBA")

    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)
    
    img.save(new_image, "PNG")   

#transparent(r'D:\Code\PlantsVsZombies\resources\graphics\Plants\Squash\Squash\Squash_1.png','test.png')


# f = []
# for (dirpath, dirnames, filenames) in os.walk(r'D:\Code\PlantsVsZombies\resources\graphics'):
#     f.extend(filenames)

# print(f)

files = glob.glob(r'D:\Code\PlantsVsZombies\resources\graphics\**\*.png', recursive= True)
for file in files:
    transparent(file,file)