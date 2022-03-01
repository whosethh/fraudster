import discord
from discord.ext import commands
from colored import fg
from colorama import init, deinit
import aiosqlite
import random
import fade
import os, datetime
from rich.console import Console

bot = commands.Bot(command_prefix="$", help_command=None, status=discord.Status.dnd, activity=discord.Streaming(name="Prefix $", url="https://www.twitch.tv/elraenn"))

c = Console(
        color_system="auto", 
        legacy_windows=True,
      # soft_wrap=True
    )
lemon = 0xfaf273

def get_time():
        return datetime.datetime.now().strftime("[%H:%M:%S | %m/%d/%y]")
    
def clear():
        os.system("cls") if os.name == "nt" else os.system("clear")

#async with a'aiosqlite.connect("./credentials.db") as db:

def splashy():
    clear()
    init(strip=True, convert=True, autoreset=True)
    colors = [fade.purpleblue, fade.pinkred, fade.purplepink, fade.greenblue, fade.fire, fade.water]
    color =  [fade.greenblue]
    splash = random.choice(color)("""
                ███████╗██████╗  █████╗ ██╗   ██╗██████╗
                ██╔════╝██╔══██╗██╔══██╗██║   ██║██╔══██╗
                █████╗  ██████╔╝███████║██║   ██║██║  ██║
                ██╔══╝  ██╔══██╗██╔══██║██║   ██║██║  ██║
                ██║     ██║  ██║██║  ██║╚██████╔╝██████╔╝
                ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
                v2.0 (rewritten)
                made by hate#1337 | with love ♡
                Developer Screen
    """)
    clr = fg("#fffff")
    clr2 = fg("#66ffc2")
    clr3 = fg("#ffff80")
    c.print(splash, justify="center")
    deinit()
    #c.print(clr + "[" clr2 + f"{get_time()}" + clr "]" + clr3 + "The client is ready")
    print(f"{clr}{clr2}{get_time()}{clr} {clr3} The client is ready.")

@commands.is_owner()
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def deluser(ctx, username):
    database = await aiosqlite.connect("./credentials.db")
    cursor = await database.cursor()
    await cursor.execute('''
    DELETE FROM "users" WHERE username=?;
    ''', (username,))
    await database.commit()
    await database.close()
    embed = discord.Embed(color=lemon)
    embed.add_field(name="User deleted!", value=f"Deleted User: `{username}`")
    await ctx.send(embed=embed)

@commands.is_owner()
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def adduser(ctx, username, password):
    database = await aiosqlite.connect("./credentials.db")
    cursor = await database.cursor()
    await cursor.execute('''
    INSERT INTO "users" VALUES  (?, ?);
    ''', (username, password,))
    await database.commit()
    await database.close()
    embed = discord.Embed(color=lemon)
    embed.add_field(name="User added!", value=f"Username: `{username}` \n Password: `{password}`")
    await ctx.send(embed=embed)

@commands.is_owner()
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def delete(ctx):
    database = await aiosqlite.connect("./credentials.db")
    cursor = await database.cursor()
    await cursor.execute("DROP TABLE users")
    await database.commit()
    await database.close()
    embed = discord.Embed(color=lemon)
    embed.add_field(name="Succesfully Deleted The Table.", value="Code `501`")
    await ctx.send(embed=embed)

@commands.is_owner()
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def create(ctx): #member: discord.Member):
    database = await aiosqlite.connect("./credentials.db")
    cursor = await database.cursor()
    await cursor.execute('''
    CREATE TABLE IF NOT EXISTS "users"(
        "username" TEXT,
        "password" TEXT
    )
        ''')
    await database.commit()
    await database.close()
    embed = discord.Embed(color=lemon)
    embed.add_field(name="Succesfully Created Table.", value="Code `501`")
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    splashy()


bot.run('OTQ3NTkxMzEwOTAxMTM3NDQ4.YhvfLQ.SW6PtXKrQNRWcffEfzPX2eGqv3s')