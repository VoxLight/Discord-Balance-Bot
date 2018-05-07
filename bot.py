from discord.ext import commands
from operator import itemgetter
from config import get_config

# import the settings
settings = get_config('settings.ini')
login = settings["LOGIN"]
bot_info = settings["BOT INFO"]

# create the bot
bot = commands.Bot(command_prefix=bot_info['prefix'], 
            description=bot_info['description'],
            pm_help=None)

    
@bot.event   
async def on_ready():
    print(f"{bot.user.name}[{bot.user.id}] Connected Succesfully")
    try:
        bot.load_extension('team_sorter')
    except Exception as e:
        print(e)
        
bot.run(login["token"])