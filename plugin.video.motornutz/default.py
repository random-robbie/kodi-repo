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

addonID = 'plugin.video.motornutz'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "MotoGP"
YOUTUBE_CHANNEL_ID_2 = "CarjamRadio"
YOUTUBE_CHANNEL_ID_3 = "TopGear"
YOUTUBE_CHANNEL_ID_4 = "britishdriftchamp"
YOUTUBE_CHANNEL_ID_5 = "RSRNurburg"
YOUTUBE_CHANNEL_ID_6 = "TheSmokingTire"
YOUTUBE_CHANNEL_ID_7 = "UCUb_HfsiE_FlcFho2FrWxhw"
YOUTUBE_CHANNEL_ID_8 = "DIRTBIKESandQUADS"
YOUTUBE_CHANNEL_ID_9 = "redbull"
YOUTUBE_CHANNEL_ID_10 = "JBB013"
YOUTUBE_CHANNEL_ID_11 = "mightycarmods"

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
        title="Moto GP",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://www.tippingcompetitions.com/images/competition/logo/motogp.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="CarjamRadio",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-19oOI-64FRI/AAAAAAAAAAI/AAAAAAAAAAA/Whu13akf2Vg/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Top Gear",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-3778qljvKEQ/AAAAAAAAAAI/AAAAAAAAAAA/g-bHapsDzwQ/s176-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="British Drift Championship",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-M-xVIxo_Gks/AAAAAAAAAAI/AAAAAAAAAAA/LtZ6V0zT87k/s176-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="RSRNurburg",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-S8Njnvd_h9U/AAAAAAAAAAI/AAAAAAAAAAA/NrU7TjrZ1gQ/s176-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Smoking Tire",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-hXfw2tAFSK4/AAAAAAAAAAI/AAAAAAAAAAA/v7cLgaVP-E8/s176-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Amazing Drifting Cars",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.ytimg.com/vi/pCt0KXC1tng/maxresdefault.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Two Wheels TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-d953aloYYaE/AAAAAAAAAAI/AAAAAAAAAAA/g7jJc3Xkhm8/s176-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Redbull",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-V1E6nSEmRlM/AAAAAAAAAAI/AAAAAAAAAAA/zFmOgJmgH2s/s176-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="JBB013 - Supercar Videos",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-VH57gvibcnc/AAAAAAAAAAI/AAAAAAAAAAA/6cmXWTfHv7A/s176-c-k-no/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Mighty Car Modz",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-b8-0ku2pp-U/AAAAAAAAAAI/AAAAAAAAAAA/2QftimURo_A/s176-c-k-no/photo.jpg",
        folder=True )
				
    plugintools.add_item( 
        #action="", 
        title="Adam Phillpotts",
        url="plugin://plugin.video.youtube/channel/UC5lqC84Kc3mIiUMASF3L-Wg/",
        thumbnail="https://yt3.ggpht.com/-DKtpB_CoyZc/AAAAAAAAAAI/AAAAAAAAAAA/tBtRAlbiRQ8/s176-c-k-no/photo.jpg",
        folder=True )
		
				
    plugintools.add_item( 
        #action="", 
        title="The Stig",
        url="plugin://plugin.video.youtube/channel/UCELrWeVLazR49umE5qSF3VQ",
        thumbnail="https://yt3.ggpht.com/-2gd_UihShb8/AAAAAAAAAAI/AAAAAAAAAAA/ZZBzvr2PCfY/s100-c-k-no/photo.jpg",
        folder=True )


    
run()
