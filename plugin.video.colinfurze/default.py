# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Colin Furze Addon by @random_robbie
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: random_robbie
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.colinfurze'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "colinfurze"
skin_used = xbmc.getSkinDir()
if skin_used == 'skin.confluence':
    xbmc.executebuiltin('Container.SetViewMode(500)') # "Thumbnail" view
elif skin_used == 'skin.aeon.nox':
    xbmc.executebuiltin('Container.SetViewMode(512)') # "Info-wall" view. 

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title=" Colin Furze Crazy Inventions ",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://griffin.mixrmedia.com/user_photos/blog/2013/06/13/f2c21481fdd026ab08453d65af53b176-500.jpg",
        folder=True )

    
run()
