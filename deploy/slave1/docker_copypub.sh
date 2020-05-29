#!/bin/bash
docker cp /root/2.pub slave$1:/root/2.pub
rm -f /root/2.pub
docker exec -i slave$1 bash /root/copypub.sh
