# discord_bot_quick_start_rus
 **Гайд для GitHub по написанию бота c помощью discord.py**
 
Если есть какие-то вопросы или пожелания писать сюда ==> MishaSok#6723

Дата написания данного гайда 05.02.2021
Библиотека discord.py может обновляться, поэтому после 
крупных патчей разработка бота может отличаться. В любом случае ближайшие несколько месяцев данный гайд будет актуален.

**Что нам потребуется?**:
* Стабильное интернет соединение
* Неплохие знания Питона
* Умение "гуглить" и находить нужную информацию
* Среда для написания кода

Я советую для разработки бота создать отдельный сервер в Дискорде, где мы будем
проверять нашего бота, потому что почти ни у кого не получается запустить сложный код с первого раза, 
а спамить другим не очень хочется.

**Создание Application'a:**

Для начала нам нужно создать Discord Application, для этого мы должны перейти по этой ссылке: https://discord.com/developers/applications. После 
успешного входа в ваш аккаунт Discord, вам нужно нажать на кнопку **New Application**
и выбрать имя для приложения. ВАЖНО: ИМЯ ДЛЯ САМОГО БОТА ДИСКОРДА МЫ БДЕМ НАСТРАИВАТЬ ПОЗЖЕ.

После создания Application'а мы должны перейти во вкладку **Bot**, а затем нажать на кнопку **Add Bot**.

Если у вас появилось зеленая надпись по типу: **A wild bot has appeared!**, значит вы всё сделали правильно и бот у вас уже создан.

**Подключаем нашего бота к серверу:**

Для того чтобы подключить бота к вашему серверу Дискорд, нужно следовать простым инструкциям:
1. Нужно получить Client_ID вашего бота. Для этого мы переходим во вкладку General Information и копируем
его нажав на кнопку **Copy**.
   
2. Копируем эту ссылку ==> https://discordapp.com/oauth2/authorize?&client_id=(тут)&scope=bot&permissions=8
. В эту ссылку вместо слова "тут" вставляем наш Client_ID. Скобки естественно убираем. Доп. информация: В нашей
   ссылке bot&permissions=8 означает что наш permissions integer равен 8. Проще говоря, это число отвечает за то, 
   какие права будут выданы боту при подключении. Этот код можно узнать во вкладке Bot (в которой мы создавали бота). Пролистав вниз,
   вы сможете сами выбрать нужные вам права, но я советую оставить 8, так как если вы будете сами выбирать права, могут произойти казусные ситуации
   при работе с ботом.
   
3. После создания нашей ссылки мы переходим по ней, выбираем сервер на который хотите пригласить бота и нажимаем кнопку **Авторизовать**.
После прохождения капчи наш бот успешно присоединится к серверу, но будет оффлайн. Не пугайтесь, это нормально, ведь наш бот еще не запущен.
   
**Создание проекта:**

Ну вот мы и готовы начать писать код для нашего прекрасного бота. Если вы знаете Python на ОЧЕНЬ низком уровне, я советую воздержаться от создания ботов и заняться чем нибудь более простым.

Для начала я советую создать пустую папку где мы будем хранить все файлы для нашего бота.

Затем если у вас не установлена библиотека discord.py, вам нужно её устновить. Для этого переходим в командную строку и пишем: 
_pip install discord.py_  
Внимание, для установки библиотек требуется pip, если он у вас не установлен, то гугл в помощь ^_^

После успешной установки библиотеки, переходим в вашу любимую среду разработки, в моём случае это PyCharm. 
Затем создаем новый файл Python файл с названием "bot" (такое название не даст вам запутаться) и расширением .py и сразу сохраняем его в нашей папке с проектом.

**Первые строчки кода:**
Начинаем писать скрипт для нашего бота. 

Для начала подключаем (импортируем) наши библиотеки:

```python
import discord
from discord.ext import commands
```

(можем запустить наш скрипт для проверки работоспособности библиотеки)

Создаем еще один файлик .py  названием config, для хранения в нём опасных данных.
Почему мы не можем просто создать переменные с этими данными? Всё очень просто. Это самый простой способ защитить себя от злоумышленников. Если кто-то каким-то образом получит ваш код, то не сможет управлять вашим ботом. Все наши токены будут хранится в отдельном файлике.

В файле config.py создаем словарь, к которому мы будем обращаться при работе в ботом:
```python
settings = {
    'token': 'Введите ваш токен',
    'bot': 'Название вашего бота',
    'id': 'id вашего бота (без кавычек)',
    'prefix': 'префикс'
}
```

Сохраняем файл config.py и возвращаемся обратно к файлу bot.py

Импортируем наш файлик config.py:

```python
from config import settings
```

**Написание "тела" для бота и первый запуск:**

Я буду стараться объяснять подробно каждый шаг и каждую строчку, потому что на первый взгляд это может показаться сложным, хотя таковым не является.

```python
bot = commands.Bot(command_prefix=settings['prefix'])
```

* Переменная bot - это "тело" нашего бота. Ему мы присваиваем значение commands.Bot с определёнными аргументами.
* command_prefix=settings['prefix'] - это аргумент, в который мы вписываем значение нашего профекса. settings['prefix'] означает, кто мы обращаемся к словарю settings (который мы импортировали из файла config.py) и обращаемся к ключу prefix, в котором вписано
нужное нам значение.
  
Затем мы можем проверить, запускается наш бот или нет. В библиотеке discord.py есть огромное количество разных ивентов (Event).
Одним из них мы сейчас воспользуемся:

```python
@bot.event
async def on_ready():
    print('Bot connected successfully!')
```
* @bot.event - говорит нам о том, что ниже будет прописана функция, являющаяся ивентом. 
* async def on_ready(): - Асинхронная функция (Очень важно все функции создавать асинхронными, так как бот должен выполнять несколько функций в одно время). Ей присваивается 
значение on_ready, данная функция срабатывает когда бот полностью подключен и готов к работе. Аргументов у этой функции нет.
  
* Ну и последняя строка просто выводит в консоль сообщение, по которому мы можем понять работает наш бот или нет.

**Создание первой команды:** 

Настало время создать первую команду для нашего бота:
```python
@bot.command()
async def hello(ctx):  
    author = ctx.message.author  
    await ctx.send(f'Hello, {author.mention}!')
```
В отличии от нашей прошлой функции on_ready, эта будет начинаться с @bot.command(), потому что это не ивент, а уже полноценная команда, хоть и простая.
Вызов функции происходит точно так же как и с ивентами, но в этот раз мы передаем значение ctx. 
Затем мы создаем перменную author, в которую передаем значение аккаунта пользователя (@name#0000), который вызвал функцию.
Затем с помощью await ctx.send выводим наше сообщение в чат. В скобках у нас написано author.mention, 
метод mention позволяет "тэгать" пользователя, который написал команду.

**Можем запускать нашего бота и проверять команду!**

На этом я закончу свой краткий гайд по созданию бота для дискорда. Дальше только чтение документации, которую
вы можете найти по ссылке: https://discordpy.readthedocs.io/en/latest/index.html#getting-started

_P.S Возможно, я когда нибудь дополню этот гайд дополнительными интересными командами и ивентами_. 