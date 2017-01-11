import discord
from appuselfbot import isBot
from discord.ext import commands
import asyncio


class Userinfo:

    def __init__(self, bot):
        self.bot = bot

    # Get user info
    @commands.command(pass_context=True)
    async def info(self, ctx):
        if ctx.invoked_subcommand is None:
            name = ctx.message.content[5:].strip()
            if name:
                try:
                    name = ctx.message.mentions[0]
                except:
                    name = ctx.message.server.get_member_named(name)
                if not name:
                    await self.bot.send_message(ctx.message.channel, isBot + 'Could not find user.')
                    return
            else:
                name = ctx.message.author

            em = discord.Embed(timestamp=ctx.message.timestamp, colour=0x708DD0)
            em.add_field(name='User ID', value=name.id, inline=True)
            em.add_field(name='Nick', value=name.nick, inline=True)
            em.add_field(name='Status', value=name.status, inline=True)
            em.add_field(name='In Voice', value=name.voice_channel, inline=True)
            em.add_field(name='Account Created', value=name.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
            em.add_field(name='Join Date', value=name.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
            em.set_thumbnail(url=name.avatar_url)
            em.set_author(name=name, icon_url='https://i.imgur.com/RHagTDg.png')
            await self.bot.send_message(ctx.message.channel, embed=em)
            await asyncio.sleep(2)
            await self.bot.delete_message(ctx.message)


def setup(bot):
    bot.add_cog(Userinfo(bot))
