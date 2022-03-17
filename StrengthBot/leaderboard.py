import discord
from userflow import bot

weightClassMen = ['59 kg', '66 kg', '74 kg', '83 kg', '93 kg', '105 kg', '120 kg', '120 kg+']
weightClassesWomen = ['47 kg', '52 kg', '57 kg', '63 kg', '69 kg', '76 kg', '84 kg', '84 kg+']
ARRAY_LEN = 8


@bot.command(name='leaderboard', help='Presents all leaderboards with all weight classes')
async def leaderboard(ctx):
    await leaderboard_men(ctx)
    await leaderboard_women(ctx)


@bot.command(name='leaderboard-men', help='Presents Men\'s leaderboard')
async def leaderboard_men(ctx):
    men_board = discord.Embed(title="Men's Leaderboard",
                              color=0xFFBD33, timestamp=ctx.message.created_at)
    for i in range(ARRAY_LEN):
        men_board.add_field(name=f'{weightClassMen[i]}', value='placeholder', inline=False)

    await ctx.send(embed=men_board)


@bot.command(name='leaderboard-women', help='Presents Women\'s leaderboard')
async def leaderboard_women(ctx):
    women_board = discord.Embed(title="Women's Leaderboard",
                                color=0xFFBD33, timestamp=ctx.message.created_at)

    for i in range(ARRAY_LEN):
        women_board.add_field(name=f'{weightClassesWomen[i]}', value='placeholder', inline=False)

    await ctx.send(embed=women_board)
