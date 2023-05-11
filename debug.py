import random
import math
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import discord.utils
import requests
import json
import time
import os

os.chdir("")

client = commands.Bot(command_prefix='.')
client.remove_command('help')


@client.event
async def on_ready():
  print(f'logged in')
  await client.change_presence(activity=discord.Game('MemberDex'))



@client.command()
@commands.has_permissions(administrator=True) # only admins can use this command
async def d(ctx, user: discord.User, card_name: str):
    # Open the user's account
    await open_account(user)

    # Get the account data
    users = await get_data()

    # Check if the user has the card
    if card_name not in users[str(user.id)]["Cards"]:
        await ctx.send(f"{user.name} does not have the {card_name} card")
        return

    # Remove the card from the user's inventory
    users[str(user.id)]["Cards"] = users[str(user.id)]["Cards"].replace(card_name, "", 1)

    # Save the updated data to the file
    with open("account.json", "w") as f:
        json.dump(users, f)

    await ctx.send(f"{card_name} has been removed from {user.name}'s inventory")


@client.command()
@commands.has_permissions(administrator=True)
async def add(ctx, target: discord.User, card: str):
    # Open the account of the target user
    await open_account(target)

    # get the account data
    users = await get_data()

    # add the card to the user's inventory
    users[str(target.id)]["Cards"] += card

    # Save the updated data to the account file
    with open("account.json", "w") as f:
        json.dump(users, f)

    # Send a confirmation message
    await ctx.send(f"added {card} to {target.name}'s inventory")
    
    client.run(ragh)
