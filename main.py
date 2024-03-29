import os
from discord.ext import commands
from alive import alive
import side

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    bas_channel = bot.get_channel(860861726898782232)
    await bas_channel.send('I am ready')


@bot.event
async def on_member_join(member):
    print(f'{member} has joined server')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!DM'):
        await message.channel.send('Hello')

    if message.content.startswith(f'kop edaa'):
        await message.channel.send(f'Enna pattiyeda')

    if message.content.startswith(f'#intro'):  #role assigned with a command
        user = message.author
        role = bot.discord.utils.get(user.guild.roles, name="TEST ROLE")
        await user.add_roles(role)
        await message.add_reaction('\U00002705')
        mesg = f'Dear {user.mention} you have been assigned with <@&937732766123061321>'
        await message.channel.send(mesg, delete_after=15.0)
        reaction_channel = bot.get_channel(937743808173592686)
        await reaction_channel.send(f'{user.mention} used intro command')
    else:
        print('else condition used')

    if message.content.startswith('#remove'):  #role removed with a command
        user = message.author
        role = bot.discord.utils.get(user.guild.roles, name="TEST ROLE")
        await user.remove_roles(role)
        await message.add_reaction('\U00002611')
    else:
        print('remove else condition activated')

    if message.content.startswith('rose'):
        await message.channel.send(
            'https://user-images.githubusercontent.com/81223681/147108054-4321e894-d906-40ca-b110-b36bbcb998f9.jpg'
        )
        await message.add_reaction('\U00002611')
        await message.channel.send('Completed')
    else:
        print('rose used')
    if message.content.startswith('#organizer'):
        await message.channel.send(
            'https://user-images.githubusercontent.com/81223681/170876578-e7d276ce-1ccb-41af-a9e1-e8da0f958c34.png'
        )


@bot.command
async def test(ctx):
    print("passing")
    await side.example(ctx)


async def hello(ctx):
    await ctx.sent("hello")


alive()
bot.run(os.getenv('token'))
