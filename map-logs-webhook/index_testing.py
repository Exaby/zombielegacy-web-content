from discord_webhook import DiscordWebhook, DiscordEmbed
import a2s
import threading
import time
address = ("104.192.0.78")
port = (27031)
serveraddress = ("104.192.0.78", 27031)


def webhook():
    mapname = (a2s.info(serveraddress).map_name)
    maxplayers = (a2s.info(serveraddress).max_players)
    playercount = (a2s.info(serveraddress).player_count)
    servername = (a2s.info(serveraddress).server_name)
    laststand = DiscordWebhook(
        url='https://discord.com/api/webhooks/957856390909673503/P0R4Ft6-pJCPMXImGdPxkP4CVEe0uBH3SXONi4VGlAthNTaVUDXkOzwIWucNZnE3MvQf', username=(servername))
    embed = DiscordEmbed(title=('Now playing ' + str(mapname) + ' with ' + str(playercount) + ' players'),
                         description=('steam://connect/' + str(address) + ':' + str(port)), color='03b2f8')
    embed.set_image(
        url=('https://files.sunrust.org/map_images/' + str(mapname) + '.jpg'))
    laststand.add_embed(embed)
    response = laststand.execute()


def changemap():
    tmpmap = (a2s.info(serveraddress).player_count)
    time.sleep(8)
    setwebhook = (tmpmap != (a2s.info(serveraddress).player_count))
    while setwebhook:
        webhook()
        setwebhook = False
    changemap()

changemap()
