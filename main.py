import discord
from discord.ext import commands

botToken = ''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guild_messages = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} logged 🔵🔵🔵')

@bot.event
async def setup_hook():
    await bot.load_extension('commands.oioi')
    await bot.load_extension('commands.lembrete')
    await bot.load_extension('commands.limpa')
    await bot.load_extension('commands.channels')
    await bot.load_extension('commands.servers')
    await bot.load_extension('commands.log')
    await bot.load_extension('events.autodado')

if __name__ == "__main__":    
    bot.run(botToken)