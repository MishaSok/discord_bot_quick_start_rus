import discord  # Импортируем библиотеку discord.py

from discord.ext import commands  # Из библиотеки Discord.py импортируем комманды
from config import settings  # Из файлика config (если он у вас есть) импортируем словарь settings

bot = commands.Bot(command_prefix=settings['prefix'])  # Создаем "тело" бота


@bot.event
async def on_ready():  # Event on_ready активируется когда бот готов к использованию
    print('Bot connected successfully!')


@bot.command()
async def hello(ctx):  # Создаем комманду hello
    author = ctx.message.author  # Создаем переменную author в которую занесем имя и тэг пользователя.
    await ctx.send(f'Hello, {author.mention}!')  # Используем метод .mention, который "тэгает" пользователя


bot.run(settings['token'])  # Запускаем бота с помощью нашей библиотеки из файла config (опять же если он у вас есть)

# v1.0
