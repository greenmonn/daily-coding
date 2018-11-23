#!/bin/bash

counter=0
while [ $counter -lt 256 ]
do
    curl -X POST \
    http://localhost:8080/api/image \
    -H 'Content-Type: multipart/form-data' \
    -H 'Postman-Token: 5f2da1c6-1ef8-4daa-a1e6-e76ad4bee54d' \
    -H 'cache-control: no-cache' \
    -F cell=@cells/cell$counter \
    -F number=$counter

    ((counter++))
done
