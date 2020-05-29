FROM centos:7

LABEL Discription="spark+hadoop on centos7" version="1.0"

#安装必备的软件包
RUN yum -y install net-tools
RUN yum -y install which
RUN yum -y install openssh-server openssh-clients
RUN yum -y install python3
RUN yum -y install vim
RUN yum install -y gcc-c++
RUN yum install -y pcre pcre-devel
RUN yum install -y zlib zlib-devel
RUN yum install -y openssl openssl-devel
RUN yum clean all

#配置SSH免密登录
RUN ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N ''
RUN ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''
RUN ssh-keygen -q -t dsa -f /etc/ssh/ssh_host_ed25519_key  -N ''
RUN ssh-keygen -f /root/.ssh/id_rsa -N ''
RUN touch /root/.ssh/authorized_keys
RUN cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
RUN echo "root:ss123456" | chpasswd
COPY ./configs/ssh_config /etc/ssh/ssh_config

#添加JDK 增加JAVA_HOME环境变量
ADD ./tools/jdk-8u212-linux-x64.tar.gz /usr/local/
ENV JAVA_HOME /usr/local/jdk1.8.0_212/
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

#添加Hadoop并设置环境变量
#ADD ./tools/hadoop-2.8.5.tar.gz /usr/local
ADD ./tools/hadoop-2.7.3.tar.gz /usr/local
#ENV HADOOP_HOME /usr/local/hadoop-2.8.5
ENV HADOOP_HOME /usr/local/hadoop-2.7.3

#添加Spark并设置环境变量
ADD ./tools/scala-2.12.7.tgz /usr/share
ADD ./tools/spark-2.4.5-bin-without-hadoop.tgz /usr/local
ENV SPARK_HOME /usr/local/spark-2.4.5-bin-without-hadoop

#将环境变量添加到系统变量中
#ENV PATH $HADOOP_HOME/bin:$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$NGINX_HOME/sbin:$PATH
ENV PATH $HADOOP_HOME/bin:$JAVA_HOME/bin:$PATH

#拷贝Hadoop和Spark相关的配置文件到镜像中
COPY ./configs/hadoop-env.sh $HADOOP_HOME/etc/hadoop/hadoop-env.sh
COPY ./configs/log4j.properties $SPARK_HOME/conf/log4j.properties
COPY ./configs/spark-env.sh $SPARK_HOME/conf/spark-env.sh
COPY ./configs/hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml
COPY ./configs/core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
COPY ./configs/yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml
COPY ./configs/mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
COPY ./configs/master $HADOOP_HOME/etc/hadoop/master
COPY ./configs/slaves $HADOOP_HOME/etc/hadoop/slaves
COPY ./configs/slaves $SPARK_HOME/conf/slaves

#创建数据目录
RUN mkdir -p /data/hadoop/dfs/data && \
    mkdir -p /data/hadoop/dfs/name && \
    mkdir -p /data/hadoop/tmp 
RUN mkdir -p /mnt/spark/tmp


#配置python相关
#RUN cp -r $SPARK_HOME/python/pyspark /usr/lib64/python3.6/site-packages
#RUN rm -f /usr/bin/python
#RUN ln -s /usr/bin/python3 /usr/bin/python
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH
ENV PYSPARK_PYTHON /usr/bin/python3
ENV SPARK_PYTHONPATH /usr/bin/python3
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
#RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple py4j==0.10.7
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple py4j
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple hdfs
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple tqdm
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask_cors


#开启SSH 22 端口
EXPOSE 22

#启动容器时执行的脚本文件
CMD ["/usr/sbin/sshd","-D"]

