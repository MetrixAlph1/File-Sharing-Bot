#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Nᴏᴛʜɪɴɢ Hᴇʀᴇ Bʀᴏ\nI ᴀᴍ ᴊᴜsᴛ ᴀ ʙᴏᴛ ᴛᴏ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs Aɴᴅ only ᴍʏ 𝐌𝐀𝐒𝐓𝐄𝐑 ᴀɴᴅ ᴏᴛʜᴇʀ 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐒𝐄𝐃 ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss Iᴛ ғʀᴏᴍ 𝐒𝐏𝐄𝐂𝐈𝐀𝐋 ʟɪɴᴋ'S\n\n○ OWNER : <a href='tg://user?id={OWNER_ID}'>This Person</a></b>",
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❌ Exit MENU ❌", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
