import a2s
import time
from threading import Timer
from http.server import BaseHTTPRequestHandler, HTTPServer
address = ("104.192.0.78")
port = (27031)
hostName = "localhost"
serverPort = 8080
serveraddress = ("104.192.0.78", 27031)


class webDeploy(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        mapname = (a2s.info(serveraddress).map_name)
        maxplayers = (a2s.info(serveraddress).max_players)
        playercount = (a2s.info(serveraddress).player_count)
        servername = (a2s.info(serveraddress).server_name)
        jsonout = ('{\n"ls_zs": {\n\t"ip": "' + str(address) + ':' + str(port) + '",\n\t"Map": "' + str(mapname) + '",\n\t"MaxPLayers": ' +
        str(maxplayers) + ',\n\t"PLayerCount": ' + str(playercount) + ',\n\t"ServerName": "' + str(servername) + '",\n},\n}')
        self.wfile.write(bytes(jsonout, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), webDeploy)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
