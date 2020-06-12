from flask import Flask
from gevent.pywsgi import WSGIServer
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   # pp.run(port=5000)
   http_server = WSGIServer(('', 5000), app)
   http_server.serve_forever()