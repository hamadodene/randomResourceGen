from flask import Flask, send_file, make_response
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
from utils import *
from dotenv import load_dotenv
import multiprocessing

load_dotenv(dotenv_path='config_env.env')

app = Flask(__name__)


generator = ImageGenerator()

@app.route("/imagergb/<string:image_name>")
def generate_rgb_image(image_name):
    img_io = generator.generate_rgb_image()
    cache_control = random.choice(["no-cache", "public", "private"]) 
    response = make_response(send_file(img_io, mimetype='image/png'))
    response.headers['cache-control'] = cache_control
    return response

@app.route("/image/<string:image_name>")
def generate_image_from_api(image_name):
    img_io = generator.generate_image_from_api()
    cache_control = random.choice(["no-cache", "public", "private"])
    response = make_response(send_file(img_io, mimetype='image/png'))
    response.headers['cache-control'] = cache_control
    return response

if __name__ == "__main__":
    http_server = HTTPServer(WSGIContainer(app))
    PORTS = int(os.getenv('PORT', 8080))
    http_server.bind(PORTS)
    num_workers = int(os.getenv('NUM_WORKERS', multiprocessing.cpu_count()))
    http_server.start(num_workers)
    IOLoop.instance().start()
           