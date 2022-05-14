"""Check if userbot alive or not . """


import asyncio , time
from telethon import events
from userbot import StartTime , catdef
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME, catdef , catversion
from userbot.utils import admin_cmd,sudo_cmd
from telethon import version
from platform import python_version, uname

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"

CAT_IMG = Config.ALIVE_PIC

@borg.on(admin_cmd(outgoing=True, pattern="alive$"))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = catdef.get_readable_time((time.time() - StartTime))
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if CAT_IMG:
         cat_caption  = f"**MY BOT IS RUNNING SUCCESFULLY**\n\n"
         cat_caption += f"**Database Status: Databases functioning normally!\n**"   
         cat_caption += f"☞Telethon version : `{version.__version__}\n`"
         cat_caption += f"☞Catuserbot Version : `{catversion}`\n"
         cat_caption += f"☞Python Version : `{python_version()}\n\n`"
         cat_caption += f"**cat🐱 is always with you, my master!\n**"
         cat_caption += f"☞My peru Master: {DEFAULTUSER}\n"
         cat_caption += f"☞uptime : `{uptime}\n`"
         cat_caption +=	f"☞**Click **[here](https://github.com/sandy1709/catuserbot) to deply catuserbot"
         await borg.send_file(alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id)
         await alive.delete()
    else:
        await alive.edit(f"**MY BOT IS RUNNING SUCCESFULLY**\n\n"
                         "**Database Status: Databases functioning normally!\n**" 
                         f"☞Telethon version : `{version.__version__}\n`"
			 f"☞Catuserbot Version : `{catversion}`\n"
                         f"☞Python Version : `{python_version()}\n\n`"
                         "**cat🐱 is always with you, my master!\n**"
                         f"☞My peru Master: {DEFAULTUSER}\n"
                         f"☞uptime : `{uptime}\n`"
                         f"☞**Click **[here](https://github.com/sandy1709/catuserbot) to deply catuserbot"
                        )         

@borg.on(sudo_cmd(pattern="sudo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    uptime = catdef.get_readable_time((time.time() - StartTime))
    await event.reply(" SUDO COMMANDS ARE WORKING PERFECTLY \n\n"
                     f"☞Telethon version: {version.__version__}\n"
                     f"☞Python: {python_version()}\n"
                     f"☞My peru owner: {DEFAULTUSER}\n"
                     f"**uptime :** `{uptime}\n`"
                     #"Deploy this userbot Now"
                    )
       
CMD_HELP.update({"alive": "`.alive` :\
      \nUSAGE: Type .alive to see wether your bot is working or not. "
}) 
