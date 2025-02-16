import os, hashlib, json, discord
from discord.ext import commands

# Load the JSON file with stored hashes
with open('json/passwords.json', 'r') as f:
    stored_hashes = json.load(f)

async def authenticate_password(ctx):
    # Send a direct message to the user asking for a password
    await ctx.author.send("Insira sua senha para autenticação")

    # Wait for the user to respond with a password
    def check(message):
        return message.author == ctx.author and message.channel.type == discord.ChannelType.private

    password_message = await commands.Bot.wait_for('message', check=check)

    # Hash the password using SHA-2
    password_hash = hashlib.sha256(password_message.content.encode()).hexdigest()

    # Check if the password hash is in the stored hashes
    if password_hash in stored_hashes.values():
        await ctx.author.send("Senha correta, o log sera gerado!")
        return True
    else:
        await ctx.author.send("Invalid password. Authentication failed.")
        return False

@commands.command()
async def log(ctx, destination_guild_id: int, channel_id: int, limit: str):
    # Check if the user has authenticated
    if not await authenticate_password(ctx):
        return

    destination_guild = commands.bot.get_guild(destination_guild_id)
    if not destination_guild:
        await ctx.send(f"O ID DE SERVIDOR: '{destination_guild_id}' \n não foi encontrado.")
        return

    source_channel = discord.utils.get(destination_guild.text_channels, id=channel_id)
    if not source_channel:
        await ctx.send(f"O ID DE CANAL: '{channel_id}' \n não foi encontrado")
        return

    # Copy messages
    if limit == "all":
        file_path = f"{channel_id}_LOG.txt"
        with open(file_path, 'w') as file:
            async for message in source_channel.history(limit=None):
                file.write(f"Message from {message.author}: {message.content}\n")
        with open(file_path, 'rb') as file:
            await ctx.author.send(file=discord.File(file, f'{channel_id}_LOG.txt')) 
        os.remove(f'{channel_id}_LOG.txt')         
    else:
        file_path = f"{channel_id}_LOG.txt"
        with open(file_path, 'w') as file:
            async for message in source_channel.history(limit=int(limit)):
                file.write(f"Message from {message.author}: {message.content}\n")
        with open(file_path, 'rb') as file:
            await ctx.author.send(file=discord.File(file, f'{channel_id}_LOG.txt')) 
        os.remove(f'{channel_id}_LOG.txt')

async def setup(bot):
    bot.add_command(log)