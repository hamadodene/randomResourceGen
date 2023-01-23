import io
from PIL import Image
from flask import Flask, send_file, jsonify
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
from utils import *

app = Flask(__name__)


generator = ImageGenerator()

@app.route("/imagergb/<string:image_name>")
def generate_rgb_image(image_name):
    img_io = generator.generate_rgb_image()
    return send_file(img_io, mimetype='image/png')

@app.route("/image/<string:image_name>")
def generate_image_from_api(image_name):
    img_io = generator.generate_image_from_api()
    return send_file(img_io, mimetype='image/png')


if __name__ == "__main__":
    app.config.from_pyfile(os.path.join(os.path.dirname(__file__), 'config.py'))
    http_server = HTTPServer(WSGIContainer(app))
    http_server.bind(app.config['PORT'])
    http_server.start(app.config['NUM_WORKERS'])
    IOLoop.instance().start()
           