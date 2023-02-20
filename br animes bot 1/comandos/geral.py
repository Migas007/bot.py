import discord
from discord.ext import commands

class gerais(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:

        self.bot=bot

    
    @commands.command()
    async def olá(self, ctx):
        
        await ctx.reply('Olá, muito bom dia! Espero que esteja tudo Bom consigo!')


def setup(bot: commands.bot):
    bot.add_cog(gerais(bot))