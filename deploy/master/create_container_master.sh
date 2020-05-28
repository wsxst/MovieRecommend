#!/bin/bash
#IMG=centos-bigdata:v$1
IMG=centos-bigdata-master:0527

docker rm -f master

echo "Create and start container..."
docker run -d \
--restart=always \
--privileged \
--net="host" \
--name $1 \
--hostname $1 \
--add-host master:192.168.0.222 \
--add-host slave1:192.168.0.145 \
--add-host slave2:192.168.0.122 \
$IMG

