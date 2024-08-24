import discord

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    channel = bot.get_channel(1245366165203587164)
    
    if message.channel == channel:
        embed = discord.Embed(title="고등학교를 입력해주세요", description="형식: ○○고등학교 ○○고", color=discord.Color.random())
        

        def check(m):
            return m.channel == channel and m.author != bot.user

        msg = await bot.wait_for('message', check=check)

        try:
            guild = discord.utils.get(bot.guilds, name='HAPPY')
            if msg.content.endswith("고"):
                role_name = msg.content

            elif msg.content.endswith("고등학교"):
                role_name = msg.content[:-3]

            else:
                raise Exception
            
            role = discord.utils.get(guild.roles, name=role_name)

            if not role:
                role = await guild.create_role(name=role_name, color=discord.Color.random())

            await msg.author.add_roles(role)

            role = discord.utils.get(guild.roles, name='[USER]')
            await msg.author.add_roles(role)
            
            await channel.purge(limit=None)
            await channel.send(embed=embed)

        except Exception:
            await channel.send("형식을 지켜주세요.")

bot.run(os.getenv("Token"))
