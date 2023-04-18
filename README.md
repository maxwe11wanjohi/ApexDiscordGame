Apex Games Discord Bot
This is a Discord bot that moderates an Apex Games channel by providing game stats for the specified player.

Features
Responds to the !stats command with game stats for the specified player.
Uses the Apex Legends Tracker API to retrieve game stats.
Moderates the Apex Games channel to ensure that all messages are appropriate.
Getting Started
To use this bot, you will need to create a Discord bot and obtain a bot token. You will also need to create an Apex Legends Tracker API key.

Prerequisites
Python 3.6 or higher
Discord bot token
Apex Legends Tracker API key
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/apex-games-discord-bot.git
Install the required dependencies:

Copy code
pip install -r requirements.txt
Create a .env file in the root directory with the following contents:

makefile
Copy code
DISCORD_TOKEN=<your-discord-bot-token>
DISCORD_GUILD=<your-discord-server-name>
APEX_TRACKER_API_KEY=<your-apex-tracker-api-key>
Modify the bot.py file to include your Apex Legends Tracker API key.

Usage
To run the bot, execute the main.py file:

css
Copy code
python main.py
The bot will connect to the Discord server and start listening for messages.

To use the bot, type the !stats command followed by a player name in the Apex Games channel. For example:

diff
Copy code
!stats john
The bot will respond with the specified player's game stats.

Testing
To run the tests, execute the test_bot.py file:

bash
Copy code
python -m unittest tests/test_bot.py
The tests will run and output the results.

Contributing
Contributions are welcome! If you have any suggestions or improvements, please create a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
