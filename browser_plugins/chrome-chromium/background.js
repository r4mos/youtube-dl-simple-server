chrome.browserAction.onClicked.addListener(function(tab) {
	chrome.tabs.update(tab.id, {url: "http://localhost:49149/" + tab.url});
});
