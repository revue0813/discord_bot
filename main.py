import settings
import discord
import random
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command(
            aliases=['p'],
            brief = "Bot responds with pong",
            description = "Simple ping command",
            help = "This command will make the bot respond with 'pong'",
            enabled=True,
            hidden=False
    )
    async def ping(ctx):
        """Answers with pong"""
        await ctx.send("pong")

    @bot.command(
            aliases=['s'],
            brief = "Single word say",
            description = "Single word say command",
            help = "Bot will respond with first word only",
            enabled=True,
            hidden=False
    )
    async def say(ctx, what = "WHAT?"):
        await ctx.send(what)
    
    @bot.command(
            aliases=['s2'],
            brief = "Multi word say",
            description = "Multiple word say command",
            help = "Bot will respond with all words",
            enabled=True,
            hidden=False
    )
    async def say2(ctx, *what):
        await ctx.send(" ".join(what))

    @bot.command(
            aliases=['s3'],
            brief = "No spaces",
            description = "Removes spaces from words",
            help = "Bot will respond with all words but removes the spaces",
            enabled=True,
            hidden=False
    )
    async def say3(ctx, what = "WHAT?", why = "WHY?"):
        await ctx.send(what + why)

    @bot.command(

    )
    async def choices(ctx, *options):
        await ctx.send(random.choice(options))

    @bot.command(

    )
    async def d20(ctx):
        await ctx.send(random.randrange(1,20,1))

    @bot.command(
            
    )
    async def dice(ctx, num : int):
        await ctx.send(random.randrange(1,num,1))

    @bot.command(
            
    )
    async def roll(ctx, numOfDice, dieSize):
        try:
            numOfDiceInt = int(str(numOfDice))
        except ValueError:
            await ctx.send("The format was incorrect, enter a number first, example: '!roll 1 d20'")

        if (dieSize[0] == 'd'):
            try:
                dieSizeInt = int(dieSize[1:])
            except ValueError:
                await ctx.send("The format was incorrect, enter a die second '!roll 1 d20'")

        await ctx.send(f"Rolling {numOfDice} {dieSize}'s")
        for i in range(numOfDiceInt):
            
            await ctx.send(f"{dieSize} #{i+1}: {random.randrange(1,dieSizeInt,1)}")

    # @bot.command(
    #     aliases=["max","mr"]
    # )
    # async def maxroll(ctx, *dice):
    #     for i in range(len(dice)):
    #         try:
    #             if(dice[i].isdigit()):
    #                 numOfDice = dice[i]
    #             elif(dice[i][0] == 'd'):
    #                 dieSize = int(dieSize[1:])
    #         except ValueError:
    #             await ctx.send(f"{dice[i]} is in the wrong format")
            



        



    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()