const xmlhttp = new XMLHttpRequest();
xmlhttp.onload = function () {
  var servers = JSON.parse(this.responseText);
  console.log(servers.zl_zs.IP);
  console.log(servers.zl_zs.Map);
  console.log(servers.zl_zs.MaxPlayers);
  console.log(servers.zl_zs.PlayerCount);
  console.log(servers.zl_zs.ServerName);
  document.getElementById("players-max").innerHTML =
    servers.zl_zs.PlayerCount + " Players Online";
  document.getElementById("zl_zs-name").innerHTML = servers.zl_zs.ServerName;
  document.getElementById("zl_zs-map").innerHTML = servers.zl_zs.Map.replaceAll(
    "_",
    " "
  ).replace("zs ", "");
  document.getElementById("zl_zs-players").innerHTML =
    servers.zl_zs.PlayerCount + " / " + servers.zl_zs.MaxPlayers;
  document.title = "Zombie Legacy " + servers.zl_zs.PlayerCount + " Online";
  document.getElementById("zl_zs-steam").href =
    "steam://connect/" + servers.zl_zs.IP;
  document.getElementById("zl_zs-mapimage").style.backgroundImage =
    "url('https://cdn.spco.xyz/zlzs/map-images/" + servers.zl_zs.Map + ".jpg')";
};
xmlhttp.open("GET", "https://zlzs.spco.xyz/api/servers.json");
xmlhttp.send();
