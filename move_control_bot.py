import logging

from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)


logger = logging.getLogger(__name__)


async def start(update, context):
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'w') as file:
        file.write('')
    await update.message.reply_text(f'Датчик посещений включён', reply_markup=markup)


async def vova(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Вова был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def timur(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Тимур был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def semen(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Семён был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def sasha(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Саша был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def vanya(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Ваня был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def pasha(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Паша был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def dima(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Дима был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def nastya(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Настя была замечена датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def milana(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Милана была замечена датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def tanya(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Таня была замечена датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def denis_golubev(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Денис Голубев был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def denis_belokopytov(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Денис Белокопытов был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def roma(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Рома был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


async def yura(update, context):
    date = datetime.datetime.today()
    reply_keyboard = [['/Vova', '/Don_Maksokovsky'],
                      ['/Semen', '/Sasha'],
                      ['/Roma', '/Pasha'],
                      ['/Dima', '/Vanya'],
                      ['/Nastya', '/Milana'],
                      ['/Tanya', '/Denis_Golubev'],
                      ['/Denis_Belokopytov', '/Don_Maksokovsky_Jr']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    with open('move_control_file.txt', 'a') as file:
        file.write(f'Юра был замечен датчиком в {date.strftime("%H:%M:%S")}\n')
    await update.message.reply_text(f'Вас заметил датчик', reply_markup=markup)


def main():
    TOKEN = '6534986931:AAGmhCLEYiKXzQreGs3jWYCFY5iiCCPf0ks'
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('Vova', vova))
    application.add_handler(CommandHandler('Don_Maksokovsky', timur))
    application.add_handler(CommandHandler('Semen', semen))
    application.add_handler(CommandHandler('Sasha', sasha))
    application.add_handler(CommandHandler('Roma', roma))
    application.add_handler(CommandHandler('Vanya', vanya))
    application.add_handler(CommandHandler('Pasha', pasha))
    application.add_handler(CommandHandler('Dima', dima))
    application.add_handler(CommandHandler('Nastya', nastya))
    application.add_handler(CommandHandler('Milana', milana))
    application.add_handler(CommandHandler('Tanya', tanya))
    application.add_handler(CommandHandler('Don_Maksokovsky_Jr', yura))
    application.add_handler(CommandHandler('Denis_Golubev', denis_golubev))
    application.add_handler(CommandHandler('Denis_Belokopytov', denis_belokopytov))
    application.run_polling()


if __name__ == '__main__':
    main()
