# MCCord
Minecraftのwebsocketを利用したDiscordSRV風のプログラム。
# 動作要件
Git Bashを導入していること
Python3.10以上を導入していること
DiscordBotのトークンを所持していること
# 必要ライブラリ
nextcord
https://github.com/sonyakun/py-mcws.git
インストール方法
pip install nextcord
pip install git+https://github.com/sonyakun/py-mcws.git
# トークン発行&MCCord設定手順(DiscordSRV Wikiより画像を引用)
まず、https://discord.com/developers/applications/ でアプリケーションを新しく作成します。すでにMineCordを動作させる予定のあるアプリケーションがある場合、そのアプリケーションを利用することも可能です。
![1](https://docs.discordsrv.com/images/create_application.png)
つぎに、作成したアプリケーションのbotタブに移動し、「Add Bot」をクリックします。
![2](https://docs.discordsrv.com/images/create_bot.png)
つぎに、Reset Tokenをクリックし、トークンを再生成します。
再生成したら、次にCopyを押してトークンをコピーします。
![3](https://docs.discordsrv.com/images/copy_token.png
次に、少し下のところにあるPrivileged Gateway Intentsをすべてオンにしてください。
そして保存します。
そして生成したトークンをmain.pyの「BOTTOKEN」の文字を削除してそこにペーストします。
これで準備完了です。
# 追記
Windowsでhostを0.0.0.0、127.0.0.1やlocalhostなどのローカルループバックアドレスをご利用する場合、以下のコマンドを管理者権限を与えたWindows PowerShellで実行する必要があります。
```
CheckNetIsolation.exe LoopbackExempt -a -n="Microsoft.MinecraftUWP_8wekyb3d8bbwe"
```
