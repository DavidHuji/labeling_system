####################################################
####################################################
#######                                      #######
#######       Patches Labeling System        #######
#######                                      #######
####################################################
####################################################
# input order: input_folder, outputs_folder, patch_size, resize_factor

import numpy as np
import os
import random, cv2, sys
from matplotlib import pyplot as plt
from matplotlib import image as img_saver
from pathlib import Path

LABELS = ['1', '2', '3', '4']


print(f'inputs are: {sys.argv[1:]}')
input_folder, outputs_folder, patch_size, resize_factor = sys.argv[1:5]
if not os.path.exists(input_folder):
    print(f'The following input path not exists: {input_folder}')
    exit(0)
if not os.path.exists(outputs_folder):
    print(f'The following input path not exists: {outputs_folder}')
    exit(0)
resize_factor = int(resize_factor)
patch_size = int(patch_size)

in_imgs_paths_list = [os.path.join(input_folder, o) for o in os.listdir(input_folder)
                      if (not os.path.isdir(os.path.join(input_folder, o))) and (o[-3:] == 'jpg' or o[-3:] == 'png' or o[-3:] == 'PNG' or o[-3:] == 'npz')]


patches = []
cur_patch = []
rand_x, rand_y, cur_path, img_path = 0, 0, 0, 0


def press(event):
    patches.append((cur_path, rand_x, rand_y, event.key))

    if event.key in LABELS:
        img_name = str(img_path).split('.')[-2].split('\\')[-1]
        img_saver.imsave(Path(outputs_folder) / f'Lable_{int(event.key)} {(img_name, rand_x, rand_y)}',
                         cur_patch, cmap='gray')
        print(f'Lable_{int(event.key)} {(img_name, rand_x, rand_y)} was saved successfully')
    plt.close()


while True:
    img_path = in_imgs_paths_list[random.randint(0, len(in_imgs_paths_list) - 1)]
    try:
        img = plt.imread(img_path)
    except:
        data = np.load(img_path)
        try:
            img = data['data'][int(sys.argv[5])]
        except:
            print(f'\n\nIllegal input for channel index')
            break
    shape = np.array(img).shape
    print(shape)
    rand_x, rand_y = random.randint(patch_size, shape[0] - patch_size), random.randint(patch_size, shape[1] - patch_size)
    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('key_press_event', press)
    cur_patch = img[rand_x:rand_x + patch_size, rand_y:rand_y + patch_size]
    cur_patch = cv2.resize(cur_patch, (0, 0), fx=1 / resize_factor, fy=1 / resize_factor, interpolation=cv2.INTER_LINEAR)
    ax.imshow(cur_patch, cmap='gray')
    plt.show()
