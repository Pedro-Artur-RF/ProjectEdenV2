import discord
import re
import random
from discord.ext import commands

class AutoDado(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Check for the format x#xdx±x (e.g., 6#3d6+2 or 2d10-1)
        match = re.match(r'(\d+#)?(\d+)d(\d+)([+*/-]\d+)?$', message.content)
        if not match:
            return

        # Extract components
        repeat_part = match.group(1)
        num_dice = int(match.group(2))
        dice_type = int(match.group(3))
        modifier = match.group(4)

        # Determine repeat count
        repeat_count = int(repeat_part[:-1]) if repeat_part else 1

        # Validate dice values
        if num_dice < 1 or dice_type < 1 or repeat_count < 1:
            await message.channel.send("Error: Values must be positive")
            return

        all_results = []
        for _ in range(repeat_count):
            # Roll the dice
            rolls = [random.randint(1, dice_type) for _ in range(num_dice)]
            total = sum(rolls)

            # Apply modifier if present
            if modifier:
                op = modifier[0]
                mod_value = int(modifier[1:])

                if op == '/' and mod_value == 0:
                    await message.channel.send("Error: Division by zero")
                    return

                if op == '+':
                    total += mod_value
                elif op == '-':
                    total -= mod_value
                elif op == '*':
                    total *= mod_value
                elif op == '/':
                    total = total // mod_value  # Integer division

                total = max(total, 0)  # Prevent negative results

            all_results.append((rolls, total))

        # Build response
        if repeat_count > 1:
            response = [f"{message.content} (rolado {repeat_count} vezes!):"]
            response += [f"Resultado {i+1}: {rolls} → (**{total}**)" 
                          for i, (rolls, total) in enumerate(all_results)]
        else:
            response = [f"{message.content}: {all_results[0][0]} → (**{all_results[0][1]}**)"]

        await message.channel.send('\n'.join(response))

async def setup(bot):
    await bot.add_cog(AutoDado(bot))