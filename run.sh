#!/bin/bash

docker stop api-rest || true && docker rm api-rest || true 

# run docker app
docker run -itd --name api-rest -p 3000:3000 josenarvaezfigueroa/miappcdk-ago22:1.0

sleep 20

docker logs api-rest
