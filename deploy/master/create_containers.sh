#!/bin/bash

CODE_HOME=/opt/homework
MASTER=master

bash $CODE_HOME/create_container_master.sh $MASTER

#HADOOP_HOME=/usr/local/hadoop-2.7.3
#SPARK_HOME=/usr/local/spark-2.4.5-bin-without-hadoop
#HIVE_HOME=/usr/local/hive
#docker cp ./configs/hadoop-env.sh $MASTER:$HADOOP_HOME/etc/hadoop/hadoop-env.sh
#docker cp ./configs/spark-env.sh $MASTER:$SPARK_HOME/conf/spark-env.sh 
#docker cp ./configs/slaves $MASTER:$HADOOP_HOME/etc/hadoop/slaves
#docker cp ./configs/slaves $MASTER:$SPARK_HOME/conf/slaves
#docker cp ./configs/hive-site.xml $MASTER:$HIVE_HOME/conf/hive-site.xml
sshpass -p "sspku1234*" ssh-copy-id -p 22 db
sshpass -p "sspku1234*" ssh-copy-id s2
sshpass -p "sspku1234*" ssh-copy-id s1
sshpass -p "dashuju123" ssh-copy-id -p 22 web

docker exec -it $MASTER bash -c "echo \"export SPARK_LOCAL_IP=master\" >> /usr/local/spark-2.4.5-bin-without-hadoop/conf/spark-env.sh"

ssh root@s1 docker rm -f slave1 nn
ssh root@s2 docker rm -f slave2
ssh -p 22 root@db docker rm -f root_mysql_1
ssh -p 22 root@web docker rm -f nn back

docker exec -i $MASTER bash -c "yum install -y sshpass"
for i in 1 2
do
    ssh root@s$i bash $CODE_HOME/create_container_slave.sh $i && \
    docker exec -i $MASTER sshpass -p "ss123456" scp ~/.ssh/id_rsa.pub root@slave$i:/root/1.pub && \
    scp ~/.ssh/id_rsa.pub root@s$i:/root/2.pub && \
    ssh root@s$i bash $CODE_HOME/docker_copypub.sh $i
done

ssh -p 22 root@db bash /root/start-mysql.sh
ssh -p 22 root@web bash $CODE_HOME/create_container_web.sh
ssh root@s1 bash $CODE_HOME/start-nginx.sh

echo "Finished!"
docker ps

