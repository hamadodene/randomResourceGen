import io
from PIL import Image
from flask import Flask, send_file
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import random
import os
import requests

class ImageGenerator:
    @staticmethod
    def generate_rgb_image():
        width = random.randint(300,800)
        height = random.randint(300,800)
        img = Image.new("RGB", (width, height), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        byte_io = io.BytesIO()
        img.save(byte_io, 'PNG')
        byte_io.seek(0)
        return byte_io

    @staticmethod
    def generate_image_from_api():
        width = random.randint(300,800)
        height = random.randint(300,800)
        # Call the Lorem Picsum API to generate a random image
        response = requests.get(f"https://picsum.photos/{width}/{height}")
        image = Image.open(io.BytesIO(response.content))

        byte_io = io.BytesIO()
        image.save(byte_io, 'PNG')
        byte_io.seek(0)
        return byte_io