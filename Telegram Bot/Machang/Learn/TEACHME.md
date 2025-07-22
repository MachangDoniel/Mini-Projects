# How to create [Telegram](https://desktop.telegram.org/) Bot

1. Open Telegram
2. Search for BotFather

**Botfather Response:** BotFather is the one bot to rule them all. Use it to create new bot accounts and manage your existing bots.

About Telegram bots:
https://core.telegram.org/bots

Bot API manual:
https://core.telegram.org/bots/api

Contact @BotSupport if you have questions about the Bot API.

3. Click at Start

**Botfather Response:** I can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual (https://core.telegram.org/bots).

You can control me by sending these commands:

/newbot - create a new bot

/mybots - edit your bots

**Edit Bots**

/setname - change a bot's name

/setdescription - change bot description

/setabouttext - change bot about info

/setuserpic - change bot profile photo

/setcommands - change the list of commands

/deletebot - delete a bot

**Bot Settings**

/token - generate authorization token

/revoke - revoke bot access token

/setinline - toggle inline mode (https://core.telegram.org/bots/inline)

/setinlinegeo - toggle inline location requests (https://core.telegram.org/bots/inline#location-based-results)

/setinlinefeedback - change inline feedback (https://core.telegram.org/bots/inline#collecting-feedback) settings

/setjoingroups - can your bot be added to groups?

/setprivacy - toggle privacy mode (https://core.telegram.org/bots/features#privacy-mode) in groups

**Web Apps**

/myapps - edit your web apps (https://core.telegram.org/bots/webapps)

/newapp - create a new web app (https://core.telegram.org/bots/webapps)

/listapps - get a list of your web apps

/editapp - edit a web app

/deleteapp - delete an existing web app

**Games**

/mygames - edit your games (https://core.telegram.org/bots/games)

/newgame - create a new game (https://core.telegram.org/bots/games)

/listgames - get a list of your games

/editgame - edit a game

/deletegame - delete an existing game

4. Write command
```bash
/newbot
```
**Botfather Response:** *Alright, a new bot. How are we going to call it? Please choose a name for your bot.*

5. Write and unique name for your Telegram Bot.
in my case
```bash
Machang
```
**Botfather Response:** *Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.*
```bash
bot_machang_bot
```
**Botfather Response:** Done! Congratulations on your new bot. You will find it at t.me/bot_machang_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API: *Your API*

Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api

5. Choose /setdescription or write command
```bash
/setdescription
```
6. Select Your Bot
```bash
@bot_machang_bot
```
**Botfather Response:** *OK. Send me the new description for the bot. People will see this description when they open a chat with your bot, in a block titled 'What can this bot do?'.* 
```bash
I can respond as a bot!
```
**Botfather Response:** *Success! Description updated. /help*
```bash
/setabouttext
```
**Botfather Response:** *Choose a bot to change the about section.*

7. Select Your Bot
```bash
@bot_machang_bot
```
**Botfather Response:** *OK. Send me the new 'About' text. People will see this text on the bot's profile page and it will be sent together with a link to your bot when they share it with someone.*
```bash
I belong to Mr Machang, I am here to help!
```
**Botfather Response:** *Success! About section updated. /help*
```bash
/setuserpic
```

**Botfather Response:** *Choose a bot to change profile photo.*
```bash
@bot_machang_bot
```
**Botfather Response:** *OK. Send me the new profile photo for the bot.*

8. Drag and Drop an image as your bot's profile picture.

**Botfather Response:** *Success! Profile photo updated. /help*

9. Now we can find it searching *"bot_machang_bot"* at telegram.

10. Open terminal and write the command
```bash
pip install python-telegram-bot
pip install telegram
```
11. Create *main.py* and copy paste the following code.
```bash
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import TOKEN, BOT_USERNAME



# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am Machang Bot!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am Machang Bot! How can i help you?')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

# handle responses

def handle_response(text: str)-> str:
    text = text.lower()
    if 'hello' in text:
        return 'Hey there!'
    if 'hi' in text:
        return 'Hey there!'
    if 'how are you' in text:
        return "I'm feeling even better now that I'm talking to you. How about you? Ready to make today even brighter together?"
    if 'who are you' in text:
        return "I am Machang Bot, I serve my master Machang!"
    if 'girlfriend' in text:
        return 'Owch! I have a girlfriend, her name is Rimjhim!'
    
    return "I do not get it..."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'supergroup':
        print(BOT_USERNAME, text)
        if BOT_USERNAME in text:
            response: str = handle_response(text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



if __name__ == '__main__':
    print("Starting Bot...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    # Message
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    
    # Errors
    app.add_error_handler(error)

    # Polls the Bot
    print('Polling...')
    app.run_polling(poll_interval=3)    # after 3 second, it'll check for new message
```

for security purpose, i have not uploaded my *config.py* file that contain TOKEN and BOT_USERNAME
Include yours creating *config.py*
```bash
from typing import Final

TOKEN: Final = 'PASTE YOUR HTTP API HERE'
BOT_USERNAME: Final = '@bot_machang_bot'
```

12. Now, open Botfather at telegram again. let's set command.
```bash
/setcommands
```

**Botfather Response:** *Choose a bot to change the list of commands.*
```bash
@bot_machang_bot
```

**Botfather Response:** OK. Send me a list of commands for your bot. Please use this format:

command1 - Description

command2 - Another description

Send /empty to keep the list empty.
```bash
start-Starts the bot
help-Provide help for Machang Bot
custom-This is a custom command
```

**Botfather Response:** *Success! Command list updated. /help*

13. Now chill with your Telegram Bot and update as you want.
