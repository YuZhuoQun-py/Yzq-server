from wgsiserver.wgsi_server import WSGIServer
from app import app
# from blog import app as application
import atexit

if __name__ == "__main__":
    server = WSGIServer("127.0.0.1", 8889, app)
    atexit.register(server.server_close)
    print('running http://{}:{}'.format("127.0.0.1", 8889))
    server.server_forever()