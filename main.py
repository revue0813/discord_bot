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
            aliases=["r"],
            brief = "Rolls dice",
            description = "Rolls any dice size",
            help = "Bot will roll dice if format matches: #d#.\nExample1: 2d20 will roll 2 20 sided dice.\nExample2: 1d20 2d10 will roll 1 20 sided die and 2 10 sided dice.",
            enabled=True,
            hidden=False
            )
    async def roll(ctx, *args):
        results = []

        for arg in args:
            single_results = []
            if 'd' in arg:
                try:
                    parts = arg.split('d')
                    num_of_dice = int(parts[0])
                    die_size = int(parts[1])
                    for i in range(num_of_dice):
                        roll = random.randint(1, die_size)
                        #await ctx.send(f"Roll {i} with d{die_size} is: {roll}")
                        single_results.append(roll)
                        results.append(roll)
                except ValueError:
                    await ctx.send(f"Ran into an error with the argument: {arg}")
                    return
            else:
                await ctx.send(f"Invalid argument format: {arg}")
                return
            single_result_str = ', '.join(map(str, single_results))
            await ctx.send(f"d{die_size} Rolls: {single_result_str}")
        
        result_str = ', '.join(map(str, results))
        total = sum(results)

        await ctx.send(f"Total: {total}")

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()