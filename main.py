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
from keep_alive import keep_alive
from keep_alive import keep_alive

client = commands.Bot(command_prefix='.')
client.remove_command('help')

lis = [
"cant show even after open sourcing"
]

cards = [
"cant show even after open sourcing"
]

cardss = [
  #chances
"cant show even after open sourcing"
]

cardsss = [
  #completion
  " Juan",
  " Paley",
  " Ducky",
  " Loschi",
  " Lemonxle",
  " Skeppy",
  " Fluffyfox",
  " Meep",
  " Nilai",
  " Rylan",
  " Pancaker",
  " Kronos",
  " Vienna",
  " Osman",
  " CCCP",
  " Arson",
  " Pengu",
  " Xsuma",
  " Singa",
  " Kali",
  " Weon",
  " Skrov",
  " Greek_man",
  " Mark",
  " Dansk",
  " Meep",
  " Mapes",
  " Aceh",
  " Belg",
  " Whacky",
  " Galati",
  " Bruvball",
  " Mass",
  " Lesser",
  " Skipperz",
  " Swiss",
  " Serb",
  " Stalker",
  " Shukhevych",
  " Faith",
  " Miholj",
  " Castro",
  " Connor",
  " Galati",
  " Kielce",
  " Shrews",
  " Trix",
  " Spieler",
  " Smaland",
  " Lyx",
  " Kebby",
  " TRIgam",
  " Ru",
  " Joseph",
  " Jade",
  " Katzelande",
  " Hazel",
  " Ezekiel",
  " Rhine",
  " TB",
  " Minn",
  " Janpello",
  " Purtu",
  " Tringa",
  " Thailantain",
  " Nic",
  " Luff",
  " Narsof",
  " Beast",
  " Nomo",
  " Luff",
  " Helghie",
  " James",
  " Alif",
  " 1.2",
  " Mo Kush",
  " Fortress"
]

limited = [
"cant show even after open sourcing"
]

limiteds = [
"cant show even after open sourcing"
]


@client.event
async def on_ready():
  print(f'logged in')
  await client.change_presence(activity=discord.Game('MemberDex'))


@client.command(aliases=[
  "repetition", "card", "multiples", "sprint", "competetion", "list", "dupe",
  "search", "claik", "basketball", "clam"
])
async def help(ctx):
  embed = discord.Embed(color=0x1abc9c)

  embed.add_field(
    name="PLEASE HELP!!!!",
    value=
    "To claim, Just do the command .claim\n\nand to see your cards do .cards\n\nTo view images do .image and the card name (card name)\n\n.completion is self explanitory\n\n(there is a cooldown on claiming)\n\nTo claim energys just do .energy",
    inline=False)
  await ctx.send(embed=embed)


@client.command()
async def cards(ctx):

  await open_account(ctx.author)

  user = ctx.author

  users = await get_data()

  cards = users[str(user.id)]["Cards"].split()

  for i in range(0, len(cards), 25):
    embed = discord.Embed(color=0x1abc9c,
                          description='\n'.join(cards[i:i + 25]))
    await user.send(embed=embed)


@client.command()
async def duplicates(ctx, card: str):

  await open_account(ctx.author)

  user = ctx.author

  users = await get_data()

  user_cards = users[str(user.id)]["Cards"].split()

  count = user_cards.count(card)

  await ctx.send(f"You have {count} duplicates of the {card} card.")


@client.command()
async def completion(ctx):

  await open_account(ctx.author)

  user = ctx.author
  users = await get_data()
  user_cards = users[str(user.id)]["Cards"]

  embeds = []
  embed = discord.Embed(color=0x1abc9c)

  for card in cardsss:
    emoji = "✅" if card in user_cards else "❌"
    if len(embed) > 300:  # Discord's character limit for embeds is 6000
      embeds.append(embed)
      embed = discord.Embed(color=0x1abc9c)
    embed.add_field(name=f"{card} {emoji}", value="-", inline=False)

  embeds.append(embed)
  for embed in embeds:
    await user.send(embed=embed)


@client.command()
async def register(ctx):

  users = await get_data()


async def open_account(user):

  users = await get_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["Cards"] = ""

  with open("account.json", "w") as f:
    json.dump(users, f)
  return True


async def get_data():
  with open("account.json", "r") as f:
    users = json.load(f)

  return users


@client.command()
@commands.cooldown(1, 1200, commands.BucketType.user)
async def claim(ctx):

  await open_account(ctx.author)

  things = random.choice(cardss)

  users = await get_data()

  user = ctx.author

  embed = discord.Embed(color=0x1abc9c)

  embed.add_field(name="Congratulation on the claim!",
                  value=f"You have just caught\n{things}",
                  inline=False)
  await ctx.send(embed=embed)

  users[str(user.id)]["Cards"] += things

  with open("account.json", "w") as f:
    users = json.dump(users, f)


@claim.error
async def claim_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    em = discord.Embed(title=f"You silly bitch",
                       description=f"Claim in {error.retry_after:.2f}s.",
                       color=0x1abc9c)
    await ctx.send(embed=em)


@client.command(aliases=["img", "view", "see"])
async def image(ctx, image_name: str):

  path = "/home/runner/MemberDex"
  file = f"{path}/{image_name}.png"
  if os.path.isfile(file):
    await ctx.send(file=discord.File(file))
  else:
    await ctx.send(f"{image_name} not found.")


@client.command()
#@commands.cooldown(1, 900, commands.BucketType.user)
async def limited(ctx):

  await open_account(ctx.author)

  users = await get_data()

  user = ctx.author

  embed = discord.Embed(color=0x1abc9c)

  embed.add_field(
    name="No Limited's",
    value=
    f"You either missed out on a limited time claim or there hasnt been any released",
    inline=False)
  await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 1200, commands.BucketType.user)
async def energy(ctx):

  await open_account(ctx.author)

  retard = random.choice(limiteds)

  users = await get_data()

  user = ctx.author

  embed = discord.Embed(color=0x1abc9c)

  embed.add_field(name="Congratulation on the claim!",
                  value=f"You have just caught\n{retard}",
                  inline=False)
  await ctx.send(embed=embed)

  users[str(user.id)]["Cards"] += retard

  with open("account.json", "w") as f:
    users = json.dump(users, f)


@energy.error
async def energy_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    em = discord.Embed(title=f"You silly bit+ch",
                       description=f"Claim in {error.retry_after:.2f}s.",
                       color=0x1abc9c)
    await ctx.send(embed=em)


@client.command(name='add')
async def add(ctx, *nums):
  operation = " + ".join(nums)
  await ctx.send(f'{operation} = {eval(operation)}')


@client.command(name='sub')
async def sub(ctx, *nums):
  operation = " - ".join(nums)
  await ctx.send(f'{operation} = {eval(operation)}')


@client.command(name='multiply')
async def multiply(ctx, *nums):
  operation = " * ".join(nums)
  await ctx.send(f'{operation} = {eval(operation)}')


@client.command(name='divide')
async def divide(ctx, *nums):
  operation = " / ".join(nums)
  await ctx.send(f'{operation} = {eval(operation)}')


gabago = ["Tails", "Heads"]
gabagos = ["Tails", "Heads"]


@client.command(name='coin')
async def coin(ctx):
  yozama = random.choice(gabagos)
  await ctx.send(f'Coin flip decides {yozama}')


@client.command()
async def mp(ctx, number: float, percentage: int):
  result = number - (number * percentage / 100)
  await ctx.send(f"{number} - {percentage}% = {result}")


@client.command()
async def verify(ctx, card_name):
  user_data = await get_data()
  user_cards = user_data[str(ctx.author.id)]["Cards"]
  if card_name in user_cards:
    await ctx.send(f"you have the card {card_name}")
  else:
    await ctx.send(f"why does this silly ass nigga think he has {card_name}")

  if card_name == "balls":
    await ctx.send(f"kys")

  if card_name == "Balls":
    await ctx.send(f"kys")

@client.command()
async def deletecard(ctx, card: str):
    # Open the account of the user
    await open_account(ctx.author)

    # Get the account data
    users = await get_data()

    # Check if the card exists in the user's inventory
    if card not in users[str(ctx.author.id)]["Cards"]:
        await ctx.send("You dont have that card")
        return

    # Remove the card from the user's inventory
    users[str(ctx.author.id)]["Cards"] = users[str(ctx.author.id)]["Cards"].replace(card, "", 1)

    # Update the account data
    with open("account.json", "w") as f:
        json.dump(users, f)

    await ctx.send(f"{card} has been removed from your inventory")

my_secret = os.environ['TOKEN']
keep_alive()
keep_alive()
client.run(my_secret)
