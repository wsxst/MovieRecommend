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
#sshpass -p "sspku1234*" ssh-copy-id -p 22 db
#sshpass -p "sspku1234*" ssh-copy-id s2
#sshpass -p "sspku1234*" ssh-copy-id s1
#sshpass -p "dashuju123" ssh-copy-id -p 22

docker exec -it $MASTER bash -c "echo \"export SPARK_LOCAL_IP=master\" >> /usr/local/spark-2.4.5-bin-without-hadoop/conf/spark-env.sh"

bash $CODE_HOME/clean_all_containers.sh

docker exec -i $MASTER bash -c "yum install -y sshpass"
ip_arr=("192.168.0.145" "192.168.0.122")
for i in 1 2
do
    ssh root@s$i bash $CODE_HOME/create_container_slave.sh $i && \
    docker exec -i $MASTER sshpass -p "ss123456" ssh-copy-id s$i && \
    sshpass -p "ss123456" ssh-copy-id -p 22 s$i
    #docker exec -i $MASTER sshpass -p "ss123456" scp ~/.ssh/id_rsa.pub root@slave$j:/root/1.pub && \
    #scp ~/.ssh/id_rsa.pub root@$h:/root/2.pub && \
    #ssh root@$h bash $CODE_HOME/docker_copypub.sh $j
done

ssh -p 22 root@db bash /root/start-mysql.sh
ssh -p 22 root@web bash $CODE_HOME/create_containers_web.sh
ssh root@s1 bash $CODE_HOME/start-nginx.sh

echo "Finished!"
docker ps

