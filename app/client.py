# Send request using reverse proxy

import concurrent.futures
import time
import requests
import random
import string
from requests.packages import urllib3
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='config_env.env')

URL = os.getenv("REVERSE_PROXY_URL")
num_requests = int(os.getenv("NUM_CLIENT_REQUEST"))
ssl_verification = True if os.getenv("SSL_VERIFICATION").lower == "true" else False

if not ssl_verification:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create a session with no SSL verification
session = requests.Session()
session.verify = ssl_verification

# Function to make a request using the session
def make_request(url):
    return session.get(url)

start_time = time.time()


def random_string(string_lenght=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_lenght))

def random_path():
    path = random.choice(["/imagergb/", "/image/"])
    return path

def createExecutor(max_workers=None):
    if max_workers is None:
        max_workers = concurrent.futures.cpu_count()
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(max_workers)) as executor:
        results = [executor.submit(make_request, URL + random_path() + random_string() + '.png') for i in range(num_requests)]
        for future in concurrent.futures.as_completed(results):
            start_time_req = time.time()
            # Get the response from the Future object
            response = future.result()
            end_time_req = time.time()
            print(f"Request {response.url} returned status code {response.status_code} in {end_time_req - start_time_req} seconds")
            print(f"request {response.url} headers is {response.headers} ")

    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / num_requests

    print(f"Sent {num_requests} requests in {total_time} seconds")
    print(f"Average time for each request: {average_time} seconds")


max_workers = os.getenv("MAX_WORKERS", None)
if max_workers:
    createExecutor(max_workers)
else:
    createExecutor()