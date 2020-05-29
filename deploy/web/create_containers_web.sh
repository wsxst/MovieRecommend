#!/bin/bash
#IMG=centos:7
IMG=my-flask:0527
docker run -d --name nn -p 8080:80 --privileged my-nginx:0527
docker run -itd \
--restart=always \
--privileged \
--net="host" \
--name back \
--hostname back \
$IMG

