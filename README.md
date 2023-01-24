# Random resource generator
This is a simple app for generate random resource, like image and text file for reverse proxy test.

## Startup instructions
Edit **env/client.env** and **env/server.env** files with the settings you need.

### Env variables
#### Client config
- **REVERSE_PROXY_URL** : Reverse proxy url you want to bench. You will need to configure reverse to route requests to the python server
- **NUM_CLIENT_REQUEST = 1000**: Number of requests to send
- **SSL_VERIFICATION=False**: Default is false. If true if the certificate verification fails, the request also fails.
- **MAX_WORKERS = 4** The number of workers that will forward requests. Default is the number of server CPUs.

#### Server config
- **PORT=8080**: Server listening port
- **NUM_WORKERS=4** The number of workers to handle incoming requests. Default is the number of server CPUs


### Build server and client

```
docker compose build server
docker compose build client
```

### Start server
```
docker compose run -d server
```
### Run beckmark
```
docker compose run --rm client
```

At the moment the server allows to generate images. The client then sends a series of random png image requests and the server will reply back with a random png image. The response will also contain a random control cache header. Based on the type of cache header, the reverse will have to decide whether to cache it or not.