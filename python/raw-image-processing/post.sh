#!/bin/bash

counter=0
while [ $counter -lt 100 ]
do
    curl -X POST \
    http://localhost:8080/api/image \
    -H 'Content-Type: multipart/form-data' \
    -H 'Postman-Token: 5f2da1c6-1ef8-4daa-a1e6-e76ad4bee54d' \
    -H 'cache-control: no-cache' \
    -F cell=@/Users/greenmon/Projects/daily-coding/python/print-raw-image/cells/cell$counter \
    -F number=$counter

    ((counter++))
done
