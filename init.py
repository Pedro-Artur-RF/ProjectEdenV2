import discord
from discord.ext import commands
import asyncio

iniciativa = []
turno_atual = 0

class Iniciativa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def init(self, ctx):
        """Comando para iniciar o rastreador de iniciativa."""
        global iniciativa, turno_atual
        iniciativa = []  # Reseta a lista de iniciativa
        turno_atual = 0  # Reseta o turno atual

        embed = discord.Embed(title="Rastreador de Iniciativa", description="Use `!join <valor> <nome>` para entrar na iniciativa.")
        embed.set_footer(text="Aguarde a entrada dos jogadores.")
        
        # Envia o embed inicial
        mensagem = await ctx.send(embed=embed)

        # Adiciona a reação para passar o turno
        await mensagem.add_reaction("➡️")

        # Espera por reações
        def check(reaction, user):
            return user != self.bot.user and str(reaction.emoji) == "➡️" and reaction.message.id == mensagem.id

        while True:
            try:
                # Espera pela reação
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                # Passa para o próximo jogador
                turno_atual = (turno_atual + 1) % len(iniciativa)
                await self.atualizar_embed(mensagem, embed)
            except asyncio.TimeoutError:
                await ctx.send("Tempo esgotado! O rastreador de iniciativa foi encerrado.")
                break

    @commands.command()
    async def join(self, ctx, valor: int, *, nome: str):
        """Comando para adicionar um jogador à iniciativa."""
        global iniciativa
        iniciativa.append((valor, nome))
        iniciativa.sort(reverse=True, key=lambda x: x[0])  # Ordena pela iniciativa

        await ctx.send(f"{nome} entrou na iniciativa com valor {valor}!")

    async def atualizar_embed(self, mensagem, embed):
        """Atualiza o embed com o jogador atual."""
        global iniciativa, turno_atual
        embed.description = "Iniciativa:\n"
        for i, (valor, nome) in enumerate(iniciativa):
            if i == turno_atual:
                embed.description += f"**{nome}** (Iniciativa: {valor})\n"  # Destaca o jogador atual
            else:
                embed.description += f"{nome} (Iniciativa: {valor})\n"
        
        await mensagem.edit(embed=embed)

async def setup(bot):
    await bot.add_cog(Iniciativa(bot))