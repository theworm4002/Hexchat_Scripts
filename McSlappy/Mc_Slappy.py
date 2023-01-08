# -*- coding: UTF-8 -*-
import os
import hexchat
from random import choice

__module_name__ = "Mc_Slappy"
__module_version__ = "1.0"
__module_description__ = "A Slap plugin for HexChat"

dirName = os.path.dirname(os.path.abspath(__file__))
McSlappysActionFile = '{}/slapActions.txt'.format(dirName)

def slap(word, word_eol, userdata):
    global McSlappysActions
    nick2Slap = word[1]    
    msgpick = choice(McSlappysActions)
    nick2SlapBold = '{}'.format(nick2Slap)
    olSlappyCMD = msgpick.strip().format(nick2SlapBold)
    hexchat.command(olSlappyCMD)
    return hexchat.EAT_ALL
 
def reloadMcSlappy(word, word_eol, userdata):
    global McSlappysActions
    #Using a file for Ct with love, Worm 
    with open(McSlappysActionFile, 'r') as fp:
        McSlappysActions = fp.readlines()
    hexchat.prnt("McSlappysActions file loaded")
    return hexchat.EAT_ALL

hexchat.hook_command('slap', slap, help="/slap <nick>")
hexchat.hook_command('reloadMcSlappy', reloadMcSlappy, help="/reloadMcSlappy reloads McSlappy's Action File")

try:
    reloadMcSlappy(1,2,3)
    hexchat.prnt(__module_name__ + " loaded.")
except:
    hexchat.prnt("Failed to load")
