# -*- coding: UTF-8 -*-
import hexchat
from random import choice
 
__module_name__ = "Mc_Slappy"
__module_version__ = "1.0"
__module_description__ = "A Slap plugin for HexChat"
 
def slap(word, word_eol, userdata):
    nick2Slap = word[1]
    
    #Using a file for Ct with love, Worm 
    with open('%AppData%/HexChat/addons/slapActions.txt', 'r') as fp:
        lines = fp.readlines()
    
    msgpick = choice(lines)
    olSlappyCMD = msgpick.strip().format(nick2Slap)
    hexchat.command(olSlappyCMD)
    return hexchat.EAT_ALL
 
hexchat.hook_command('slap', slap, help="/slap <nick>")
hexchat.prnt(__module_name__ + " loaded.")
