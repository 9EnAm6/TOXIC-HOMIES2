import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("ToxicHomies).")
    game = discord.Game('WithToxicHomies')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 541975332593336337:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="TOXIC")
                        embed.add_field(name="HOMIES", value=msg, inline=True)
                        embed.set_footer(text=f"DISCORD")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzM3NDUxMzA2MTk2Nzk1NDcz.Xx9jDA.lVBWEsmYSS-ek_4axXOxiJIdfHQ')
