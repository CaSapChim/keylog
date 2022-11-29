import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

#vào việc
GUILD_ID = ID_Server
CHANNEL_ID = ID_Channele

@client.event
async def on_ready():
    os.system('clear')
    print(f'Đăng Nhập Với Tên {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=False)
    print(f"Đã Tham Gia Thành Công {vc.name} ({vc.id})")

keep_alive()
client.run(os.getenv("TOKEN"))
#không nhập token ở "TOKEN"
#Nhập xong mất acc không chịu đâu
