# Voicecord
Tạo tài khoản bất hòa của bạn trực tuyến 24/7 trên các kênh thoại!

----

Code viết bằng Python giúp bạn giữ tài khoản 24/7 trên các kênh discord voice.

#### Please check out this if you want to add multiple tokens with just one file: [sealedsaucer.sellix.io/product/6359655010aec](https://sealedsaucer.sellix.io/product/6359655010aec)

---

The [main.py](https://github.com/SealedSaucer/Voicecord/blob/main/main.py) is the main file. [keep_alive.py](https://github.com/SealedSaucer/Voicecord/blob/main/keep_alive.py) prevents your repl from going to sleep. (If you have a replit hacker plan or want to run the script locally, then you can delete [this file](https://github.com/SealedSaucer/Voicecord/blob/main/keep_alive.py) and paste this code inside the [main.py](https://github.com/SealedSaucer/Voicecord/blob/main/main.py) file : 

</br>

```py
import discord
import os
from discord.ext import commands

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

GUILD_ID = ID_Server
CHANNEL_ID = ID_Channel

@client.event
async def on_ready():
    os.system('clear')
    print(f'Logged in as {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=False)
    print(f"Successfully joined {vc.name} ({vc.id})")

client.run(os.getenv("TOKEN"))
```


**DO NOT GIVE YOUR TOKEN TO OTHERS!**

Sử dụng [uptimerobot.com](https://uptimerobot.com) để thay thế bạn trực tuyến 24/7.

</br>

> ⭐ Vui lòng gắn dấu sao cho kho lưu trữ nếu điều này giúp ích cho bạn! :)

----

> Voicecord của FINN nói không với keylog 
