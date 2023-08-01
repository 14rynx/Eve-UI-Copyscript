# ----------Eve UI Copyscript--------------------------
# Requirements: Python 3
# For any problems contact Larynx Austrene ingame

import os
import shutil
import ctypes, sys

#---------Innerworkings, do not touch-------------------

def get_profile_dir(server, profile):
    eve_dir = os.path.join(os.getenv('LOCALAPPDATA'), "CCP", "EVE")
    for file in os.listdir(eve_dir):
        if os.path.isdir(os.path.join(eve_dir, file)):
            if file.endswith(server):
                return os.path.join(eve_dir, file, profile)


def replace(char_master_path, user_master_path, destination_path):
    files_replaced = 0
    for file in os.listdir(destination_path):
        if os.path.isfile(os.path.join(destination_path, file)):
            destination_filepath = os.path.join(destination_path, file)

            if "core_char" in file:
                if file.split("_")[2] not in exclude_chars and char_master_path != destination_filepath:
                    shutil.copy(char_master_path, destination_filepath)
                    files_replaced += 1
            
            elif "core_user" in file:
                if file.split("_")[2] not in exclude_users and user_master_path != destination_filepath:
                    shutil.copy(user_master_path, destination_filepath)
                    files_replaced += 1

    return files_replaced


def run(profile_master, user_master, char_master, exclude_users, exclude_chars, include_profiles):
    # Generating Paths to coresponding files
    master_profile_path = get_profile_dir(*profile_master)
    char_master_filepath = os.path.join(master_profile_path, f"core_char_{char_master}.dat")
    user_master_filepath = os.path.join(master_profile_path, f"core_user_{user_master}.dat")

    for (server, profile) in include_profiles:
        profile_path = get_profile_dir(server, profile)

        try: # Try-except block, so that in case of an error you still get some output, that I might debug at some point
            print(f"Running for Profile {profile} on Server {server} ... ", end="")
            files_replaced = replace(char_master_filepath, user_master_filepath, profile_path)
        except Exception as e:
            raise
            print(f"resultet in an error: {e}")
        else:
            if files_replaced > 0:
                print(f"completed succesfully ({files_replaced} files replaced)!")
            else:
                print(f"did not result in any replaced files!")

#------------Your info goes here------------------------
# In order for this to find the right character to copy this needs your Character ID and user ID
# The user ID is usually easy to find, just look in your zkill url. The user id is usually a bit harder to find.
# The easiest way to get both is that you log in the desired character and go to
# %LOCALAPPDATA%\CCP\EVE\c_program_files_eve_sharedcache_tq_tranquility\settings_Default
# and check wicht user_xy and char_xy file got changed when you logged in. The XY at the end is the desired ID respectively
# Then check that the profiles you use in the game are the correct ones here. The master files is where the script copies from, 
# and then the unclude_profiles is where it copies to.
user_master = 123456789
char_master = 277137239
profile_master = ("tranquility", "settings_Default")

# These chars don't get copied
exclude_chars = []
exclude_users = []

include_profiles = [
    ("tranquility", "settings_Default"),
    ("singularity", "settings_Default"),
    ("thunderdome", "settings_Default"),
]

run(profile_master, user_master, char_master, exclude_users, exclude_chars, include_profiles)
# Add more runs with the same structure if you want to copy specific thing or from one profile to another

#-------------end of your info--------------------------
# Comment out this last line if you run it by script and want the shell to auto-close
input("All Done, Press any key to continue ...")
