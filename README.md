# Eve-Overview-Copier
Simple script that alows you to automatically copy your overview setting to multiple chars

# To use
1. navigate to ```C:\Users\"Your Username"\AppData\Local\CCP\EVE\c_eve_sharedcache_tq_tranquility\settings_Default``
   here the settings for Overview and Shortcuts are saved
2. Find out witch settings you want to copy to all other chars, launch said character and figuring out witch files got written to e.g "last updated"
3. Copy the settings for that character and name them ````master_char.dat`` and ``master_user.da``" respectively
4. Run this script it will  replace all ```core_user_xxx.dat``` and ```core_char_xxx.dat``` files by master_char.dat and master_user.dat
5. Finally your settings should appear on any char that had such files in this directory.

# To Note
- You can create a backup of these ```master_char.dat``` and ```master_user.dat``` files and use them later, however it is not clear if their syntax never changes with never versions of eve
  - This also works on the respective folders for SISI and similar
  - You might also rename the files in this script and not create  ``` master_char.dat``` and ```master_user.dat``` at all

For any problems contact Larynx Austrene ingame
