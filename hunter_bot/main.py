import os

import discord
from dotenv import load_dotenv

load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        user = self.get_user(message.author.id)
        await user.send("Нельзя")
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)

client.run(os.environ["DISCORD_TOKEN"])
