#!/bin/bash

#docker exec -i master bash -c "ssh slave1 rm ~/id_rsa.pub"
#docker exec -i node1 /usr/local/hadoop-2.8.5/start-hadoop.sh
docker exec -i master /usr/local/hadoop-2.7.3/sbin/start-dfs.sh
docker exec -i master /usr/local/hadoop-2.7.3/sbin/start-yarn.sh

docker exec -i master hdfs dfs -mkdir -p /hive
docker exec -i master hdfs dfs -mkdir -p /hive/warehouse
docker exec -i master hdfs dfs -chmod 777 /hive
docker exec -i master hdfs dfs -chmod 777 /hive/warehouse
docker exec -i master hdfs dfs -mkdir -p /tmp/hive/
docker exec -i master hdfs dfs -chmod 777 /tmp/hive/

docker exec -i master /usr/local/spark-2.4.5-bin-without-hadoop/sbin/start-all.sh

#docker exec -i master schematool -dbType mysql -initSchema --verbose

docker exec -i master /usr/local/hbase/bin/start-hbase.sh

docker exec -d master hiveserver2


while :
do
    p=$(netstat -nlp|grep 10002|grep -v grep)
    if [ -n "$p" ]
    then
        break
    fi
done

echo "ok"
ssh -p 22 root@web docker exec -d back python3 /code/backend.py > /backend.log

docker exec -d master python3 /data/back.py > /backend.log
