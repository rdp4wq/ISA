__author__ = 'Patrick'
from pyspark import SparkContext
from itertools import combinations

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.txt", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: tuple(line.split("\t")))

distinct_pairs = pairs.distinct()
output = pairs.collect()
print("Pairs")
for user, page in output:
	print("user: %s, page: %s" % (user, page))

output = distinct_pairs.collect()
print("Distinct Pairs")
for user, page in output:
	print("user: %s, page: %s" % (user, page))


user_pages = distinct_pairs.groupByKey()
user_pages = user_pages.mapValues(lambda pages: sorted(pages))
output = user_pages.collect()
print("User Pages")
for user, pages in output:
	print("user: %s, pages: %s" % (user, list(pages)))

user_pairs = user_pages.flatMapValues(lambda user_pages: combinations(user_pages, 2))
output = user_pairs.collect()
print("User Page Pairs")
for user, pair in output:
	print("user: %s, page pairs: %s" % (user, pair))

reverse_user_pairs = user_pairs.map(lambda user_pair: (user_pair[1], user_pair[0]))
output = reverse_user_pairs.collect()
print("Reverse User Pairs")
for pair, user in output:
	print("pair: %s, user: %s" % (pair, user))

grouped_pairs = reverse_user_pairs.groupByKey()
output = grouped_pairs.collect()
print("Grouped Pairs")
for pair, users in output:
	print("pair: %s, users: %s" % (pair, list(users)))

pair_counts = grouped_pairs.mapValues(lambda users: len(users))
output = pair_counts.collect()
print("Pair Counts")
for pair, count in output:
	print("pair: %s, count: %s" % (pair, count))

significant_pairs = pair_counts.filter(lambda pair: pair[1] >= 3).keys()
output = significant_pairs.collect()
print("Significant Pairs")
for pair in output:
	print("pair: %s" % (pair, ))

sc.stop()
