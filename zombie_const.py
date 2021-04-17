import os 
dir = r'D:\Code\PlantsVsZombies\resources\graphics\Plants'

const = '\t'

def generate_image_code(dirname, subdir):
    class_list = []
    class_name = f'class {dirname}Image(Enum):'
    class_list.append(class_name)
    if len(subdir) == 0:
        class_enum = const + f"{dirname} =\"{dirname}\""
        class_list.append(class_enum)
    else:
        for dir in subdir:        
            class_enum = const + f"{dir} =\"{dir}\""
            class_list.append(class_enum)
    return '\n'.join(class_list) + '\n'




for subdir in os.listdir(dir):
    sub_dir_full_path = os.path.join(dir,subdir)
    sub_dir_2 =   os.listdir(sub_dir_full_path)
    sub_dir_2_filtered = [ name for name in sub_dir_2 if os.path.isdir(os.path.join(sub_dir_full_path, name)) ]

    code = generate_image_code(subdir, sub_dir_2_filtered)
    print(code)
    # if(len(sub_dir_2_filtered) >0):
    #     print(f'{subdir} has the follwing sub dir {",".join(sub_dir_2)}')
    # else:
    #     print(f'{subdir} has is the singel')


code_list= []
code_list.append(f'class PlantNameEnum(Enum):')
for subdir in os.listdir(dir):
    class_enum = const + f"{subdir} =\"{subdir}\""
    code_list.append(class_enum)

#print('\n'.join(code_list) + '\n')


code_list= []
code_list.append('PlantName2ImageList = {')
def add_quote(input):
    return f'\"{input}\"'
for subdir in os.listdir(dir):
    sub_dir_full_path = os.path.join(dir,subdir)
    sub_dir_2 =   os.listdir(sub_dir_full_path)
    sub_dir_2_filtered = [ name for name in sub_dir_2 if os.path.isdir(os.path.join(sub_dir_full_path, name)) ]

    if len(sub_dir_2_filtered) == 0:
        sub_dir_2_filtered = [subdir]
    sub_dir_2_filtered_quoted = [ add_quote(name) for name in sub_dir_2_filtered] 
    code_single_line = f'PlantNameEnum.{subdir}:[{",".join(sub_dir_2_filtered_quoted)}],'
    code_list.append(code_single_line)

#print('\n'.join(code_list) + '\n')



# #---now let's handle zombies more carefully#

dir_zombie = r'D:\Code\PlantsVsZombies\resources\graphics\Zombies'

code_list= [] 
code_list.append(f'class ZombieImageEnum(Enum):')
zombie_name_list = []
for subdir_1 in os.listdir(dir_zombie):
    subdir_1_full_path = os.path.join(dir_zombie,subdir_1)
    for sub_dir_2 in os.listdir(subdir_1_full_path):
        #subdir_2_full_path = os.path.join(dir, subdir_1, sub_dir_2)
        zombie_name_code =const +  f'{sub_dir_2}={add_quote(sub_dir_2)}'
        code_list.append(zombie_name_code)
        zombie_name_list.append(add_quote(sub_dir_2))

print('\n'.join(code_list))
print(f'ZombieImageArray=[{",".join(zombie_name_list)}]')



dir_zombie = r'D:\Code\PlantsVsZombies\resources\graphics\Bullets'

code_list= [] 
code_list.append(f'class BulletImageEnum(Enum):')
zombie_name_list = []
for subdir_1 in os.listdir(dir_zombie):
        zombie_name_code =const +  f'{subdir_1}={add_quote(subdir_1)}'
        code_list.append(zombie_name_code)
        zombie_name_list.append(add_quote(subdir_1))

print('\n'.join(code_list))
print(f'BulletImagesArray=[{",".join(zombie_name_list)}]')



    