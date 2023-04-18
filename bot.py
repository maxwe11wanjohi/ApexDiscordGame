import discord
from dotenv import load_dotenv
from utils import get_game_stats

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_NAME = 'apex-games'

class ApexBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        guild = discord.utils.get(self.guilds, name=GUILD)
        channel = discord.utils.get(guild.channels, name=CHANNEL_NAME)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.channel == channel:
            # Check if message contains stats command
            if message.content.startswith('!stats'):
                # Get game stats for player
                player_name = message.content.split(' ')[1]
                stats = get_game_stats(player_name)
                await message.channel.send(stats)
