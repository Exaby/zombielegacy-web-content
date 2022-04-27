from discord_webhook import DiscordWebhook, DiscordEmbed
import a2s
import threading
import time
address = ("74.91.120.128")
port = (27015)
serveraddress = ("74.91.120.128", 27015)


def webhook():
    mapname = (a2s.info(serveraddress).map_name)
    maxplayers = (a2s.info(serveraddress).max_players)
    playercount = (a2s.info(serveraddress).player_count)
    servername = (a2s.info(serveraddress).server_name)
    laststand = DiscordWebhook(
        url='https://discord.com/api/webhooks/968328265288790117/GHzU-k_jhMEr6PKZBMZgh_WcLal3CVNrJkuJ1UaSGFjBjPEKJlxW0GTA6D_DPsKSBD-i', username=(servername))
    embed = DiscordEmbed(title=('Now playing ' + str(mapname) + ' with ' + str(playercount) + ' players'),
                         description=('steam://connect/' + str(address) + ':' + str(port)), color='03b2f8')
    embed.set_image(
        url=('https://files.sunrust.org/map_images/' + str(mapname) + '.jpg'))
    laststand.add_embed(embed)
    response = laststand.execute()


def changemap():
    tmpmap = (a2s.info(serveraddress).map_name)
    time.sleep(8)
    setwebhook = (tmpmap != (a2s.info(serveraddress).map_name))
    while setwebhook:
        webhook()
        setwebhook = False
    changemap()

changemap()
