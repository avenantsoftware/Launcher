#!/usr/bin/python
import SimpleHTTPServer, SocketServer, os, httplib, urllib

# port of launcher
port = 4040
# ip address of launcher
host = '192.168.2.3'
# sh script folder
folder = '/home/htpc/Launcher/'

def pushover(str):      
  conn = httplib.HTTPSConnection("api.pushover.net:443")
  conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "yourkeyhere",
    "user": "yourkeyhere",
    "message": str,
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()
  return;

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
             urlparse.urlparse(self.path)
        elif self.path.startswith('/chrome'):
             pushover('Chrome starts')
             return os.system(folder + 'chrome')     
        elif self.path.startswith('/killchrome'):
             pushover('Chrome stops')
             return os.system('killall chrome')
        elif self.path.startswith('/xbmc'):
             pushover('XBMC starts')
             return os.system(folder + 'xbmc')
        elif self.path.startswith('/killxbmc'):
             pushover('XBMC stops')
             return os.system('killall -9 /usr/lib/xbmc/xbmc.bin')
        elif self.path.startswith('/taskmanager'):
             pushover('Taskmanager starts')
             return os.system(folder + 'taskmanager')
        elif self.path.startswith('/killtaskmanager'):
             pushover('Taskmanager stops')
             return os.system('killall gnome-system-monitor')
        elif self.path.startswith('/router'):
             pushover('Router login starts')
             return os.system(folder + 'router')
        elif self.path.startswith('/terminal'):
             pushover('Terminal starts')
             return os.system(folder + 'terminal')
        elif self.path.startswith('/killterminal'):
             pushover('Terminal stops')
             return os.system('killall gnome-terminal')
        elif self.path.startswith('/gmail'):
             pushover('Gmail starts')
             return os.system(folder + 'gmail')
        elif self.path.startswith('/nemo'):
             pushover('Nemo starts')
             return os.system(folder + 'nemo')
        elif self.path.startswith('/killnemo'):
             pushover('Nemo stops')
             return os.system('killall nemo')
        elif self.path.startswith('/wiki'):
             pushover('Wikipedia starts')
             return os.system(folder + 'wiki')
        elif self.path.startswith('/imdb'):
             pushover('Imdb starts')
             return os.system(folder + 'imdb')
        elif self.path.startswith('/youtube'):
             pushover('Youtube starts')
             return os.system(folder + 'youtube')                                                  
        elif self.path.startswith('/changebg'):
             pushover('Background wallpaper changes')
             return os.system(folder + 'changebg')         
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer((host, port), Handler)
server.serve_forever()
