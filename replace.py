# This is made to copy Eve Settings to chars

# To use:
# 1. navigate to C:\Users\"Your Username"\AppData\Local\CCP\EVE\c_eve_sharedcache_tq_tranquility\settings_Default
#    here the settings for Overview and Shortcuts are safed
# 2. Find out witch settings you want to copy to all other chars, launch said character and figuring out witch files got written to e.g "last updated"
# 3. Copy the settings for that character and name them "master_char.dat" and "master_user.dat" respectively
# 4. Run this script it will  replace all core_user_xxx.dat and core_char_xxx.dat files by master_char.dat and master_user.dat
# Finally your settings should appear on any char that had such files in this directory.

# To Note:
#  - You can create a backup of these "master_char.dat" and "master_user.dat" files and use them later, however it is not clear if their syntax never changes with never versions of eve
#  - This also works on the respective folders for SISI and similar
#  - You might also rename the files in this script and not create  "master_char.dat" and "master_user.dat" at all

# For any problems contact Larynx Austrene ingame

import os
import shutil
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin(): # Find out if this script is run as admin, to circumvent file permission issues

	# Gets the directory of this file, which is not always cwd
	use_dir = os.path.dirname(os.path.realpath(__file__))
	print("Searching in directory: {}".format(use_dir))

	# These filenames might be replaced by the files you want to use as master
	char_master = os.path.join(use_dir, "master_char.dat")
	user_master = os.path.join(use_dir, "master_user.dat")

	try: # Try-except block, so that in case of an error you still get some output, that I might debug at some point
		for root, dirs, files in os.walk(use_dir):
			for file in files:

				if "core_char" in file:
					shutil.copy(char_master, file)
					print("Overwriten: {}".format(file))

				if "core_user" in file:
					shutil.copy(user_master, file)
					print("Overwriten: {}".format(file))
	except Exception as e:
		print("An Error occurred while: copying: {}".format(str(e)))
	else:	
		print("Done")

	input("Press any key to continue ...")
	
else: # If this is not already admin elevate and run again

	print("Running as admin ...")
	try: # Try-except block, so that in case of an error you still get some output, that I might debug at some point
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
	except Exception as e:
		print("An Error occurred  while elevating: {}".format(str(e)))


