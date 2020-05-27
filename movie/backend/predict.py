from pyspark import SparkContext

sc = SparkContext("local")

from pyspark.mllib.recommendation import MatrixFactorizationModel
model = MatrixFactorizationModel.load(sc, '/data/model1')

def movie_predict(userid,movieNum):
	tmp = model.recommendProducts(userid, movieNum)
	result = []
	for r in tmp:
		result.append(r.product)
	return result


