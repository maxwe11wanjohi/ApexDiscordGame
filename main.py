import os
from dotenv import load_dotenv
from bot import ApexBot

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = ApexBot()
bot.run(TOKEN)
