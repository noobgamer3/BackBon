import discord
import asyncio
from discord.ext import commands

client = commands.Bot(description="BackBon Official Bot", command_prefix="tk!", pm_help = True)
client.remove_command('help')

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started <BackBon>')

@client.event
async def on_reaction_add(reaction , user):
  if reaction.emoji == '🇬':
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = 'tk!invite or tk!authlink',value ='Use it to invite our bot to your server',inline = False)
    embed.add_field(name = 'tk!enterme',value ='Use it like ``tk!enterme <giveaway channel>`` to enter in a giveaway running in a particular channel',inline = False)
    embed.add_field(name = 'tk!whoami',value ='Tells you what your username is; this is how you are saved in the file.',inline = False)
    embed.add_field(name = 'tk!real',value ='Tells you what the real username of a mentioned user is. This is how they are saved in the file.',inline = False)
    embed.add_field(name = 'tk!choose',value ='Chooses between multiple choices.',inline = False)
    embed.add_field(name = 'tk!poll ',value ='Use it like ``tk!poll "Question" "Option1" "Option2" ..... "Option9"``.',inline = False)
    embed.add_field(name = 'tk!guess ',value ='To play guess game use ``tk!guess <number> and number should be between 1-10``',inline = False)
    embed.add_field(name = 'tk!github ',value ='Use it like- ``tk!github uksoftworld/DarkBot``',inline = False)
    embed.add_field(name = 'tk!bottutorial ',value ='Use it like ``tk!bottutorial <tutorial name by darklegend>``',inline = False)
    embed.add_field(name = 'tk!dyno ',value ='Use it like ``tk!dyno <dyno command name>``',inline = False)
    embed.add_field(name = 'tk!happybirthday @user ',value ='To wish someone happy birthday',inline = False)
    embed.add_field(name = 'tk!verify ',value ='Use it to get verified role. Note- It needs proper setup.',inline = False)
    await client.send_message(user,embed=embed)
  if reaction.emoji == '🇲':
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Moderation Commands Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'tk!say(Admin permission required) ',value ='Use it like ``tk!say <text>``',inline = False)
    embed.add_field(name = 'tk!showme(Requires a role named Giveaways)',value ='To see how many people are taking part in giveaway',inline = False)
    embed.add_field(name = 'tk!pickwinner(Requires a role named Giveaways)',value ='To pick winner',inline = False)
    embed.add_field(name = 'tk!embed(Admin permission required) ',value ='Use it like ``tk!embed <text>``',inline = False)
    embed.add_field(name = 'tk!membercount(Kick members Permission Required) ',value ='Use it like ``tk!membercount`` to get membercount',inline = False)
    embed.add_field(name = 'tk!removemod(Admin Permission Required)',value ='Use it like ``tk!removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.',inline = False)
    embed.add_field(name = 'tk!makemod(Admin Permission Required)',value ='Use it like ``tk!makemod @user`` to make him mod. Note-You need Moderator role in your server below darkbot to use it.',inline = False)
    embed.add_field(name = 'tk!friend(Admin Permission Required) ',value ='Use it like ``tk!friend @user`` to give anyone Friend of Owner role',inline = False)
    embed.add_field(name = 'tk!role(Manage Roles Permission Required)',value ='Use it like ``tk!role @user <rolename>``.',inline = False)
    embed.add_field(name = 'tk!setnick(Manage nickname permission required)',value ='Use it like ``tk!setnick @user <New nickname>`` to change the nickname of tagged user.',inline = False)
    embed.add_field(name = 'tk!english(Kick members Permission Required)',value ='Use it like ``tk!english @user`` when someone speaks languages other than English.',inline = False)
    embed.add_field(name = 'tk!serverinfo(Kick members Permission Required) ',value ='Use it like ``tk!serverinfo`` to get server info',inline = False)
    embed.add_field(name = 'tk!userinfo(Kick members Permission Required) ',value ='Use it like ``tk!userinfo @user`` to get some basic info of tagged user',inline = False)
    react_message = await client.send_message(user,embed=embed)
    reaction = '⏭'
    await client.add_reaction(react_message, reaction)
    
  if reaction.emoji == '⏭':
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Moderation Commands Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'tk!kick(Kick members Permission Required)',value ='Use it like ``tk!kick @user`` to kick any user',inline = False)
    embed.add_field(name = 'tk!roles(Kick members Permission Required) ',value ='Use it to check roles present in server',inline = False)
    embed.add_field(name = 'tk!clear(Manage Messages Permission Required)',value ='Use it like ``tk!purge <number>`` to clear any message',inline = False)
    embed.add_field(name = 'tk!mute(Mute members Permission Required)',value ='Use it like ``tk!mute @user <time>`` to mute any user',inline = False)
    embed.add_field(name = 'tk!unmute(Mute members Permission Required) ',value ='Use it like ``tk!unmute @user`` to unmute anyone',inline = False)
    embed.add_field(name = 'tk!ban(Ban members Permission Required) ',value ='Use it like ``tk!ban @user`` to ban any user',inline = False)
    embed.add_field(name = 'tk!rules(Kick members Permission Required)',value ='Use it like ``tk!rules @user <violation type>`` to warn user',inline = False)
    embed.add_field(name = 'tk!warn(Kick members Permission Required)',value ='Use it like ``tk!warn @user <violation type>`` to warn any user',inline = False)    
    embed.add_field(name = 'tk!norole(Kick members Permission Required) ',value ='Use it like ``tk!norole @user`` to warn anyone if he/she asks for promotion',inline = False)
    embed.add_field(name = 'tk!getuser(Kick members Permission Required) ',value ='Use it like ``tk!getuser @rolename`` to get list of all users having a particular role',inline = False)
    react_message = await client.send_message(user,embed=embed)
    reaction = '⏮'
    await client.add_reaction(react_message, reaction)
    
  if reaction.emoji == '⏮':
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Moderation Commands Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'mv!setupwelcomer(Admin Permission required) ',value ='Simply use it to make a channel named ★彡-welcome-彡★ so that bot will send welcome and leaves logs in that channel.',inline = False)
    embed.add_field(name = 'tk!say(Admin permission required) ',value ='Use it like ``tk!say <text>``',inline = False)
    embed.add_field(name = 'tk!embed(Admin permission required) ',value ='Use it like ``tk!embed <text>``',inline = False)
    embed.add_field(name = 'tk!membercount(Kick members Permission Required) ',value ='Use it like ``tk!membercount`` to get membercount',inline = False)
    embed.add_field(name = 'tk!removemod(Admin Permission Required)',value ='Use it like ``tk!removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.',inline = False)
    embed.add_field(name = 'tk!makemod(Admin Permission Required)',value ='Use it like ``tk!makemod @user`` to make him mod. Note-You need Moderator role in your server below darkbot to use it.',inline = False)
    embed.add_field(name = 'tk!friend(Admin Permission Required) ',value ='Use it like ``tk!friend @user`` to give anyone Friend of Owner role',inline = False)
    embed.add_field(name = 'tk!role(Manage Roles Permission Required)',value ='Use it like ``tk!role @user <rolename>``.',inline = False)
    embed.add_field(name = 'tk!setnick(Manage nickname permission required)',value ='Use it like ``tk!setnick @user <New nickname>`` to change the nickname of tagged user.',inline = False)
    embed.add_field(name = 'tk!english(Kick members Permission Required)',value ='Use it like ``tk!english @user`` when someone speaks languages other than English.',inline = False)
    embed.add_field(name = 'tk!serverinfo(Kick members Permission Required) ',value ='Use it like ``tk!serverinfo`` to get server info',inline = False)
    embed.add_field(name = 'tk!userinfo(Kick members Permission Required) ',value ='Use it like ``tk!userinfo @user`` to get some basic info of tagged user',inline = False)
    react_message = await client.send_message(user,embed=embed)
    reaction = '⏭'
    await client.add_reaction(react_message, reaction)
  if reaction.emoji == '🏵':
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Setup Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'Setting up Welcomer log(Admin Permission required) ',value ='Use tk!setupwelcomer. It will add a welcome channel. Just put that channel in your desired category and it will send all logs there.',inline = False)
    embed.add_field(name = 'Setting up Giveaway feature(Manage roles permission required) ',value ='Just add a role named ``Giveaways`` and give that role to user who wanna be giveaway manager. Then use ``tk!help`` and check giveaway commands.',inline = False)
    embed.add_field(name = 'Setting up Reaction Verification(Admin Permission required) ',value ='Just add a role named ``Verified`` then remove permission from everyone to send message in all channels. Also add permission of verified role to send message in chatting channels. Then use ``tk!setreactionverify`` it will automatically add a channel and post information about verification.',inline = False)
    await client.send_message(user,embed=embed)    
    
@client.event
async def on_message(message):
	await client.process_commands(message)
  
@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'Having doubts? Join our server and clear your doubts. Server link: https://discord.gg/bYjScDG ',value ='that you can use:',inline = False)
    embed.add_field(name = 'React with 🇲 ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
    embed.add_field(name = 'React with 🇬 ',value ='Explaines all the commands which are usable by everyone.',inline = False)
    embed.add_field(name = 'React with 🏵 ',value ='Explaines how to setup some stuffs like Giveaway feature and welcomer feature in your server',inline = False)
    react_message = await client.send_message(author,embed=embed)
    reaction1 = '🇲'
    reaction2 = '🇬'
    reaction3 = '🏵'
    await client.add_reaction(react_message, reaction1)
    await client.add_reaction(react_message, reaction2)
    await client.add_reaction(react_message, reaction3)
    await client.say('📨 Check DMs For Information')

client.run('NTE2OTI3ODU5MDYzOTE0NDk3.DuACwQ.xd0jh10J6NNJFo56OHVlfSxEni0')