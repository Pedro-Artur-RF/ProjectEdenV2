import discord, json, os
from discord.ext import commands

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # Define o evento (on message), o código sera executado em toda mensagem.
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
    