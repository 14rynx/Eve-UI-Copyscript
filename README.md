# Eve-Overview-Copier
Simple script that alows you to automatically copy your overview setting to multiple chars

# Recuirements
You need Python 3.xx to use this script, Python can be found at [python.org](https://www.python.org/)

# First use
1. navigate to ```C:\Users\"Your Username"\AppData\Local\CCP\EVE\c_eve_sharedcache_tq_tranquility\settings_Default```
   here the settings for Overview and Shortcuts are saved
2. Find out witch settings you want to copy to all other chars, launch said character and figuring out witch files got written to e.g "last updated"
3. *Method 1* Copy the settings for that character and name them ```master_char.dat``` and ```master_user.dat``` respectively
   *Method 2* Rename ```master_char.dat``` and ```master_user.dat```in the script with the ones you want to have copied
4. Download ```replace.py``` and place it in the same directory
5. Run ```replace.py```. It will  replace all ```core_user_xxx.dat``` and ```core_char_xxx.dat``` files by the ```master_char.dat``` and ```master_user.dat``` files you just created
6. Finally your settings should appear on any char that had such files in this directory.

# Later use
- Whenever you want your overview set back to the master files just run ```replace.py```
- Update the faster files by replacing them with the character files of your desire

# To Note
- You can create a backup of these ```master_char.dat``` and ```master_user.dat``` files and use them later, however it is not clear if their syntax never changes with never versions of eve
- This also works on the respective folders for SISI and similar
- You could automate this with Windows Task Sceduler or similar

For any problems contact Larynx Austrene ingame
