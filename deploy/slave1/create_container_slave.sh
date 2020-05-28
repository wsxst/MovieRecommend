#!/bin/bash

CODE_HOME=/opt/homework

#IMG=centos-bigdata:v$1
IMG=centos-bigdata-slave:0527

SLAVE=slave$1
echo "Create and start container..."
docker run -d \
--restart=always \
--privileged \
--net="host" \
--name $SLAVE \
--hostname $SLAVE \
--add-host master:192.168.0.222 \
--add-host slave1:192.168.0.145 \
--add-host slave2:192.168.0.122 \
$IMG

#HADOOP_HOME=/usr/local/hadoop-2.7.3
#SPARK_HOME=/usr/local/spark-2.4.5-bin-without-hadoop
#docker cp ./configs/hadoop-env.sh $SLAVE:$HADOOP_HOME/etc/hadoop/hadoop-env.sh
#docker cp ./configs/spark-env.sh $SLAVE:$SPARK_HOME/conf/spark-env.sh 
#docker cp ./configs/slaves $SLAVE:$HADOOP_HOME/etc/hadoop/slaves
#docker cp ./configs/slaves $SLAVE:$SPARK_HOME/conf/slaves
docker exec -i $SLAVE bash -c "echo \"export SPARK_LOCAL_IP=slave$1\" >> /usr/local/spark-2.4.5-bin-without-hadoop/conf/spark-env.sh"

docker cp $CODE_HOME/copypub.sh $SLAVE:/root/

echo "Finished!"
docker ps

