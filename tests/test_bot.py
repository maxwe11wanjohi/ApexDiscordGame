import os
import unittest
from dotenv import load_dotenv
from bot import ApexBot

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_NAME = 'apex-games'

class TestApexBot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bot = ApexBot()
        cls.bot.run(TOKEN)

    @classmethod
    def tearDownClass(cls):
        cls.bot.close()

    def test_stats_command(self):
        guild = self.bot.guilds[0]
        channel = discord.utils.get(guild.channels, name=CHANNEL_NAME)

        message = discord.Message(channel=channel, content='!stats john')
        self.bot.dispatch('message', message)

        response = self.bot.last_response

        self.assertIn('john\'s stats', response)

if __name__ == '__main__':
    unittest.main()
