from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello(request):
    return Response('Hello world!')

if __name__ == '__main__':
    port = int(os.environ.get('OPENSHIFT_PYTHON_PORT',8080))
    ip = os.environ.get('OPENSHIFT_PYTHON_IP','0.0.0.0')
    config = Configurator()
    config.add_route('hello_world', '/')
    config.add_view(hello, route_name='hello_world')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
