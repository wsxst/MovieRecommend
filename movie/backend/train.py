from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# delete the old file and put the new file
import os
os.system("hadoop fs -rm -r -skipTrash /data/ratings_small.csv")
os.system("hdfs dfs -put ratings_small.csv /data")

print("start")

conf = SparkConf()
conf.setMaster("spark://master:7077")
conf.setAppName("recommend_train")
conf.setExecutorEnv(key="executor-memory",value="3g")
conf.setExecutorEnv(key="driver-memory",value="9g")

sc = SparkContext(conf=conf)
#sc = SparkContext("local")

text = sc.textFile("/data/ratings_small.csv")
text=text .filter(lambda x: "movieId" not in x)
movieRatings=text.map(lambda x: x.split(",")[:3])   

print("start counting")
from pyspark.mllib.recommendation import ALS
model = ALS.train(movieRatings, 10, 10, 0.01)  

model.save(sc,"/data/model1")
print(model.recommendProducts(1, 5))
