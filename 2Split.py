import os
import image_slicer

#################################################################################################
# 2Split Directory Manager for image_slicer v1.01 by Francesco Paterna
# Take the image from a directory, split them in two and put the cutted image in two separated
# directory
#
# Please insert all the paths and name that you prefer on the parameters tables below
#################################################################################################
source_path = "[SOURCE_PATH]" # Where the images are
output_path = "[OUTPUT_PATH]" # Where the two directory with the cutted images will be stored
RIGHT_CUT_DIR_NAME = "[RIGHT_CUT DIR_NAME]" #Name of the directory thay contains the right cuts
LEFT_CUT_DIR_NAME = "[LEFT_CUT DIR_NAME]" #Name of the directory thay contains the left cuts
LEFT_PREFIX = "[INSERT LEFT_FRAME NAME]" #Prefix for left cuts
RIGHT_PREFIX = "[INSERT RIGHT_FRAME NAME]" #PRefix for right cuts
#################################################################################################



#WARNING os.mkdir stops the entire script if the folders already exist!
#TODO wirte if check in v1.02

os.mkdir(output_path + RIGHT_CUT_DIR_NAME)
os.mkdir(output_path + LEFT_CUT_DIR_NAME)

t = 0
for file in os.listdir(source_path):
    if file.endswith(".jpg"):
        print(file)
        crop_frame = image_slicer.slice(source_path + file, 2, save=False)
        crop_Even = (crop_frame[0],)
        crop_Odd = (crop_frame[1],)
        image_slicer.save_tiles(crop_Even, directory=output_path + RIGHT_CUT_DIR_NAME,
                                prefix=RIGHT_PREFIX + str(t), format='jpeg')
        image_slicer.save_tiles(crop_Odd, directory=output_path + LEFT_CUT_DIR_NAME,
                                prefix=LEFT_PREFIX + str(t), format='jpeg')
        t = t + 1
        continue
    else:
        continue
