from time import time

from ..helper.ext_utils.bot_utils import new_task
from ..helper.telegram_helper.button_build import ButtonMaker
from ..helper.telegram_helper.message_utils import send_message, edit_message, send_file
from ..helper.telegram_helper.filters import CustomFilters
from ..helper.telegram_helper.bot_commands import BotCommands
from ..helper.telegram_helper.media_utils import send_photo  # New import for sending images


@new_task
async def start(_, message):
    buttons = ButtonMaker()
    buttons.url_button(
        "Base Repo", "https://www.github.com/anasty17/mirror-leech-telegram-bot"
    )
    buttons.url_button("Leech Group", "https://t.me/Public_Mirror_Leech_Group")
    reply_markup = buttons.build_menu(2)
    
    # Send image along with the message
    image_url = "https://envs.sh/v_K.jpg"
    if await CustomFilters.authorized(_, message):
        start_string = f"""
Listen up, pal. This bot's got the power to mirror from links, tgfiles, torrents, nzb, and even rclone-cloud—straight to any rclone cloud, Google Drive, or even Telegram. Want to know more? Type /help and see the commands at your disposal.
"""
        await send_photo(message, image_url, caption=start_string, reply_markup=reply_markup)
    else:
        await send_message(
            message,
            "This bot can mirror from links|tgfiles|torrents|nzb|rclone-cloud to any rclone cloud, Google Drive or to telegram.\n\n⚠️ You Are not authorized user! Deploy your own mirror-leech bot",
            reply_markup,
        )


@new_task
async def ping(_, message):
    start_time = int(round(time() * 1000))
    reply = await send_message(message, "Starting Ping")
    end_time = int(round(time() * 1000))
    await edit_message(reply, f"{end_time - start_time} ms")


@new_task
async def log(_, message):
    await send_file(message, "log.txt")
