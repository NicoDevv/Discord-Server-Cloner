import os
import discord
from discord.ext import commands
import asyncio 
import logging
import random 
from colorama import init
from colorama import Fore, Style
import requests
import json
import datetime
import random
import threading
import random
import time
import threading

init()
os.system("cls" or "clear")

print(' ,---.                                        ,-----.,--.                             ') #per cambiare font/scritta --> https://devops.datenkollektiv.de/banner.txt/index.html
print("'   .-' ,---. ,--.--.,--.  ,--.,---. ,--.--. '  .--./|  | ,---. ,--,--, ,---. ,--.--.")
print("`.  `-.| .-. :|  .--' \  `'  /| .-. :|  .--' |  |    |  || .-. ||      \ .-. :|  .--'")
print(".-'    \   --.|  |     \    / \   --.|  |    '  '--'\|  |' '-' '|  ||  \   --.|  |   ")
print("`-----' `----'`--'      `--'   `----'`--'     `-----'`--' `---' `--''--'`----'`--'", '{}{} V1.0 {}'.format(Fore.RESET, Fore.RED, Fore.RESET)) #versione del Selfbot
print("                                   {}{}[ {}".format(Fore.RESET, Fore.RED, Fore.RESET),end="")
print("{}{}Coded BY Nico{}".format(Fore.RESET, Fore.GREEN, Fore.RESET),end="")
print("{}{} ]{}".format(Fore.RESET, Fore.RED, Fore.RESET),"\n\n")

token = input('{}\n[>] {} TOKEN: {}'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET))
prefix = input('{}\n[>] {} PREFIX: {}'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET))
client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                      self_bot=True)

client.remove_command('help')
header = {"Authorization": f'Bot {token}'}
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

intents = discord.Intents.all()
intents.members = True

@client.event
async def on_ready():
    print(' ,---.                                        ,-----.,--.                             ') #per cambiare font/scritta --> https://devops.datenkollektiv.de/banner.txt/index.html
    print("'   .-' ,---. ,--.--.,--.  ,--.,---. ,--.--. '  .--./|  | ,---. ,--,--, ,---. ,--.--.")
    print("`.  `-.| .-. :|  .--' \  `'  /| .-. :|  .--' |  |    |  || .-. ||      \ .-. :|  .--'")
    print(".-'    \   --.|  |     \    / \   --.|  |    '  '--'\|  |' '-' '|  ||  \   --.|  |   ")
    print("`-----' `----'`--'      `--'   `----'`--'     `-----'`--' `---' `--''--'`----'`--'", '{}{} V1.0 {}'.format(Fore.RESET, Fore.RED, Fore.RESET)) #versione del Selfbot
    print("                                   {}{}[ {}".format(Fore.RESET, Fore.RED, Fore.RESET),end="")
    print("{}{}Coded BY Nico{}".format(Fore.RESET, Fore.GREEN, Fore.RESET),end="")
    print("{}{} ]{}".format(Fore.RESET, Fore.RED, Fore.RESET),"\n\n")
    


    print('{}\n[>] {} Cloner running... {}'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET))
    print('{}\n[>] {} Command:{} {}copyserver\n'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET, prefix))
    print('{}\n[>] {} User info:{}\n'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET, prefix))    
    print('     - Logged in as ' + client.user.name)
    print('     - User ID: ' + str(client.user.id))
    print('     - User Token: ' + token)



@client.command()
async def copyserver(ctx):  #richiamo al comando copyserver
    
    print('{}\n[>] {} cloning enabled... {}'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET)) #inizo del processo di clonazione
    await ctx.message.delete()
    wow = await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4) 
    print('{}\n[>] {} Server created {}'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET))#creazione del server completata

    print("{}\n[>]{} I'm cloning the channels....{}".format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET)) #clonazione dei canali
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            print(ctx.guild.roles,)
    print('{}\n[>]{} Roles cloned:{}\n'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET, prefix))
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print(f"Created new role : {role.name}")
            except:
                break
    print('{}\n[>]{} Cloning completed{}\n'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET, prefix))

client.run(token, bot=False)