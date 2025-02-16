import discord
import re
import random
from discord.ext import commands

class AutoDado(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # Define o evento (on message), o código sera executado em toda mensagem.
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        # Checa se a mensagem está no formato da mensagem (xdx+x)
        # A FAZER: Mudar o formato para x#xdx+x
        match = re.match(r'(d#)?(\d+)d(\d+)([+*/-][+-]?\d+)?$', message.content)
        if match:
            # Separa as rolagens em grupos
            has_Hash = bool(match.group(1))
            num_dice = int(match.group(2))
            dice_type = int(match.group(3))
            modifier = match.group(4)
            # gerendo os valores de cada rolagem
            original_rolls = [random.randint(1, dice_type) for _ in range(num_dice)]
            modified_rolls = []
            total = 0
            # Se não houver hash no código, calcula os modificadores para cada rolagem individual
            if (has_Hash == True):
                # Se houver modificador realiza as alterações em cada rolagem individual
                if modifier:
                    op = modifier[0]
                    modifier_value = int(modifier[1:])

                    if op == '/' and modifier_value == 0:
                        await message.channel.send("Error: Division by zero")
                        return

                    for roll in original_rolls:
                        if op == '+':
                            modified = roll + modifier_value
                        elif op == '-':
                            modified = roll - modifier_value
                        elif op == '*':
                            modified = roll * modifier_value
                        elif op == '/':
                            modified = roll // modifier_value
                        modified_rolls.append(modified)
                        total += modified
                else:
                    modified_rolls = original_rolls.copy()
                    total = sum(original_rolls)
                # Gera uma string com todos as rolagens originais e modificadas
                results = [f"{message.content.replace("#", "")}: {orig}→(**{mod}**)" for orig, mod in zip(original_rolls, modified_rolls)]
                results_str = '\n'.join(results)
                await message.channel.send(f"{results_str}")
            # Se houver hash no código, realiza a soma dos valores originais e somente depois realiza os calculos com os modificadores
            elif (has_Hash == False):
                total = sum(original_rolls)
                if modifier:
                    op = modifier[0]
                    modifier_value = int(modifier[1:])

                    if op == '/' and modifier_value == 0:
                        await message.channel.send("Error: Division by zero")
                        return
                     
                    if op == '+':
                       modified = total + modifier_value
                    elif op == '-':
                        modified = total - modifier_value
                    elif op == '*':
                        modified = total * modifier_value
                    elif op == '/':
                        modified = total // modifier_value
                    await message.channel.send(f"{message.content}:{original_rolls} → (**{modified}**)")
                else:
                    await message.channel.send(f"{message.content}:{original_rolls} → (**{total}**)")

                        

async def setup(bot):
    await bot.add_cog(AutoDado(bot))