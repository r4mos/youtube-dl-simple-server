chrome.browserAction.onClicked.addListener(function(tab) {
  server = 'localhost';
  port = '49149'

  if (typeof(localStorage['ydlssServer']) != "undefined")
    server = localStorage['ydlssServer'];
  if (typeof(localStorage['ydlssPort']) != "undefined")
    port = localStorage['ydlssPort'];

  chrome.tabs.update(tab.id, {url: "http://" + server + ":" + port + "/" + tab.url});
});
