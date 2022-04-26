var previous = null;
var current = null;
setInterval(function() {
    $.getJSON("http://127.0.0.1:5500/servers.json", function(json) {
        current = JSON.stringify(json);            
        if (previous && current && previous !== current) {
            console.log('refresh');
            location.reload();
        }
        previous = current;
    });                       
}, 2000);   