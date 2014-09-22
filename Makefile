all: pack

pack:
	zip --quiet youtube-dl-simple-server youtube_dl_simple_server/*.py
	zip --quiet --junk-paths youtube-dl-simple-server youtube_dl_simple_server/__main__.py
	echo '#!/usr/bin/env python' > youtube-dl-simple-server
	cat youtube-dl-simple-server.zip >> youtube-dl-simple-server
	rm youtube-dl-simple-server.zip
	chmod a+x youtube-dl-simple-server

run: pack
	./youtube-dl-simple-server --verbose

install: pack
	mv youtube-dl-simple-server /usr/local/bin/youtube-dl-simple-server

uninstall:
	rm -f /usr/local/bin/youtube-dl-simple-server

clean:
	rm -f youtube-dl-simple-server