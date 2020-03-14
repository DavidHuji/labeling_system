# labeling_system
A simple python script for a quick image labeling.
Given an images directory, the script iterativelly presents random patches and wait for getting a lable from the user, when the user press the lable, it saves the patch when it's name contains the given lable and the patch source, then the next itration starts.

##usage
-1- First make sure you have the required Python packeges (you can run pip install -r requirements.txt).
-2- Run the following: python main.py input_folder outputs_folder patch_size resize_factor
                      Example: python main.py C:\labeling_system\folder_that_contains_all_the_images  C:\Desktop\labeling_system\folder_for_saving_patchs_with_labels 60 2

-3- Random patches will be displayed one after the other, each time press the label and the next patche will be displayed.
-4- The patches are saved in the given output folder when their name contains their label and their source (top left point and the original image name).
-5- For stopping the program just close the shell and that's it, everything is saved during the labeling.
  
