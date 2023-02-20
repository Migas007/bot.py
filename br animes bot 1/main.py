import asyncio
import discord
from discord import Embed, Color
from discord.ext import commands, tasks
import openai
import random
import os

# Cria uma instância do bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
statuses = ["Moderando o Servidor!", "Melhor servidor de Animes!", "Geek's Paradise", "Gosta de Pizza?"]


@tasks.loop(seconds=10)
async def change_status():
    # Seleciona um status aleatório da lista de status definida acima
    new_status = discord.Activity(type=discord.ActivityType.listening, name=statuses[random.randint(0, len(statuses)-1)])
    await bot.change_presence(activity=new_status)


for filename in os.listdir('./comandos'):
    if filename.endswith('.py') and not filename.startswith('__'):
        bot.load_extension(f'comandos.{filename[:-3]}')


@bot.event
async def on_ready():
    print(f'{bot.user.name} Se conectou ao discord!')
    change_status.start()


TOKEN = "token"
bot.run(TOKEN)


