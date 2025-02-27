import discord, os, json
from discord.ext import commands

# Carrega as configurações do arquivo JSON
with open('./config/MainConfig.json', 'r') as f:
    config = json.load(f)

# Obtém o token do bot e o prefixo de comando a partir do arquivo de configuração
botToken = config['token']
prefix = config['prefix']

# Define as permissões necessárias para o bot
intents = discord.Intents.default()
intents.members = True  # Permite acessar eventos de membros
intents.message_content = True  # Permite acessar o conteúdo das mensagens
intents.guild_messages = True  # Permite acessar mensagens do servidor
intents.messages = True  # Permite acessar mensagens em geral

# Cria o bot com o prefixo de comando e as permissões definidas
bot = commands.Bot(command_prefix=prefix, intents=intents)

# Evento acionado quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f'{bot.user} logged 🔵🔵🔵')

# Evento de configuração do bot, carregando as extensões (comandos e eventos)
@bot.event
async def setup_hook():
    await bot.load_extension('commands.oioi')
    await bot.load_extension('commands.lembrete')
    await bot.load_extension('commands.limpa')
    await bot.load_extension('commands.channels')
    await bot.load_extension('commands.servers')
    await bot.load_extension('commands.log')
    await bot.load_extension('commands.init')
    await bot.load_extension('events.autodado')

# Inicia o bot com o token carregado do arquivo de configuração
if __name__ == "__main__":    
    bot.run(botToken)
