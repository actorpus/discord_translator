import discord
from googletrans import Translator


client = discord.Client()
translator = Translator()

translate_to = "nl"
translate_from = "gb"
offset = 0x1F1E6 - 0x41

active = False


@client.event
async def on_ready():
    print('connected to account "{0.user}"'.format(client))


@client.event
async def on_message(ctx):
    global translate_to, active

    if ctx.author.id == <YOUR ID GOES HERE>:
        if ctx.content[0] == "/":
            if ctx.content[1:13] == "translate_to":
                translate_to = ctx.content[14:16].lower()

                await ctx.edit(content=ctx.content + " DONE")
                await ctx.delete(delay=3)

            elif ctx.content[1:19] == "translate_activate":
                active = True

                await ctx.edit(content=ctx.content + " DONE")
                await ctx.delete(delay=3)

            elif ctx.content[1:21] == "translate_deactivate":
                active = False

                await ctx.edit(content=ctx.content + " DONE")
                await ctx.delete(delay=3)

        elif ctx.channel.id in [
            <ALLOUD CHANNELS GOES HERE>
        ] and active:
        
            new = translator.translate(ctx.content, dest=translate_to)

            old_flag = str(chr(ord(translate_from.upper()[0]) + offset) + chr(ord(translate_from.upper()[1]) + offset))
            new_flag = str(chr(ord(translate_to.upper()[0]) + offset) + chr(ord(translate_to.upper()[1]) + offset))

            await ctx.edit(content="%s ```%s```%s ```%s```" % (old_flag, ctx.content, new_flag, new.text))


client.run("<YOUR TOKEN GOES HERE>")
