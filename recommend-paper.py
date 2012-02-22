
import inputdata
import ratings

data = inputdata.raw_scores
r = ratings.ratings(data)
result = r.recommendations()
print result
