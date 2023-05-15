from cgitb import handler
from contextvars import Context
from email.mime import application
import logging
from telegram import Update, PersonalDetails
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import core, files, config



logging.basicConfig(
    filename='logs.txt',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Привет, роллеры!'
        )

async def suggest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_fullname = update.message.from_user.full_name
    user_id = update.message.from_user.id
    text = update.message.text
    await update.message.reply_text(files.add_sugg(user_fullname, user_id, text))

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_fullname = update.message.from_user.full_name
    user_name = update.message.from_user.username
    user_id = update.message.from_user.id
    files.grab(user_fullname, user_name, user_id, 'roll')
    await update.message.reply_text(core.compose_dbl(user_id, user_fullname))

async def askhole(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_fullname = update.message.from_user.full_name
    user_name = update.message.from_user.username
    user_id = update.message.from_user.id
    files.grab(user_fullname, user_name, user_id, 'askhole')
    await update.message.reply_text(core.askhole_compose(user_id, user_fullname))
        

async def xkcd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    img = core.xkcd_comp()[0]
    text = core.xkcd_comp()[1]
    await update.message.reply_photo(photo = img, caption = text)

async def cat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    img = core.cat_f()[0]
    text = core.cat_f()[1]
    await update.message.reply_photo(photo = img, caption = text)

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(core.send_support())

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.tgToken).build()

    start.handler = CommandHandler('start', start)
    application.add_handler(start.handler)

    roll.handler = CommandHandler('roll', roll)
    application.add_handler(roll.handler)

    askhole.handler = CommandHandler('askhole', askhole)
    application.add_handler(askhole.handler)

    xkcd.handler = CommandHandler('xkcd', xkcd)
    application.add_handler(xkcd.handler)

    cat.handler = CommandHandler('cat', cat)
    application.add_handler(cat.handler)

    support.handler = CommandHandler('support', support)
    application.add_handler(support.handler)

    suggest.handler = CommandHandler('suggest', suggest)
    application.add_handler(suggest.handler)

    application.run_polling()