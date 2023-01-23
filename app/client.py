# Send request using reverse proxy

import concurrent.futures
import time
import requests
import config
import random
import string

URL = config.REVERSE_PROXY_URL
num_requests = config.NUM_CLIENT_REQUEST
ssl_verification = True if config.SSL_VERIFICATION.lower == "true" else False

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

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(make_request, URL + '/imagergb/' + random_string() + '.png') for i in range(num_requests)]
    #results = [executor.submit(requests.get, url + '/image/' + random_string() + '.png') for i in range(num_requests)]]
    for future in concurrent.futures.as_completed(results):
        start_time_req = time.time()
        # Get the response from the Future object
        response = future.result()
        end_time_req = time.time()
        print(f"Request {response.url} returned status code {response.status_code} in {end_time_req - start_time_req} seconds")

end_time = time.time()

total_time = end_time - start_time
average_time = total_time / num_requests

print(f"Sent {num_requests} requests in {total_time} seconds")
print(f"Average time for each request: {average_time} seconds")