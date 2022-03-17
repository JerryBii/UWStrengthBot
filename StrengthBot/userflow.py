import discord
from discord.ext import commands

from modules.bot import bot


@bot.command(name='list', help='Presents all members')
@commands.has_role('Mod')
async def members(ctx):
    # TODO: Reformat this
    club_members = discord.Embed(title="All Members",
                                 color=0xFFBD33)
    for guild in bot.guilds:
        for member in guild.members:
            club_members.add_field(name="Name", value=member.display_name + "\n", inline=True)
            club_members.add_field(name="Squat", value="0lbs" + "\n", inline=True)
            club_members.add_field(name="Bench", value="0lbs" + "\n", inline=True)
            club_members.add_field(name="Deadlift", value="0lbs" + "\n", inline=True)
            club_members.add_field(name="Total", value="0lbs" + "\n", inline=True)
    await ctx.send(embed=club_members)
