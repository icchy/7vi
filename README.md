# 7vi (wwwvi)
7vi helps you to edit web resources for debugging purpose.

## Prerequisites
* install [mitmproxy](https://mitmproxy.org/) with `pip install mitimproxy --user`
* configure SSL certificate if you will edit HTTPS resources

## Usage
start 7vi to log all HTTP/HTTPS traffic
```
~$ mkdir workdir
~$ 7vi # spawns mitmproxy, hit Ctrl-C when you want stop them
```

access web page via proxy (localhost:8080 by default).
```
~$ curl -x localhost:8080 mitmproxy.org 
<html>
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
<hr><center>CloudFront</center>
</body>
</html>
```

then launch another shell on same directory
**NOTE: enter same URL appeared on mitmproxy's log**
```
~$ 7vi "http://mitmproxy.org/" # spawns editor you set on $EDITOR, or vim
```

after editing on editor, the response content would be overwritten
```
~$ curl -x localhost:8080 mitmproxy.org
edited by 7vi
```

you can restore default contents from server by deleting file you are editing
```
# execute `:!rm %` on vim
curl -x localhost:8080 mitmproxy.org
<html>       
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
<hr><center>CloudFront</center>
</body>
</html>
```


## TODO
* edit everything
  * HTTP response header
  * WebSocket
  * etc...

* enable to keep specific variables rendered by server (ex. CSRF token)
* history management