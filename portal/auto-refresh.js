var previous = null;
var current = null;
setInterval(function() {
    $.getJSON("https://zlzs.spco.xyz/api/servers.json", function(json) {
        current = JSON.stringify(json);            
        if (previous && current && previous !== current) {
            console.log('refresh');
            location.reload();
        }
        previous = current;
    });                       
}, 2000);   
