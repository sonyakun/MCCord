import py_mcws
from logging import getLogger
import nextcord
from nextcord.ext import commands

# MineCord設定
# 助けが必要？ Discord、sonyakun#6928にご連絡ください。
# Bot token: 取得したトークンはここに設定してください。設定方法は、MineCordの導入手順を参照してください。
# このオプションを変更した後、プログラムを再接続する必要があります
BotToken = "BOTTOKEN"

# ゲームからDiscordへのチャンネルリンク
# 構文は Channels = "DiscordのチャンネルID"

#
# チャンネルペアの最初の部分はDiscordチャンネル名ではありません！
# このオプションを適用するように変更した後、プログラムを再起動する必要があります。
Channels = 000000000000000000

# コンソールチャンネルの数値のID(チャンネル名ではありません)。コンソールチャンネルを全て無効にするなら、空のままにしてください。
DiscordConsoleChannelId = 000000000000000000

# デバッグ情報
# 有効化すると、Minecraft及びDiscordのチャット情報がコンソールに出力されます。
Debug = False

class WssClient(py_mcws.WsClient):
  logger = getLogger(__name__)
  wss = commands.Bot()
  def event_ready(self):
    logger.info(f'{self.host}:{self.port}で接続を開始しました')

    self.events = ["PlayerMessage", "PlayerDied"]

    async def event_PlayerMessage(self, event):
        channel = wss.get_channel(Channels)
        await channel.send(event)

    async def event_PlayerDied(self, event):
        channel = wss.get_channel(Channels)
        await channel.send(event)

    @wss.event
    async def on_message(seld, message):
        if message.channel.id == DiscordConsoleChannelId:
           cmd = await self.command(message.content)
           message.channel.send(cmd)
           if Debug == True:
             logger.info(f'コンソールで{message.author.id}が以下のコマンドを実行しました：/{message.content}')
        elif message.channel.id == Channels: 
           cmd = await self.command(f"say [§1discord§f]{message.author.name} {message.content}")
           if Debug == True:
             logger.info(f"say [discord]{message.author.name} {message.content}")
        else:
          return


    
      WssClient().wss.run(BotToken)