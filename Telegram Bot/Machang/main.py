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
    text = text.lower().strip()
    print(text)
    if 'stupid' in text:
        return 'Sorry for dissappointing you! I am still learning you know!'
    if text.startswith('say'):
        return text[3:]
    if 'i love you' in text:
        return 'i love you too sona 😘!'
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

def delete_substring(text, substring):
    return text.replace(substring, "", 1)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'supergroup':
        # text = delete_substring(text, BOT_USERNAME)
        if BOT_USERNAME in text:
            # print(BOT_USERNAME, text)
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