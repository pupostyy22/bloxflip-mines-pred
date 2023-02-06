import discord, time
import cloudscraper, requests
import asyncio
from discord import app_commands
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hi im running")


@bot.tree.command(name="paid-mines")
@discord.app_commands.checks.has_role("Buyer")
@app_commands.describe(serverhash = "enter your serverhash", mines = "enter your amount of mines")
async def mines(interaction: discord.Interaction, serverhash: str, mines: str):
    serverhash = str(serverhash)
    serverhash_length = len(serverhash)
    if serverhash_length < 64:
        await interaction.response.send_message(":x: Please enter a vaild serverhash :x:")
    elif serverhash_length == 64:
      try:
        rfile = open("dataID.txt", "r")
      except:
        e = open("dataID.txt", "w")
        e.write("data")
        e.close()
        rfile = open("dataID.txt", "r")

      rid = rfile.read(64)
      if rid != serverhash:
        wfile = open("dataID.txt", "w")
        wfile.write(serverhash)
        wfile.close()
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:', ':💣:'
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18, 25)
        e = random.randint(22, 25)
        
        a1 = random.randint(26, 33)
        b1 = random.randint(34, 38)
        c1 = random.randint(39, 42)

        a2 = random.randint(1, 12)
        b2 = random.randint(13, 25)
        
 

        # normal mines

        if a == 1:
          mine1 = ":💎:"
        elif a == 2:
          mine2 = ":💎:"
        elif a == 3:
          mine3 = ":💎:"
        elif a == 4:
          mine4 = ":💎:"
        elif a == 5:
           mine5 = ":💎:"
        elif a == 6:
          mine6 = ":💎:"
        elif a == 7:
          mine7 = ":💎:"
        elif a == 8:
          mine8 = ":💎:"
        if b == 9:
          mine9 = ":💎:"
        elif b == 10:
          mine10 = ":💎:"
        elif b == 11:
          mine11 = ":💎:"
        elif b == 12:
          mine12 = ":💎:"
        elif b == 13:
          mine13 = ":💎:"
        if c == 14:
          mine14 = ":💎:"
        elif c == 15:
          mine15 = ":💎:"
        elif c == 16:
          mine16 = ":💎:"
        elif c == 17:
          mine17 = ":💎:"
        if d == 18:
          mine18 = ":💎:"
        elif d == 19:
          mine19 = ":💎:"
        elif d == 20:
          mine20 = ":💎:"
        elif d == 21:
          mine21 = ":💎:"
        if e == 22:
          mine22 = ":💎:"
        elif e == 23:
          mine23 = ":💎:"
        elif e == 24:
          mine24 = ":💎:"
        elif e == 25:
          mine25 = ":💎:"


                # 50% mines

        if a2 == 1:
          mine1 = ":❓:"
        elif a2 == 2:
          mine2 = ":❓:"
        elif a2 == 3:
          mine3 = ":❓:"
        elif a2 == 4:
          mine4 = ":❓:"
        elif a2 == 5:
           mine5 = ":❓:"
        elif a2 == 6:
          mine6 = ":❓:"
        elif a2 == 7:
          mine7 = ":❓:"
        elif a2 == 8:
          mine8 = ":❓:"
        elif a2 == 10:
          mine10 = ":❓:"
        elif a2 == 11:
          mine11 = ":❓:"
        elif a2 == 12:
          mine12 = ":❓:"
        elif a2 == 13:
          mine12 = ":❓:"
        elif a2 == 14:
          mine12 = ":❓:"
        if b2 == 15:
          mine1 = ":❓:"
        if b2 == 16:
          mine1 = ":❓:"
        elif b2 == 17:
          mine2 = ":❓:"
        elif b2 == 18:
          mine3 = ":❓:"
        elif b2 == 19:
          mine4 = ":❓:"
        elif b2 == 20:
           mine5 = ":❓:"
        elif b2 == 21:
          mine6 = ":❓:"
        elif b2 == 22:
          mine7 = ":❓:"
        elif b2 == 23:
          mine8 = ":❓:"
        elif b2 == 24:
          mine10 = ":❓:"
        elif b2 == 23:
          mine11 = ":❓:"
        elif b2 == 24:
          mine12 = ":❓:"
        elif b2 == 25:
          mine12 = ":❓:"


        # grey mines

        if a1 == 26:
          mine1 = ":❌:"
        elif a1 == 27:
          mine2 = ":❌:"
        elif a1 == 28:
          mine3 = ":❌:"
        elif a1 == 29:
          mine4 = ":❌:"
        elif a1 == 30:
           mine5 = ":❌:"
        elif a1 == 31:
          mine6 = ":❌:"
        elif a1 == 32:
          mine7 = ":❌:"
        elif a1 == 33:
          mine8 = ":❌:"
        if b1 == 34:
          mine9 = ":❌:"
        elif b1 == 35:
          mine10 = ":❌:"
        elif b1 == 36:
          mine11 = ":❌:"
        elif b1 == 37:
          mine12 = ":❌:"
        elif b1 == 38:
          mine13 = ":❌:"
        if c1 == 39:
          mine14 = ":❌:"
        elif c1 == 40:
          mine15 = ":❌:"
        elif c1 == 41:
          mine16 = ":❌:"
        elif c1 == 42:
          mine17 = ":❌:"



        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        
        result = f"""
        Mines
        {row1}
        {row2}
        {row3}
        {row4}
        {row5}
        """

        gamedata = f"""
        Info
        ────────────────
        Amount of Mines: {mines}
        ────────────────
        :💣: Is where a bomb could possibly be 
        ────────────────
        :❌: Is a common pattern of mines
        ────────────────
        :💎: Is showing a Predicton
        ────────────────
        :❓: Is a 50/50 prediction
        """


        dfile = open("dataRes.txt", "w")
        dfile.write(result)
        dfile.close()
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Very good predictor")
        em.add_field(name="Your Prediction", value=result)
        em.add_field(name="Info", value=gamedata)
        await interaction.response.send_message(embed=em)
      elif serverhash == rid:
        dafile = open("dataRes.txt", "r")
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Very good predictor")
        em.add_field(name="This serverhash has already been used", value=dafile.read())
        await interaction.response.send_message(embed=em)
        dafile.close()
      rfile.close()



bot.run("TOKEN")




