from googletrans import Translator
import discord
from discord.ext import commands
from os import environ

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/',intents=intents)
bot_token = environ['translate_bot']
translator = Translator()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
    # if user reacts to any message with a question mark they're asked if they want to translate the contents of the message.
    # you can change the emoji to whatever you like by editing this if statement.
    if reaction.emoji == '❓':
        view = AddFlag(content = reaction.message.content)
        await reaction.message.reply(content="Translate to what language?", view=view, allowed_mentions = discord.AllowedMentions.none(),delete_after=10)
        await reaction.message.clear_reactions()

class AddFlag(discord.ui.View):
    def __init__(self, content : str):
        super().__init__()
        self.content = content

    # add other languages here. You could also add to this bot and make a slash command that takes and argument
    # that specifies the destination language.

    @discord.ui.button(label="English",style=discord.ButtonStyle.blurple)
    async def EngButton(self, interaction : discord.Interaction, button: discord.ui.Button):
        translation = translator.translate(self.content,dest='en').text
        await interaction.response.send_message(translation, ephemeral=True)

    @discord.ui.button(label="Russian",style=discord.ButtonStyle.blurple)
    async def RuButton(self, interaction : discord.Interaction, button: discord.ui.Button):
        translation = translator.translate(self.content,dest='ru').text
        await interaction.response.send_message(translation, ephemeral=True)

    @discord.ui.button(label="Turkish",style=discord.ButtonStyle.blurple)
    async def TurkButton(self, interaction : discord.Interaction, button: discord.ui.Button):
        translation = translator.translate(self.content,dest='tr').text
        await interaction.response.send_message(translation, ephemeral=True)

client.run(bot_token)