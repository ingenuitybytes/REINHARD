import os
from dotenv import load_dotenv

import logging
from colorlog import ColoredFormatter

################logColoringSettings################
LOG_LEVEL = logging.DEBUG
LOGFORMAT = " %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"

logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
log = logging.getLogger('pythonConfig')
log.setLevel(LOG_LEVEL)
log.addHandler(stream)

################colorPalette################
class Style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
################TOKENandDEVTHINGS################
load_dotenv()
TOKEN = os.environ["DISCORD_BOT_TOKEN"]
APPLICATION_ID = os.environ["DISCORD_APPLICATION_ID"]
GUILD_ID = os.environ["DISCORD_GUILD_ID"]

################sourceCodeGithub################
GITHUB_LINK = "https://github.com/Tutu-Inc/REINHARD"

################createMainVoice################
TEMP_MAIN_CHANNEL = "➕〡CREATE CHANNEL"
TEMP_MAIN_CATEGORY = "──༺VOICECHANNEL༻──"

################createSchuleVoice################
TEMP_SCHULE_CHANNEL = "➕〡LEARNING ROOM"
TEMP_SCHULE_CATEGORY = "─────༺TGM༻─────"

################music################
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
    }
YDL_OPTIONS = {
    'format':'bestaudio',
     'quiet': True, 
     'default_search':"ytsearch", 
     'noplaylist':'True'
    }

################channels################
MUSICCHANNEL = "musik"
RULEROLECHANNEL = "regeln"

################roles################
MODERATOR_ROLE_NAME = "Moderatoren"

################emojis################
#games
MINECRAFT_EMOJI = "<:minecraft:880179878601846835>"
AVORION_EMOJI = "<:avorion:880179879646216222>"
SCRAP_EMOJI = "<:scrap:880179878631211008>"
KERBAL_EMOJI = "<:ksp:880179878954164224>"
FACTORIO_EMOJI = "<:factorio:880179878526332970>"
UNITY_EMOJI = "<:unity:880179878010449960>"
#music
PLAYORPAUSE_EMOJI = "<:playorpause:880179840119095346>"
STOP_EMOJI ="<:stop:880179840026812486>"
NEXTTRACK_EMOJI = "<:nexttrack:880179839909376011>"
COUNTERCLOCKWISE_EMOJI = "<:counterclockwisearrows:880179840173621259>"
SHUFFLETRACKS_EMOJI = "<:shuffletracks:880179840056197151>"
STAR_EMOJI = "<:star:880179840140054539>"
CROSSMARK_EMOJI = "<:crossmark:880179839859060778>"
#blurble
BLURBLEYES_EMOJI = "<:blurpleYES:880180644804698163>"
BLURPLENO_EMOJI = "<:blurpleNO:880180644368494655>"
BLURPLETEXTCHANNEL_EMOJI = "<:blurpletextchannel:880196321187864606>"
BLURPLEVOICECHANNEL_EMOJI = "<:blurplevoicechannel:880197686870020148>"
BLURPLEUNMUTED_EMOJI = "<:blurpleunmuted:880198186931744808>"
BLURPLESETTINGS_EMOJI = "<:blurplesettings:880198972654895105>"
BLURPLEGUIDE_EMOJI = "<:blurpleGuide:880180644850847774>"
BLURPLEANNOUNCEMENTS_EMOJI = "<:blurpleannouncements:880180645140246568>"
BLURPLEBELL_EMOJI = "<:blurplebell:880180645228314695>"
BLURPLECAMERA_EMOJI = "<:blurplecamera:880180644892770326>"
BLURPLECERTIFIEDMODERATOR_EMOJI = "<:blurplecertifiedmoderator:880180644863438879>"
BLURPLECOMPASS_EMOJI = "<:blurplecompass:880180645521915934>"
BLURPLEDEAFENED_EMOJI = "<:blurpledeafened:880180645509353522>"
BLURPLEDISCONNECT_EMOJI = "<:blurpledisconnect:880180645542895696>"
BLURPLEEMPLOYEE_EMOJI = "<:blurpleemployee:947167754564276276>"
BLURPLEGIFT_EMOJI = "<:blurplegift:880180645240901663>"
BLURPLEIMAGE_EMOJI = "<:blurpleimage:880180645559689347>"
BLURPLEINBOX_EMOJI = "<:blurpleinbox:880180645261877290>"
BLURPLEINTEGRATION_EMOJI = "<:blurpleintegration:880180645614194698>"
BLURPLEINVITE_EMOJI = "<:blurpleinvite:880180645744226404>"
BLURPLELIBRARY_EMOJI = "<:blurplelibrary:880180645752614932>"
BLURPLELINE_EMOJI = "<:blurpleline:880180646067183676>"
BLURPLELINK_EMOJI = "<:blurplelink:880180645480005673>"
BLURPLEMEMBERS_EMOJI = "<:blurplemembers:880180645752627271>"
BLURPLEMUTED_EMOJI = "<:blurplemuted:880180645878464582>"
BLURPLEPARTNER_EMOJI = "<:blurplepartner:880180645752619009>"
BLURPLEROCKET_EMOJI = "<:blurplerocket:880180644817297448>"
BLURPLEROLES_EMOJI = "<:blurpleroles:880180644829872251>"
BLURPLERULES_EMOJI = "<:blurplerules:880180645400313857>"
BLURPLESEARCH_EMOJI = "<:blurplesearch:880180646209802290>"
BLURPLESHOP_EMOJI = "<:blurpleshop:880180646276915220>"
BLURPLESTAR_EMOJI = "<:blurplestar:880180646209790062>"
BLURPLESUPPORT_EMOJI = "<:blurplesupport:880180646054625342>"
BLURPLETICKET_EMOJI = "<:blurpleticket:880180646268534784>"
BLURPLEUNDEAFENED_EMOJI = "<:blurpleundeafened:880180646243356692>"
WELCOME1_EMOJI = "<:welcome1:880180644825673769>"
WELCOME2_EMOJI = "<:welcome2:880180645169606676>"