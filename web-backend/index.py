import a2s
import time
from threading import Timer
from http.server import BaseHTTPRequestHandler, HTTPServer
address = ("74.91.120.128")
port = (27015)

serveraddress = ("74.91.120.128", 27015)

servername = (a2s.info(serveraddress).server_name)
mapname = (a2s.info(serveraddress).map_name)
maxplayers = (a2s.info(serveraddress).max_players)
playercount = (a2s.info(serveraddress).player_count)
servername = (a2s.info(serveraddress).server_name)

api = open('servers.json', 'a')
api.truncate(0)

api.write(
'{\n\t"zl_zs": {\n\t\t"IP": "' + str(address) + ':' + str(port) + '",\n\t\t"Map": "' + str(mapname) + '",\n\t\t"MaxPlayers": ' +
str(maxplayers) + ',\n\t\t"PlayerCount": ' + str(playercount) +
',\n\t\t"ServerName": "' + str(servername) + '",\n\t\t "ServerShortName": "zl_zs"' '\n\t}\n}'    
)
api.close()