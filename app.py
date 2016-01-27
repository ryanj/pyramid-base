from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def home(request):
	return Response("<head><link href='/static/css/site.css' rel='stylesheet' type='text/css' /></head><body><h1>Hello from Pyramid!</h1><p>Learn how to extend this example at <a href='http://trypyramid.com/'>TryPyramid.com</a>.</body>")

if __name__ == '__main__':
    port = int(os.environ.get('OPENSHIFT_PYTHON_PORT',8080))
    ip = os.environ.get('OPENSHIFT_PYTHON_IP','0.0.0.0')
    config = Configurator()
    #config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_view(home, route_name='home')
    config.add_static_view(name='static', path='static')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
