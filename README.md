# MovieRecommend

## 电影推荐系统

```
-- movie
|-- frontend
|-- backend
```

## 日志分析系统

```
-- log
|-- frontend
|-- backend
```

## 部署步骤

1.将deploy文件夹中的脚本、docker镜像文件拷贝到对应的主机上
2.在各个节点上从文件加载docker镜像，分别在各主机上执行相应命令
```bash
#master
docker load < master.tar
#slave1
docker load < slave1.tar
#slave2
docker load < slave2.tar
#web
docker load < web.tar
#db
docker load < db.tar
```
3.为master节点配置IP与主机名的映射
```bash
echo "192.168.0.222    master" >> /etc/hosts
echo "192.168.0.145    slave1" >> /etc/hosts
echo "192.168.0.122    slave2" >> /etc/hosts
echo "192.168.0.157    web" >> /etc/hosts
echo "192.168.0.187    db" >> /etc/hosts
```
4.配置master免密登录其他主机，中间会要求输入其他主机的密码
```bash
ssh-copy-id master
ssh-copy-id slave1
ssh-copy-id slave2
ssh-copy-id web
ssh-copy-id db
```
5.在master节点上执行以下脚本，创建并启动所有主机上的容器，并启动集群中的大数据组件以及各web服务
```bash
cd /opt/homework
bash create_containers.sh && bash start-all.sh
```

## 集群参数配置

集群中大数据组件的配置文件可分别参见以下路径：
```bash
#hadoop: master节点master容器
$HADOOP_HOME/etc/hadoop
#spark: master节点master容器、slave1节点slave1容器、slave2节点slave2容器
$SPARK_HOME/conf
#hbase: master节点master容器
$HABSE_HOME/conf
#flume: master节点master容器
$FLUME_HOME/conf
#hive: master节点master容器
$HIVE_HOME/conf
```