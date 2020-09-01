import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("Triz") != -1:
        await message.channel.send("My queen! She's definitely the most awesome queen in the world")

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="My Presence Spell detected a new member!", colour=0x29f297, description=f"{member} Joined!")

    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name="Personal Wizard", url="https://discordapp.com", icon_url="https://media.discordapp.net/attachments/750017263503147100/750052769376764024/Mago.png?width=374&height=499")
    embed.set_footer(text="Awesome Kingdom", icon_url="https://media.discordapp.net/attachments/750017263503147100/750024412153118821/Castle_Icon.jpg?width=499&height=499")

    embed.add_field(name="Sort Your Roles!", value="Go to <#745687148598132787> and choose your personal roles, to personalize your server experience!")
    embed.add_field(name="Make a little introduction about you to the citizens!", value="Everyone is excited to meet you! So, what you think about write a introdution in <#745687174783172616>?")
    embed.add_field(name="Meet the Staff team!", value="Take a look in <#746058266630553670> to know who are the team that makes our server works!")
    embed.add_field(name="Meet the Server!", value="Are you lost? So take a look in <#745846038157590558> and you will know each channel's function!")

    channel = client.get_channel(745692230353682564)

    await channel.send(embed=embed)

    await channel.send(f"<@&745835685818138719> Atention! {member.mention} Passed through the Kingdom's gate!")


client.run('NzQ2NDY5MzE3NTYxOTQyMDQ5.X0Axug.Zvnaf6qpjq8br6VRK3jL6dxa6WY')
