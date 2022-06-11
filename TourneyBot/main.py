from discord.ext import commands
import os
import discord
import random
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

bot.videos = ['https://www.youtube.com/watch?v=XmoKM4RunZQ', 'https://www.youtube.com/watch?v=qTmjKpl2Jk0', 'https://www.youtube.com/watch?v=hY7m5jjJ9mM']

bot.playerlist = []
# help function
@bot.group(invoke_without_command = True)
async def help(ctx):
  em = discord.Embed(title = "Help", description = "Use !help for extended info", color = ctx.author.color)

  em.add_field(name = "**Bracket**", value = "`eight`: creates a bracket with 8 players" + "\n" + "`sixteen`: creates a bracket with 16 players")
  em.add_field(name = "**Players**", value = "`addP`: adds a player" + "\n" + "`showP`: shows the players that are participating")

  await ctx.send(embed = em)

#commands to create the bracket
@bot.command()
async def eight(ctx):
  if len(bot.playerlist) != 8:
    await ctx.send("There are not 8 people entered!")
  else:
    bot.randomlist = random.sample(bot.playerlist, 8)
    await ctx.send(bot.randomlist[0] + " **VS** " + bot.randomlist[1] + '\n' +'\n' + bot.randomlist[2] + " **VS** " + bot.randomlist[3] + '\n' +'\n' + bot.randomlist[4] + " **VS** " + bot.randomlist[5] + '\n' +'\n' + bot.randomlist[6] + " **VS** " + bot.randomlist[7])
  
@bot.command()
async def sixteen(ctx):
  if len(bot.playerlist) != 16:
    await ctx.send("There are not 16 people entered!")
  else:
    bot.randomlist = random.sample(bot.playerlist, 16)
   
    await ctx.send(bot.randomlist[0] + " **VS** " +  bot.randomlist[1] + '\n' + '\n' + bot.randomlist[2] + " **VS** " + bot.randomlist[3] + '\n' + '\n' + bot.randomlist[4] + " **VS** " + bot.randomlist[5] + '\n' + bot.randomlist[6] + " **VS** " + bot.randomlist[7] + '\n' + '\n' + bot.randomlist[8] + " **VS** " + bot.randomlist[9] + '\n' +'\n' + bot.randomlist[10] + " **VS** " + bot.randomlist[11] + '\n' +'\n' + bot.randomlist[12] + " **VS** " + bot.randomlist[13] + '\n' +'\n' + bot.randomlist[14] + " **VS** " + bot.randomlist[15])


# finished bottom to add and show who is entered
@bot.command()
async def addP(ctx, *, item):
  await ctx.send("Added " + item + "!")
  bot.playerlist.append(item)
  print(bot.playerlist)

@bot.command()
async def showP(ctx):
  for i in bot.playerlist:
    await ctx.send(i)

keep_alive()

password = os.environ['password']
bot.run(password)