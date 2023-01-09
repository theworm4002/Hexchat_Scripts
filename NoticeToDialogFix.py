# -*- coding: UTF-8 -*-
import os
import hexchat

__module_name__ = "NoticeToDialogFix"
__module_version__ = "0.0.1"
__module_description__ = "Catches any NOTICE and makes it go to it's own Dialog window"

# If you only want this to work on a single network
networkName = 'Rizon'

def servNotice(word, word_eol, userdata):
    if networkName != '' and hexchat.get_info("network") != networkName: return hexchat.EAT_NONE
    ircmsg = word_eol[0]
    name = ircmsg.split('!',1)[0][1:]
    msgSplit = ircmsg.split(' ',3)
    target = msgSplit[2]
    if target.startswith('#'): return hexchat.EAT_NONE
    hexchat.command('query {}'.format(name))
    return hexchat.EAT_NONE


hexchat.hook_server("NOTICE", servNotice, priority=hexchat.PRI_HIGH)
