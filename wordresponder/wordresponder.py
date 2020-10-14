import contextlib
import zlib

from redbot.core import commands, Config
from redbot.core.utils.mod import check_permissions
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
from typing import Literal
import discord

import aiohttp
import random

class WordResponder(commands.Cog):
    """Respond to a specified keyword with a specified response"""

    __author__ = "dsmoth"

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.config = Config.get_conf(self, 37656404831943818)
        self.config.register_global(
            keyword=None,
            response=None
        )
        @bot.event
        async def on_message(message):
            _kw = await self.config.keyword() or ''
            kw = ''.join([i for i in _kw if i.isalpha()])
            response = await self.config.response()
            if not kw or not response or message.author.bot:
                pass
            else:
                if kw in ''.join([i for i in message.content.lower() if i.isalpha()]):
                    await message.channel.send(response)
            await bot.process_commands(message)

    @commands.command()
    async def set_keyword(self, ctx, keyword):
        """Set your keyword"""
        await self.config.keyword.set(keyword)
        await ctx.send(f'Keyword set to {keyword}')

    @commands.command()
    async def set_response(self, ctx, response):
        """Set your response"""
        await self.config.response.set(response)
        await ctx.send(f'Response set to {response}')

    @commands.command()
    async def get_keyword(self, ctx):
        """Get your keyword"""
        kw = await self.config.keyword()
        await ctx.send(kw)

    @commands.command()
    async def get_response(self, ctx):
        """Get your response"""
        kw = await self.config.response()
        await ctx.send(kw)

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())
