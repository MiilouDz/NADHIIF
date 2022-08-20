
import os 
import asyncio
import config
import logging
from pyrogram import Client, filters 
from core.checker import video_checker,image_checker
from pyrogram.types import Message


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)



app = Client("Linux64",api_id=config.API_ID,api_hash=config.API_HASH,bot_token=config.BOT_TOKEN,in_memory=True)

@app.on_message(filters.chat(config.GROUP_ID))
async def group_handler(client:Client,message:Message):
    logging.info("GROUP_HANDLER TRIGGERED")
    

    if message.photo:
        logging.info("Analyzing Photo")
        file_path = await message.download()


        if image_checker(file_path=file_path):
            logging.info("NSFW Detected")
            resp = await message.reply("Analyzing...")
            await asyncio.sleep(2)
            await resp.edit_text("NSFW Detected")
            await message.delete()        
            await resp.edit_text("Message Removed")
            await asyncio.sleep(2)
            await client.delete_messages(message.chat.id,resp.id)

        os.remove(file_path)

        # Delete

    if message.video :
        logging.info("Analyzing Video")
        file_path = await message.download()
        if video_checker(file_path=file_path):
            logging.info("NSFW Detected")
            resp = await message.reply("Analyzing...")
            await asyncio.sleep(2)
            await resp.edit_text("NSFW Detected")
            await message.delete()        
            await resp.edit_text("Message Removed")
            await asyncio.sleep(2)
            await client.delete_messages(message.chat.id,resp.id)
            
        os.remove(file_path)


    

    if message.from_user.is_fake:
        await client.ban_chat_member(config.GROUP_ID,message.from_user.id)

    if message.from_user.is_scam:

        await client.ban_chat_member(config.GROUP_ID,message.from_user.id)

    if message.from_user.is_bot:

        await client.ban_chat_member(config.GROUP_ID,message.from_user.id)

    if config.BAN_ACCOUNT_WITHOUT_PROFILE_PIC:
        if not message.from_user.dc_id:
            await client.ban_chat_member(config.GROUP_ID,message.from_user.id)

    return None 


@app.on_message(filters.new_chat_members)
async def new_member(client:Client,message:Message):
    logging.info("NEW MEMBER JOINED")

    if message.from_user.is_bot:
        logging.info("BOT_DETECTED")
        await client.ban_chat_member(config.GROUP_ID,message.from_user.id)
        

app.run()



