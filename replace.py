# ----------Eve UI Copyscript--------------------------
# Requirements: Python 3
# For any problems contact Larynx Austrene ingame

import os
import shutil
import ctypes, sys

#------------Your info goes here------------------------
# In order for this to find the right character to copy this needs your Character ID and user ID
# The user ID is usually easy to find, just look in your zkill url. The user id is usually a bit harder to find.
# The easiest way to get both is that you log in the desired character and go to
# %LOCALAPPDATA%\CCP\EVE\c_program_files_eve_sharedcache_tq_tranquility\settings_Default
# and check wicht user_xy and char_xy file got changed when you logged in. The XY at the end is the desired ID respectively
user_master = "15402804"
char_master = "2114060571"

# In case you or sharedcache folders are at a different location you can change the paths here
tq_dir = os.path.join(os.getenv('LOCALAPPDATA'), "CCP\EVE\c_program_files_eve_sharedcache_tq_tranquility\settings_Default")
sisi_dir =  os.path.join(os.getenv('LOCALAPPDATA'), "CCP\EVE\c_program_files_eve_sharedcache_sisi_singularity\settings_Default")
#-------------end of your info--------------------------

def replace(files, char_master_path, user_master_path, dest_dir):
                    for file in files:
                        
                        if "core_char" in file and not char_master in file:
                                shutil.copy(char_master_path, os.path.join(dest_dir, file))
                                print("Overwriten: {}".format(file))

                        if "core_user" in file and not user_master in file:
                                shutil.copy(user_master_path, os.path.join(dest_dir, file))
                                print("Overwriten: {}".format(file))

# Generating Paths to coresponding files
char_master_path = os.path.join(tq_dir, "core_char_{}.dat".format(char_master))
user_master_path = os.path.join(tq_dir, "core_user_{}.dat".format(user_master))

try: # Try-except block, so that in case of an error you still get some output, that I might debug at some point
        print("Tranquility")
        for root, dirs, files in os.walk(tq_dir):
                replace(files, char_master_path, user_master_path, tq_dir)

        # Comment out the next 3 lines if you dont want to copy the settings to singularity              
        print("Singularity")
        for root, dirs, files in os.walk(sisi_dir):
                replace(files, char_master_path, user_master_path, sisi_dir)
                
except Exception as e:
        print("An Error occurred while: copying: {}".format(str(e)))
else:	
        print("Done")

# Comment out this last line if you run it by script and want the shell to auto-close
input("Press any key to continue ...")
	
