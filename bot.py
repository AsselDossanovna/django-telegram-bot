from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Привет! Я твой бот.")

updater = Updater("7583479376:AAE2mLTo1wlkBZ2Z8-hshr7EAXwmcvbqdaw")
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
from myproject.models import Product  # Импорт модели
from telegram.ext import Updater, CommandHandler

def add_product(update, context):
    name = context.args[0]
    price = float(context.args[1])
    product = Product.objects.create(name=name, price=price)
    update.message.reply_text(f"Товар {product.name} добавлен!")

updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
dp = updater.dispatcher

dp.add_handler(CommandHandler("add", add_product))

updater.start_polling()
updater.idle()
