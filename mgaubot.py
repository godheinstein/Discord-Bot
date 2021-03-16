import discord
from discord.ext import commands
from typing import Optional
from discord import Embed, Member
from discord.ext.commands import Cog, Greedy
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions, bot_has_permissions
from datetime import datetime, timedelta
import random

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
		   "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command(aliases=["HELLO"])
async def hello(ctx):
    await ctx.send("Hello Dipshit")

@client.command(aliases=["FUCK"])
async def fuck(ctx):
    await ctx.send("Fuck You Too")

#clear function
@client.command(name="clear", aliases=["purge"])
@bot_has_permissions(manage_messages=True)
@has_permissions(manage_messages=True)
async def clear_messages(ctx, limit: Optional[int] = 1):
    if 0 < limit <= 100:
        with ctx.channel.typing():
            await ctx.message.delete()
            deleted = await ctx.channel.purge(limit=limit)

            await ctx.send(f"Deleted {len(deleted):,} messages.", delete_after=5)

    else:
        await ctx.send("The limit provided is not within acceptable bounds.")

#8ball function
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely',
                 'You may rely on it',
                 'As I see it, yes.',
                 'Most likely',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.',
                 'fuck you i dont want answer you.',
                 'yep cock.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#Reactions function

@Cog.listener()
async def on_reaction_add(reaction, user):
    print(f"{user.display_name} reacted with {reaction.emoji.name}")

@client.command(name="createpoll", aliases=["mkpoll"])
@has_permissions(manage_guild=True)
async def create_poll(ctx, question, *options):
    if len(options) > 10:
        await ctx.send("You can only supply a maximum of 10 options")

    else:
        embed = Embed(title="Poll",
                  description=question,
                  colour=ctx.author.colour)

        fields = [("Options", "\n".join([f"{numbers[idx]} {option}" for idx, option in enumerate(options)]), False),
              ("Instructions", "React to cast a vote!", False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        message = await ctx.send(embed=embed)

        for emoji in numbers[:len(options)]:
            await message.add_reaction(emoji)


client.run("NzQyNjkwMTM3MDk5NzMxMDU1.XzJyFw.3wtHTSgcj6IdGIfD10cVL5sDZe0")
