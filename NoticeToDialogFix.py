# -*- coding: UTF-8 -*-
# 
#=============
# = Settings =
#============================================================

# If you only want this to work on a single network
networkName = 'Rizon'
# Do you want server notices to go to  its own dialog window
putServerNotice = False


#============================================================
import os
import hexchat

__module_name__ = 'NoticeToDialogFix'
__module_version__ = '0.0.2'
__module_description__ = 'Catches any NOTICE, LOCOPS, & WALLOPS, then makes it go to its own dialog window'


def servNotice(word, word_eol, userdata):
    if networkName != '' and hexchat.get_info('network') != networkName: return hexchat.EAT_NONE
    ircmsg = word_eol[0]

    if ' WALLOPS :' in ircmsg or ' LOCOPS :' in ircmsg:
        # ':[Nick]!~[hostname]@[IPAddress] WALLOPS :[message]'
        msgSplit = ircmsg.split(' ',2)
        fullFrom = msgSplit[0]
        fromName = fullFrom.split('!',1)[0][1:]
        cmd = msgSplit[1]
        if cmd != 'WALLOPS' or cmd != 'LOCOPS' : return hexchat.EAT_NONE        
        hexchat.command('query {}'.format(fromName))
        return hexchat.EAT_NONE        

    elif ' NOTICE ' in ircmsg:
        # ':[Nick]!~[hostname]@[IPAddress] NOTICE [channel] :[message]'
        msgSplit = ircmsg.split(' ',3)
        fullFrom = msgSplit[0]
        try: 
            fromName = fullFrom.split('!',1)[0][1:] 
        except: 
            if not putServerNotice: return hexchat.EAT_NONE
            fromName = fullFrom
        target = msgSplit[2]    
        if target.startswith('#'): return hexchat.EAT_NONE        
        hexchat.command('query {}'.format(fromName))
        return hexchat.EAT_NONE

    else:
        return hexchat.EAT_NONE
    

hexchat.hook_server('RAW LINE', servNotice, priority=hexchat.PRI_HIGH)

hexchat.prnt(__module_name__ + ' loaded.')
