#!/bin/bash

counter=0
while [ $counter -lt 256 ]
do
    curl -X POST \
    http://localhost:8080/api/image \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -H 'cache-control: no-cache' \
    -d "number=$counter&cell=4845444241403d3b3c3a43413f3d3d3d3b3b3a3b3e3d3b3c3a3b3d3b3a3b3c3b383b39393a3b3c3b3a38393a393b3b3b3c3b393839393b3a3c3b3e3e3838383a3b3b3c3b3c3e3739383b3b3c3c3d3e403a3b3b3c3a3c3d3e3e3e3a3a3b3c3c3c3e3e3e3f"

    ((counter++))
done
