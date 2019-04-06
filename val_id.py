# WHAT THIS CODE DOES:
# scans through validation images contained in a single folder
# collects batch of val images and copies them into respective folders
# folders are named according to the class name

# first the folders are created by scanning throught the txt file containing
#   folder names (class names).
#   folder names alone are copied to and saved into an excel sheet
# secondly, using the xlrd lib to read excel sheet cell values, the folder names
#   are scanned and val images with mathing folder (class) name is copied to resp
#   folder. Hence 50 images copied into each folder (tiny-imageNet)

import xlrd         #read excel sheet cell values
import os, fnmatch  #folder access
import shutil       #copyTo

img_path = '_PATH_TO_VAL_IMAGES_FOLDER_'
root_path = '_PATH_TO_VAL_FOLDER_'
created=[] #handle multiple files with same name (not really used though)

wb = xlrd.open_workbook(os.path.join(root_path, 'val_annotations.xlsx'))
sheet = wb.sheet_by_index(0)
def create_folders():
  for row in range(1, 10000+1):
    filename = sheet.cell_value(row,0)  #row,col
    if filename in created:
      continue
    else:
      os.mkdir(filename)
    created.append(filename)
    
def run():
  create_folders()
  i=0
  #for image in os.listdir(img_path):
  for img_index in range(10000):
    copy_from = os.path.join(img_path, 'val_%d.JPEG' %img_index)
    copy_to = sheet.cell_value(i,0)
    file1 = open("annot_maps2.txt","a") 
    file1.write(copy_from + ' : ' + copy_to + '\n')
    i+=1
    shutil.copy(copy_from, copy_to) #from, to
    if i%5 == 0: print('progress: %d' %((i+1)//100))
  file1.close() 

run()
