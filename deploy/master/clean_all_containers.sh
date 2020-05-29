#!/bin/bash
ssh root@s1 docker rm -f slave1 nn
ssh root@s2 docker rm -f slave2
ssh -p 22 root@db docker rm -f root_mysql_1
ssh -p 22 root@web docker rm -f nn back

