# yuumi-bot
A bot that listens in on Discord calls to play your Yuumi support.


Part 1) Listenning in on Discord voice channels

The first part of this project is a bot that sits in discord voice and listens in on the conversation. It'll parse the speech and output text. 

Considerations: Focus on the speech to text. Don't worry about the Discord part just yet.


Part 2) Translating text logs to keybinds

After the bot successfully parses text, we will have it scrum the transcript for key words that we will set to specific keybinds. When a trigger word is detected, the bot will execute the designated keybind


Part 3) Playing the game

The bot will then need to be configured so that the keybinds correspond to real ingame actions. This should be the last phase which will consist of debugging and live testing.



