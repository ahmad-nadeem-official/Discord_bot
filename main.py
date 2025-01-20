import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online and ready!")

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    embed = discord.Embed(title="Pong! 🏓", description=f"Latency: {latency}ms", color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"{member.name}'s Info", color=discord.Color.green())
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Joined At", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.add_field(name="Created At", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def clear(ctx, amount: int = 5):
    if not ctx.author.guild_permissions.manage_messages:
        return await ctx.send("You lack the required permissions.")
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Cleared {amount} messages.", delete_after=5)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required arguments for the command.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Use `!help` for a list of commands.")
    else:
        await ctx.send("An unexpected error occurred.")
        raise error

bot.run("MTMyNjc0OTI0Mzc2MzA2ODkzOA.GUdYOx.4sIZdMbnScF2m2bMGEECQ_OISvj8OpPQCoI0zE")
