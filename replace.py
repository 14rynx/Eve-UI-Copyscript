# ----------Eve UI Copyscript--------------------------
# Requirements: Python 3
# For any problems contact Larynx Austrene ingame

import os
import shutil
import ctypes, sys

#------------Your info goes here------------------------
# In order for this to find the right character to copy this needs your Character ID and user ID
# The character ID is usually easy to find, just look in your zkill url. The user id is usually a bit harder to find.
# The easiest way to get both is that you log in the desired character and go to
# %LOCALAPPDATA%\CCP\EVE\c_program_files_eve_sharedcache_tq_tranquility\settings_Default
# and check wicht user_xy and char_xy file got changed when you logged in. The XY at the end is the desired ID respectively
user_master = "15402804"
char_master = "2114060571"

# These chars don't get copied
exclude_chars = []
exclude_users = []

# In case you or sharedcache folders are at a different location you can change the paths here
tq_dir = os.path.join(os.getenv('LOCALAPPDATA'), "CCP\EVE\c_program_files_eve_sharedcache_tq_tranquility\settings_Default")
sisi_dir =  os.path.join(os.getenv('LOCALAPPDATA'), "CCP\EVE\c_program_files_eve_sharedcache_sisi_singularity\settings_Default")
#-------------end of your info--------------------------

def replace(char_master_path, user_master_path, dest_dir):
    for root, dirs, files in os.walk(dest_dir):
        for file in files:
            destination_path = os.path.join(dest_dir, file)

            if "core_char" in file:
                if file.split("_")[2] not in exclude_chars and char_master_path != destination_path:
                    shutil.copy(char_master_path, os.path.join(dest_dir, file))
                    print(f"Overwriten character file: {file}")
            
            elif "core_user" in file:
                if file.split("_")[2] not in exclude_users and user_master_path != destination_path:
                    shutil.copy(user_master_path, os.path.join(dest_dir, file))
                    print(f"Overwriten user file: {file}")

# Generating Paths to coresponding files
char_master_path = os.path.join(tq_dir, f"core_char_{char_master}.dat")
user_master_path = os.path.join(tq_dir, f"core_user_{user_master}.dat")

try: # Try-except block, so that in case of an error you still get some output, that I might debug at some point
    print("Tranquility")
    replace(char_master_path, user_master_path, tq_dir)

    # Comment out the next 3 lines if you dont want to copy the settings to singularity              
    print("Singularity")
    replace(char_master_path, user_master_path, sisi_dir)
                
except Exception as e:
    raise
    print("An Error occurred while: copying: {}".format(str(e)))
else:	
    print("Completed succesfully")

# Comment out this last line if you run it by script and want the shell to auto-close
input("Press any key to continue ...")
