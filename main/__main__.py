#!/usr/bin/env python3
'''This is the main file.
It starts the bot and other services.
'''


# Import modules and files
from discord.ext import commands, tasks
from itertools import cycle

import discord
import os

from resources import Token
import utils


# Bot class
class MyBot(commands.Bot):
    # Constructor
    def __init__(self) -> None:
        super().__init__(
            command_prefix='.', 
            intents=discord.Intents.all(),
            application_id=Token.APPLICATION_ID,
        )
    # Methods
    async def setup_hook(self):
        for filename in os.listdir("main/cogs/slash"):
            if filename.endswith(".py") and filename != "__init__.py":
                await self.load_extension(f"main.cogs.slash.{filename[:-3]}")
                await bot.tree.sync(guild=discord.Object(id=Token.GUILD_ID))
        for filename in os.listdir("main/cogs/context-menu"):
            if filename.endswith(".py") and filename != "__init__.py":
                await self.load_extension(f"main.cogs.context-menu.{filename[:-3]}")
                await bot.tree.sync(guild=discord.Object(id=Token.GUILD_ID))
        for filename in os.listdir("main/cogs/reaction"):
            if filename.endswith(".py") and filename != "__init__.py":
                await self.load_extension(f"main.cogs.reaction.{filename[:-3]}")
                await bot.tree.sync(guild=discord.Object(id=Token.GUILD_ID))
    async def on_ready(self):
        print('--------------------')
        utils.log.info('Logged in as {}'.format(self.user.name)) #type: ignore
        utils.log.info('ID: {}'.format(self.user.id)) #type: ignore
        print('--------------------')
        utils.log.info('All cogs are ready') #type: ignore
        print('--------------------')
        
        game = cycle(['Roblox', 'Fornite'])  # type: ignore
        @tasks.loop(seconds=5) 
        async def change_status():
            await self.change_presence(status=discord.Status.online, activity=discord.Streaming(name=next(game), url='https://www.twitch.tv/.'))
        change_status.start()
    # async def on_disconnect(self):
    #     utils.log.info('Disconnected')

bot = MyBot()

if __name__ == "__main__": 
    # Start the bot
    bot.run(Token.TOKEN, log_formatter=utils.formatter, log_handler=utils.stream)