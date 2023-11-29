import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep} 1 - Não desrespeitar os membros.{os.linesep} 2 - Não postar conteúdo inapropriado.')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)

            

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
client.run('Meu token')